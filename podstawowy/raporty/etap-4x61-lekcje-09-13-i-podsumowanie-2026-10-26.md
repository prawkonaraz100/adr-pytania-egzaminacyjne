# Etap 4x61 — lekcje B-09–13 i końcowy przegląd nawigacji

Data: 26.10.2026. Punkt wyjścia: świeży main po PR #513, commit `2109709fde323a79f157bc6536ba34bf6f119f74`.

## Przegląd oczami początkującego
Zweryfikowano obecność w każdej lekcji: jasnego celu, wyjaśnionych pojęć i skrótów, praktycznych przykładów pracy kierowcy, „Co musisz zapamiętać”, sekcji „Sprawdź się” z ID pytań działu oraz odsyłaczy do trzech scenariuszy. Wszystkie pięć lekcji miało komplet elementów, ale lista scenariuszy była rozproszona i umieszczona po podstawach prawnych, z dala od praktyki.

| Lekcja | Zmiana układu | Kontrola odsyłaczy |
|---|---|---|
| B-09 | Przeniesiono blok trzech scenariuszy przed podsumowanie. | Zachowano ID i odsyłacze; dodano odsyłacz do głównego scenariusza przy „Sprawdź się”. |
| B-10 | Jak wyżej. | Jak wyżej. |
| B-11 | Jak wyżej. | Jak wyżej. |
| B-12 | Jak wyżej. | Jak wyżej. |
| B-13 | Jak wyżej. | Jak wyżej. |

Zmiana dotyczy **nawigacji i czytelności**, bez usuwania opisów, przykładów, ID pytań lub odniesień do ADR. Nie modyfikowano treści i legal basis scenariuszy ani ich połączeń z bankiem.

## Wynik próby wyjaśnień
Nowa próbka 60 różnych ID ze wskazaniem seed `2026102661` została wykonana i opisana w `etap-4x61-proba60-i-lekcje-01-04-2026-10-26.md` (PR #512). Wszystkie 60 wyjaśnień miało 3–5 zdań i 300–429 znaków; nie stwierdzono potwierdzonej potrzeby korekty. Brak fałszywych „poprawek dla samego commita”.

## Stan ogólny
Po etapie 4x61 wszystkie 13 lekcji zachowują cel, proste wyjaśnienia, podsumowanie, pytania kontrolne i odsyłacze do trzech scenariuszy umieszczone bliżej części praktycznej. Odpowiedzi w banku nie zmieniały się, dlatego dotychczasowe warianty egzaminów próbnych i pakiet recenzyjny nie wymagają synchronizacji rekordów. Bank: 609 pytań `needs_review`, 0 `verified`. Ostatni potwierdzony pomiar długości: 72/609 = 11,82%, minimum explanation 300 znaków.

## Co dalej
Potencjalnie wartościowy następny krok: **kontrola, czy instruktor jest w stanie przeprowadzić trzy scenariusze w czasie rzeczywistych zajęć bez potrzeby interpretowania surowego JSON-a**. Dla każdego z 39 scenariuszy należy sprawdzić kolejność działań, jednoznaczność kryterium zaliczenia, bezpieczeństwo i odsyłacze do pytań. To przegląd dydaktyczny, nie zatwierdzenie prawa. Nie dodawano pytań bez potwierdzonej luki programu i nie przechodzono do innych kursów.