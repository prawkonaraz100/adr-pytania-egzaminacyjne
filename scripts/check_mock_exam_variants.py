#!/usr/bin/env python3
"""Validate learner-facing mock exam variants and keys against the current bank."""
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMS = ROOT / "podstawowy" / "egzamin-probny"
LETTERS = "ABC"


def remap_explanation(text, mapping):
    # Remap explicit references to answer choices when the printed option order changes.
    text = re.sub(
        r"\b(warianty|odpowiedzi)\s+([ABC])\s+i\s+([ABC])\b",
        lambda m: f"{m.group(1)} {mapping.get(m.group(2), m.group(2))} i {mapping.get(m.group(3), m.group(3))}",
        text,
        flags=re.IGNORECASE,
    )
    return re.sub(
        r"\b(odpowiedź|opcja|wariant|warianty|odpowiedzi)\s+([ABC])\b",
        lambda m: f"{m.group(1)} {mapping.get(m.group(2), m.group(2))}",
        text,
        flags=re.IGNORECASE,
    )


def longest_run(values):
    best = run = 0
    previous = None
    for value in values:
        run = run + 1 if value == previous else 1
        previous = value
        best = max(best, run)
    return best


def near_duplicate_pairs(questions, threshold=0.70):
    """Flag likely redundant exam questions; deterministic editorial heuristic.

    Compare token sets of stems after basic punctuation normalization.
    Only flag at least five shared meaningful tokens to avoid short-question noise.
    This is a regression guard, not a verdict that two legal questions are identical.
    """
    def words(stem):
        return set(re.findall(r"[^\\W_]{3,}", stem.casefold(), flags=re.UNICODE))
    flagged = []
    for i, left in enumerate(questions):
        a = words(left.get("stem", ""))
        for right in questions[i + 1:]:
            c = words(right.get("stem", ""))
            common = a & c
            union = a | c
            if union and len(common) >= 5 and len(common) / len(union) >= threshold:
                flagged.append((left.get("id"), right.get("id")))
    return flagged


def heuristic_warnings(rows):
    warnings = []
    cue = re.compile(
        r"\b(bo|ponieważ|dlatego|oznacza|wskazuje|wynika|nie jest|nie są|nie oznacza|"
        r"nie zastępuje|zamiast|natomiast|jednak|należy|trzeba|pozwala|wymaga|może)\b",
        re.IGNORECASE,
    )
    for row in rows:
        explanation = (row.get("explanation") or "").strip()
        reasons = []
        if re.match(r"^(?:ADR\s*)?\d+(?:\.\d+){1,}", explanation, re.IGNORECASE):
            reasons.append("zaczyna się od numeru przepisu")
        module_refs = set(re.findall(r"ADR-B-\d{2}", explanation))
        if len(module_refs) > 3:
            reasons.append(f"zawiera {len(module_refs)} odwołań do działów")
        if not cue.search(explanation):
            reasons.append("brak prostego sygnału wyjaśniającego")
        if reasons:
            warnings.append((row.get("id", "<brak-ID>"), "; ".join(reasons)))
    return warnings


def audit(root=ROOT):
    bank_path = root / "podstawowy" / "questions.jsonl"
    bank_bytes = bank_path.read_bytes()
    bank_blob_sha = hashlib.sha1(b"blob " + str(len(bank_bytes)).encode("ascii") + bytes([0]) + bank_bytes).hexdigest()
    rows = [json.loads(line) for line in bank_bytes.decode("utf-8").splitlines() if line.strip()]
    bank = {row["id"]: row for row in rows}
    errors, stats, all_ids = [], [], []
    for number in range(1, 6):
        variant_path = root / "podstawowy" / "egzamin-probny" / f"wariant-{number:03}.json"
        key_path = root / "podstawowy" / "egzamin-probny" / f"klucz-{number:03}.json"
        exam, key = json.loads(variant_path.read_text(encoding="utf-8")), json.loads(key_path.read_text(encoding="utf-8"))
        questions, answers = exam.get("questions", []), key.get("answers", [])
        prefix = f"wariant-{number:03}"
        if exam.get("source_bank_head") != bank_blob_sha:
            errors.append(f"{prefix}: source_bank_head nie wskazuje aktualnego blobu questions.jsonl")
        if key.get("source_bank_head") != bank_blob_sha:
            errors.append(f"{prefix}: klucz nie wskazuje aktualnego blobu questions.jsonl")
        if len(questions) != 30 or len(answers) != 30:
            errors.append(f"{prefix}: arkusz/klucz musi mieć dokładnie 30 pytań")
        if exam.get("publication_authorized") is not False or "answer_key_internal_only" in exam:
            errors.append(f"{prefix}: arkusz nie może ujawniać klucza ani być zatwierdzony do publikacji")
        ids = [q.get("id") for q in questions]
        for left_id, right_id in near_duplicate_pairs(questions):
            errors.append(f"{prefix}: potencjalnie powtórzone pytania {left_id} i {right_id}; sprawdź sens i podstawę ADR")
        if len(ids) != len(set(ids)):
            errors.append(f"{prefix}: powtórzone ID w arkuszu")
        all_ids.extend(ids)
        actual_modules = dict(sorted(Counter(q.get("module_id") for q in questions).items()))
        declared_modules = dict(sorted(exam.get("module_distribution", {}).items()))
        if actual_modules != declared_modules or len(actual_modules) != 13:
            errors.append(f"{prefix}: rozkład działów nie zgadza się z deklaracją albo brakuje działu")
        if sum(actual_modules.values()) != 30 or any(count not in (2, 3) for count in actual_modules.values()):
            errors.append(f"{prefix}: oczekiwano 30 pytań i 2–3 pytań z każdego z 13 działów")
        letters = []
        strictly_longest_correct = 0
        for index, q in enumerate(questions):
            qid = q.get("id")
            source = bank.get(qid)
            answer = answers[index] if index < len(answers) else {}
            if source is None:
                errors.append(f"{prefix}: {qid} nie istnieje w banku")
                continue
            if answer.get("id") != qid or answer.get("number") != q.get("number"):
                errors.append(f"{prefix}: klucz nie zachowuje kolejności/ID przy {qid}")
            expected_lesson_path = f"../lekcje/{source.get('module_id')}.md"
            if answer.get("lesson_path") != expected_lesson_path:
                errors.append(f"{prefix}: brak odnośnika do właściwej lekcji dla {qid}; oczekiwano {expected_lesson_path}")
            if not (root / "podstawowy" / "lekcje" / f"{source.get('module_id')}.md").is_file():
                errors.append(f"{prefix}: plik lekcji nie istnieje dla {qid}: {source.get('module_id')}")
            if q.get("number") != index + 1:
                errors.append(f"{prefix}: numeracja arkusza nie jest ciągła przy {qid}")
            if q.get("module_id") != source.get("module_id") or q.get("stem") != source.get("stem"):
                errors.append(f"{prefix}: treść pytania lub dział nie zgadza się z bankiem: {qid}")
            options = q.get("options", {})
            if Counter(options.values()) != Counter(source.get("options", {}).values()):
                errors.append(f"{prefix}: zestaw odpowiedzi różni się od banku: {qid}")
                continue
            mapping = {old: next((new for new in LETTERS if options.get(new) == source["options"][old]), None) for old in LETTERS}
            correct_letter = answer.get("correct_option")
            if correct_letter not in LETTERS or options.get(correct_letter) != source["options"][source["correct_option"]]:
                errors.append(f"{prefix}: poprawna odpowiedź w kluczu nie wskazuje tekstu poprawnego z banku: {qid}")
            if answer.get("explanation") != remap_explanation(source.get("explanation", ""), mapping):
                errors.append(f"{prefix}: explanation w kluczu nie jest zsynchronizowane z bankiem: {qid}")
            if len((answer.get("explanation") or "").strip()) < 200:
                errors.append(f"{prefix}: explanation poniżej 200 znaków: {qid}")
            choice_lengths = {letter: len(options[letter]) for letter in LETTERS}
            max_length = max(choice_lengths.values())
            if choice_lengths[correct_letter] == max_length and sum(value == max_length for value in choice_lengths.values()) == 1:
                strictly_longest_correct += 1
            letters.append(correct_letter)
        strict_rate = strictly_longest_correct / len(questions) if questions else 0.0
        if strict_rate > 0.18:
            errors.append(f"{prefix}: poprawna odpowiedź jest jedyną najdłuższą w {strictly_longest_correct}/30 pytań ({strict_rate:.1%}; limit 18%)")
        freq = {letter: letters.count(letter) for letter in LETTERS}
        max_run = longest_run(letters)
        if any(freq[letter] < 8 for letter in LETTERS):
            errors.append(f"{prefix}: każda litera musi wystąpić co najmniej 8 razy, rozkład={freq}")
        if max_run > 3:
            errors.append(f"{prefix}: seria tej samej litery ma długość {max_run} (>3)")
        stats.append({"variant": number, "letters": freq, "longest_run": max_run, "modules": actual_modules,
                      "strictly_longest_correct": strictly_longest_correct, "strictly_longest_rate": strict_rate})
    if len(all_ids) != len(set(all_ids)):
        errors.append("Powtarzające się ID między wariantami 001–005")
    return errors, stats, heuristic_warnings(rows)


def main():
    errors, stats, warnings = audit()
    for item in stats:
        print(f"Variant {item['variant']:03}: A/B/C={item['letters']['A']}/{item['letters']['B']}/{item['letters']['C']}; max_run={item['longest_run']}; modules={len(item['modules'])}")
    print(f"Explanation heuristic warnings: {len(warnings)}")
    for qid, reason in warnings:
        print(f"  WARN {qid}: {reason}")
    if errors:
        print("FAIL: mock exam validation")
        for error in errors:
            print("  " + error)
        return 1
    print("PASS: five variants and keys match the current bank; letter distribution and run limits pass.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
