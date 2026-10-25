# Etap 4x2 — redakcja podręcznikowa lekcji ADR-B-13

- Data: 25.10.2026.
- Punkt wyjścia: `main` po PR #307, commit `f9d62ff78cb27e57b0b8b83ad2b8efdfe283d7d7`.
- Zakres: wyłącznie kurs podstawowy ADR.

## Co zredagowano

B-13 połączono w jedną lekcję obejmującą dane dokumentu przewozowego, dokumenty dostępne w kabinie, instrukcje pisemne, wymagania dotyczące języka i dostępności, dokumenty dodatkowe oraz odcinek drogowy po transporcie morskim. Włączono przykłady brakującej nazwy przewozowej, instrukcji niezrozumiałych dla członka załogi i kontroli dokumentacji po odcinku morskim.

Usunięto z tekstu kursanta nagłówki etapowe, daty, etykiety szkicu/wersji roboczej i powtarzające się noty redakcyjne. Materiały instruktorskie przeniesiono do `podstawowy/instruktor/ADR-B-13.md`.

## Zachowanie treści i referencji

Zachowano odwołania do pytań dotyczących standardowego wzoru instrukcji pisemnych, brakujących danych dokumentu, warunków transportu kombinowanego oraz pytań 0577–0579, 0586–0590 i 0598–0601. Nie zmieniano banku ani kluczy odpowiedzi.

## Preflight Quality Gate

- Bank: 609 pytań; duplikaty ID: 0.
- Poprawna odpowiedź jest jedyną najdłuższą: 86/609 = 14.12% (limit 18%).
- Najkrótsze explanation: 300 znaków; poniżej 200 znaków: 0.
- Status: 609 `needs_review`, 0 `verified`.
- Referencje w B-13: 47 unikalnych ID; brakujące 0; inne działy 0.

## Ograniczenia

Redakcja nie jest niezależną recenzją polskiego tekstu ADR. Wszystkie pytania zachowują `needs_review`; nie rozpoczęto pracy nad cysternami ani inną specjalizacją.
