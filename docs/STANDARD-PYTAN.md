# Standard tworzenia pytań i Quality Gate

## Format danych

Jeden samodzielny rekord JSON na linię w podstawowy/questions.jsonl; kodowanie UTF-8. Formalny schemat: schema/question.schema.json.

Każdy rekord musi mieć:
- id: niezmienny unikalny identyfikator w formacie ADR-B-0001 itd.;
- module_id: ADR-B-01 do ADR-B-13, zgodnie z mapą programu;
- stem: autorskie pytanie w języku polskim;
- options: dokładnie trzy różne, niepuste odpowiedzi A, B, C;
- correct_option: A / B / C;
- explanation: krótki opis dlaczego ta odpowiedź jest poprawna, zrozumiały dla kierowcy;
- sources: co najmniej jeden dokument + dokładny punkt przepisu + adres;
- legal_basis_version: np. ADR-2025-PL;
- verification_status: draft, needs_review, verified, blocked;
- checked_at: data weryfikacji albo null przed weryfikacją;
- reviewer: identyfikator recenzenta albo null;
- image: ścieżka grafiki na własnej licencji albo null.

## Reguły redakcyjne

1. Jedno zagadnienie i jedna odpowiedź poprawna; trzy warianty to nie trzy niezależne prawdziwe stwierdzenia.
2. Pisanie dla kierowcy, bez urzędniczego żargonu. Unikać zaprzeczeń typu „która odpowiedź NIE jest NIEPRAWIDŁOWA”.
3. Nie polegać na „zawsze/nigdy” bez zweryfikowania wyjątków. Dodać warunki ilościowe, transportowe i właściwy rodzaj opakowania.
4. Wyjaśnienie mówi dlaczego, a nie tylko powtarza wybraną odpowiedź.
5. Ilustracje własne, czytelne i ze sprawdzonym znaczeniem znaku; alt w eksporcie produktu.
6. Dla pytań sytuacyjnych nie sugerować samodzielnych działań ratowniczych ponad przygotowanie kierowcy; kierować się instrukcjami i bezpieczeństwem.

## Statusy

| Status | Znaczenie | Może trafić do egzaminu próbnego? |
|---|---|---|
| draft | Nowo napisane; treść niezweryfikowana | Nie |
| needs_review | Przygotowane do sprawdzenia przez recenzenta | Nie |
| verified | Treść i źródło sprawdzone, zapisano datę i recenzenta | Tak, po przejściu Quality Gate |
| blocked | Sprzeczne źródła, niejednoznaczne lub problem prawny | Nie |

## Kontrola jakości

- Struktura JSONL i zgodność pól.
- Unikalne identyfikatory, moduły zgodne z programem.
- Dokładnie trzy opcje i poprawny klucz.
- Dowód weryfikacji prawnej każdego pytania ze statusem verified.
- Brak pustych, nieprecyzyjnych cytatów przepisów.
- Lektura przez drugą osobę/eksperta ADR; sam walidator nie wystarcza do oceny prawdziwości.
- Brak zduplikowanych pytań, praw i wariantów odpowiedzi.
- Odświeżanie po zmianie regulacji; ponowna recenzja zmian w pytaniach.

## Format egzaminu szkoleniowego

30 pytań / 60 minut / od 20 poprawnych. Losowanie powinno zachować dobrą reprezentację całego materiału i unikać duplikatów. **Rozkład tematów ustalony przez nas nie jest rozkładem urzędowego egzaminu.**

## Reguła publikacji

Nie emitować pytań nieweryfikowanych do użytkowników końcowych. Programistyczny Quality Gate to dopiero jedna z kontroli; merytoryczna aprobata eksperta jest niezależna.
