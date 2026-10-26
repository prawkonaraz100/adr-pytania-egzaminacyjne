# Etap 4x32 — kontrola dystraktorów i materiałów kursanta, B-01–04

## Punkt wyjścia
- Świeży `main`: `9b576146553b5e40d5777a7dea0a237dc8ba1d08`.
- Etap 4x31: potwierdzony jako ukończony — PR #471 scalony, Quality Gate PASS w run #40291844463. Pełny skan wykrył i poprawił ADR-B-0540 (38 słów w zdaniu); ADR-B-0319 był fałszywym alarmem z powodu skrótu „m.in.”.
- Bank przed zmianą: 609 pytań.

## Ręczny przegląd partii
Sprawdzono dystraktory w B-01–04. Przeredagowano 5 pytań, bez zmiany ID, działu ani poprawnej litery:

| ID | Problem potwierdzony | Zmiana |
|---|---|---|
| ADR-B-0313 | Odpowiedzi o „tanim towarze” i zgodzie pasażerów były łatwe do odrzucenia bez znajomości warunków wyłączenia. | Zastąpiono je wiarygodnymi, lecz błędnymi przekonaniami o wystarczalności opakowania detalicznego i dokumentu ADR. Poprawna litera A. |
| ADR-B-0266 | „Zawsze ciecz łatwopalna” i „nigdy nie wymaga oddzielenia” opierały się na absolutach i myliły podstawowe klasy. | Zastąpiono je częstszymi błędami: utożsamieniem klasy 5.1 z łatwopalnością oraz uznaniem, że zamknięte opakowanie zwalnia z zasad wspólnego załadunku. Poprawna litera B. |
| ADR-B-0317 | Kolor opakowania jako podstawa klasyfikacji był odpowiedzią zbyt oczywiście nieprawidłową. | Zmieniono na błąd polegający na poleganiu wyłącznie na nalepce bez sprawdzenia kryteriów aktywności. Poprawna litera B. |
| ADR-B-0318 | „Dowolny numer UN wybrany przez kierowcę” oraz automatyczne zwolnienie każdego odpadu były skrajnie absurdalne. | Zmieniono na pominięcie dostępnych danych technicznych oraz próbę rozpoczęcia przewozu bez klasyfikacji. Poprawna litera B. |
| ADR-B-0353 | „Słuchawki ochronne” nie miały związku z ryzykiem iskrzenia lampy. | Zmieniono na dwa wiarygodne, ale błędne założenia: krótki czas użycia i niskie napięcie rzekomo eliminujące ryzyko iskry. Poprawna litera B. |

Wyjaśnienia dla wszystkich pięciu pytań sprawdzono i przepisano tak, aby wyjaśniały sens poprawnej odpowiedzi oraz dlaczego nowe dystraktory są błędne. Każde zawiera podstawę ADR i przekracza 200 znaków. Statusy w banku nie zostały zmienione.

## Kontrola lekcji B-01–04
W każdej z czterech lekcji istnieją sekcje „Co musisz zapamiętać”, „Scenariusze praktyczne” i odwołania do pytań. W tej partii nie wykryto braku wymagającego dopisania nowej treści. To kontrola struktury i referencji, nie niezależna aprobata prawna treści.

## Metryki po zmianach
| Dział | Pytań | Poprawna = jedyna najdłuższa | Udział | Najkrótsze explanation | Rozkład klucza A/B/C |
|---|---:|---:|---:|---:|---|
| ADR-B-01 | 45 | 6 | 13.33% | 300 znaków | 17/17/11 |
| ADR-B-02 | 56 | 7 | 12.50% | 300 znaków | 21/19/16 |
| ADR-B-03 | 49 | 7 | 14.29% | 300 znaków | 16/21/12 |
| ADR-B-04 | 46 | 6 | 13.04% | 301 znaków | 15/18/13 |
- Bank: 609 pytań; brak zmian ID i poprawnych liter; statusy pozostają bez zmian.
- Zakres wskaźnika po zmianach: wszystkie działy B-01–04 poniżej 18%.
- Zmiany merytoryczne ograniczono do jakości dystraktorów i ich objaśnień; nie zmieniano podstaw prawnych ani nie oznaczano pytań jako `verified`.

## Następny krok
Kontynuować ten sam przegląd w partii B-05–08, a następnie B-09–13. Po partiach wykonać pełny Quality Gate CI i wpisać wyniki do Issue #10.
