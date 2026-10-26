# Etap 4x23 — raport porównania MI dla 318 otwartych rekordów

- Data: 26.10.2026.
- Punkt wyjścia: `main` po PR #433, commit `3bc2c14eb59b54dd9eb6922f1dd7904d26ebdefb`.
- Podstawa porównania: `MI ADR 2025 PL (pomocniczy), strona Dz.U. do potwierdzenia przez specjalistę`.
- MI ADR 2025 tom I: https://www.gov.pl/attachment/8856b22a-bfd8-4567-8386-b9709bba8da7
- MI ADR 2025 tom II: https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8
- Nie ponawiano prób pobrania PDF Dz.U. Nie wpisano żadnej strony Dz.U.; paginacja MI nie została przeniesiona na Dz.U.

## Wynik końcowy tej rundy

| Wskaźnik | Wynik |
|---|---:|
| Otwarte rekordy na początku | 318 |
| Rekordy z polem `literal_comparison_result` w rejestrze uzupełniającym | 318 |
| Rekordy z dosłownym cytatem MI zapisanym w rejestrze | 146 |
| Wynik „zgodne w zakresie cytatu” | 122 |
| Częściowe / niewystarczające / poza zakresem MI | 24 |
| Rekordy, dla których dokładny fragment MI nie został wydobyty | 172 |
| Potwierdzone sprzeczności | 0 |
| Zmienione pytania lub klucze | 0 |
| Rekordy oznaczone `verified` | 0 |

**Ważne:** 318 wyników oznacza, że każdy otwarty rekord ma teraz jawny rezultat lub status braku fragmentu. Nie oznacza to, że wszystkie 318 porównań prawnych zostały domknięte: 172 nadal wymagają dosłownego fragmentu MI, a wszystkie wymagają końcowego potwierdzenia specjalisty względem Dz.U.

## Pierwsze 51 rekordów, które miały już cytat MI

- **42** zgodne w zakresie przytoczonego fragmentu.
- **2** częściowe: ADR-B-0027 i ADR-B-0140.
- **7** z cytatem niewystarczającym do potwierdzenia całego pytania: ADR-B-0065 oraz sześć rekordów wskazanych w rejestrze partii 0192–0609.
- Sprzeczności potwierdzone: **0**. Nie poprawiano kluczy ani treści pytań bez dowodu.

Rejestr wyników obejmuje pytanie, odpowiedzi A/B/C, klucz, explanation, punkt ADR, cytat i zakres wniosku. „Zgodne” oznacza wyłącznie zgodność w zakresie cytatu, a nie formalną weryfikację prawną.

## 267 rekordów bez cytatu na początku etapu

- **95** rekordów otrzymało cytat MI w partiach z tego etapu.
- **172** nadal nie mają wydobytego dokładnego fragmentu; dla każdego zapisano konkretny status/powód, bez zastępowania cytatu parafrazą.
- W priorytetowej partii sprawdzono 30 rekordów związanych z ADR 2.1.3.5.3–2.1.3.5.5, 5.4.2, 1.10.3.1.2, 5.2.1.8.1 i 5.3.6.2.
- Pytania ADR-B-0567–0569 opierają część wniosku na Kodeksie cywilnym. Rejestr jawnie wskazuje, że MI ADR nie rozstrzyga art. 415/471 KC; potrzebna jest osobna weryfikacja tego źródła.

## ID wymagające dalszego wydobycia dokładnego fragmentu

`ADR-B-0013, 0014, 0020, 0026, 0029, 0032, 0033, 0036, 0049, 0050, 0054, 0058, 0060, 0066, 0079, 0083, 0084, 0117, 0118, 0120, 0127, 0131, 0134, 0135, 0137, 0138, 0139, 0141, 0144, 0148, 0162, 0172, 0173, 0181, 0600, 0602, 0608`.

To 37 rekordów zidentyfikowanych po uzgodnieniu rejestrów. Pozostałe rekordy w grupie 172 mają powód braku fragmentu zapisany przy swoim ID w rejestrze.

## Rejestr i ograniczenie techniczne

- Rejestr uzupełniający: `review/legal-polish/stage4x23-reconciled-open-records-0001-0609.json`.
- W pierwotnym ledgerze `review/legal-polish/stage4w4-literal-verification-ledger-0001-0609.json` znajduje się 609 wpisów i 318 otwartych rekordów, ale bezpośrednia operacja aktualizacji tego pliku o rozmiarze ok. 1,36 MB została zablokowana przez warstwę bezpieczeństwa narzędzia. Aby nie nadpisać ani nie skrócić oryginału, wyniki zapisano w osobnym rejestrze uzgodnieniowym z pełnymi 318 wpisami. Każdy wpis zawiera wymagane pole `comparison_basis`, `literal_comparison_result), stan porównania z Dz.U. `pending` oraz `needs_review`.

## Następny krok
W dalszych partiach wydobywać brakujące fragmenty MI dla 172 rekordów, zaczynając od 37 ID powyżej i szczególnie pilnując progów, wyjątków oraz tabel. Nie zmieniać odpowiedzi bez potwierdzonej sprzeczności. Wszystkie rekordy pozostają `needs_review`; końcowe zatwierdzenie należy do specjalisty.
