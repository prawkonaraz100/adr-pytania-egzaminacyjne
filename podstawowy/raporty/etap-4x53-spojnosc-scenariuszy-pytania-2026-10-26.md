# Etap 4x53 — spójność scenariuszy praktycznych z pytaniami

- Data: 26.10.2026.
- Świeży `main` przed pracą: `f994d0686aa8054cabcd2890506005defbcbdab0` (po PR #502).
- Zakres: tylko kurs podstawowy ADR; bank pytań bez zmian.

## Potwierdzone niedopasowania i poprawki

| Scenariusz | Problem | Poprawka |
|---|---|---|
| `SC-ADR-B-04-02` | Ćwiczenie o e-papierosie i pracującym silniku zawierało dodatkowo pytanie o nadzór postoju. | Zostawiono dwa pytania bezpośrednio związane z paleniem i silnikiem: ADR-B-0010, ADR-B-0012. |
| `SC-ADR-B-06-02` | Pytanie ADR-B-0170 dotyczyło litery X i użycia wody, a nie odczytania rozbieżności na tablicy. | Zastąpiono je ADR-B-0217 o znaczeniu cyfry 8 w numerze zagrożenia. |
| `SC-ADR-B-08-02` | Pytanie ADR-B-0596 dotyczyło kamizelki, nie gaśnicy. | Zastąpiono je ADR-B-0283 o brakującym oznaczeniu terminu kontroli gaśnicy. Podstawa zawężona do ADR 8.1.4.1–8.1.4.5. |
| `SC-ADR-B-09-02` | Pytania ADR-B-0026 i ADR-B-0518 dotyczyły mocowania, nie pozostałości i oględzin podłogi. | Zestaw: ADR-B-0554 oraz ADR-B-0080, dotyczące pozostałości i oczyszczenia przed kolejnym załadunkiem. |
| `SC-ADR-B-09-03` | Pytanie ADR-B-0558 dotyczyło zamknięć przy przewozie luzem; nie pasowało do mocowania skrzyń i ciężkiego elementu. | Zastąpiono je ADR-B-0235 o niezamocowanych skrzyniach; usunięto niepasującą podstawę ADR 7.3.1.1 i dopasowano podsumowanie oraz typowe błędy. |
| `SC-ADR-B-12-02` | Pytanie ADR-B-0519 dotyczyło dokumentu tożsamości członka załogi, nie zmiany postoju. | Zastąpiono je ADR-B-0407 o skuteczności zabezpieczeń przed kradzieżą w czasie przewozu. |
| `SC-ADR-B-12-03` | Tytuł mówił o odbiorcy, ale pytania dotyczyły weryfikacji przewoźnika; podstawa i instrukcje były zbyt szerokie. | Zmieniono nazwę, sytuację, kroki i typowe błędy, użyto ADR-B-0120, ADR-B-0211 i ADR-B-0414 oraz zawężono podstawę do ADR 1.10.1.2. |

## Walidacja po zmianach

- Scenariusze: 39; liczba scenariuszy w każdym dziale: ADR-B-01=3, ADR-B-02=3, ADR-B-03=3, ADR-B-04=3, ADR-B-05=3, ADR-B-06=3, ADR-B-07=3, ADR-B-08=3, ADR-B-09=3, ADR-B-10=3, ADR-B-11=3, ADR-B-12=3, ADR-B-13=3.
- Nieistniejące question IDs: 0.
- question IDs przypisane do innego działu: 0.
- Scenariusze bez 3 kroków, podstawy ADR, learner_takeaway albo common_mistakes: 0.
- Wszystkie 39 scenariuszy zachowują co najmniej 4 kroki; zmiany dotyczą wyłącznie dopasowania scenariusza do pytań i jego właściwej podstawy.

## Bank i wskaźniki

- Bank: 609 pytań, 609 `needs_review`, 0 `verified`, duplikaty ID: 0.
- Explanation poniżej 200 znaków: 0; minimum: 300 znaków.
- „Poprawna = jedyna najdłuższa”: 72/609 = 11.82%; maksimum działu: 14.29%.
- Pytania, odpowiedzi, explanation i ich statusy nie zostały zmienione; egzaminy próbne 001–005 i klucze nie wymagają regeneracji.
- Niczego nie oznaczono jako `verified`; nie stwierdzono potwierdzonej luki programu wymagającej nowego pytania.

## Testy

Brak lokalnego checkoutu i niedostępny DNS dla `git clone` uniemożliwiają deklarowanie lokalnego uruchomienia testów. PR musi przejść pełny Quality Gate CI przed scaleniem.
