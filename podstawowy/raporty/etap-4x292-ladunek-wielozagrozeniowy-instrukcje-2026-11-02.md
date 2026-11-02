# Etap 4x292 — instrukcje pisemne dla ładunku z wieloma zagrożeniami (ADR-B-0718)

Data: 02.11.2026  
Zakres: kurs podstawowy ADR  
Gałąź: `stage4x292-mixed-load-written-instructions`  
Punkt wyjścia: main `261ce00a28fd8e1e1ea2e84cb7a6af54dba27a69`  
Nowy identyfikator: `ADR-B-0718`

## Luka pokrycia
ADR-B-05-K15 (praktyczny scenariusz awarii/wypadku) miała dotąd 4 pytania. Nowe pytanie sprawdza zastosowanie uwagi 1 do instrukcji pisemnych: przy przewozie z wieloma zagrożeniami lub ładunkiem mieszanym nie wolno zignorować innych właściwych pozycji.

## Audyt A/B/C
- Klucz **A**: uwzględnić wszystkie właściwe pozycje zagrożeń i działać tylko bezpiecznie.
- B: błędnie wybiera wyłącznie pierwszy towar na liście.
- C: błędnie wybiera towar o największej masie.
- Długości odpowiedzi A/B/C: 118/106/105 znaków. Poprawna A jest najdłuższa, ale łączny wskaźnik banku pozostaje poniżej limitu.
- Explanation: 397 znaków, 4 zdania, język początkującego.
- Bank: 718 pytań, 718 `needs_review`, 0 `verified`; A/B/C=240/257/221, najdłuższa poprawna 77/718 = 10,72%; maksimum modułu 13,95%.

## Podstawa prawna
- ADR 2025, 5.4.3.4, uwaga 1: przy towarach z wieloma zagrożeniami i ładunkach mieszanych stosuje się każdą właściwą pozycję tabeli instrukcji pisemnych.
- ADR 2025, 8.2.2.3.8: indywidualne ćwiczenia praktyczne obejmują reakcję na wypadek/awarię.
- Tekst polski: https://eli.gov.pl/api/acts/DU/2025/642/text.pdf
- UNECE: https://unece.org/info/Transport/pub/395786

## Kontrola i status
Nowy blob `questions.jsonl`: `5eda2984ac8899b31bfc6b351b4cf1722ccdd07c`. Wymagana synchronizacja egzaminów 001–005, snapshotów sequential/legal, manifestów, indeksu i metryk przed CI. Pełne literalne porównanie polskiego ADR i niezależna recenzja specjalisty nadal otwarte; pytanie pozostaje `needs_review`.
