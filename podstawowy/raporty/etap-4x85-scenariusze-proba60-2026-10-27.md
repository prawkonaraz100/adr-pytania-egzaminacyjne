# Etap 4x85 — odbiór scenariuszy i próbka 60 explanation

- Data: 27.10.2026.
- Punkt wejściowy: `main` `a758c40add0db7c3e872c2a4e27dad36cb8bbce4`.
- Zakres: wyłącznie kurs podstawowy ADR.
- Gałąź: `stage4x85-scenariusze-proba60-20261027`.
- Stan po korektach banku: blob SHA `7a02299fd6fc0cd944abd8b84840b535d371fad9`.

## 1. Przegląd scenariuszy praktycznych — 39/39

Przejrzano wszystkie 39 scenariuszy pod kątem realności sytuacji, kolejności działań kierowcy, wyjaśnienia typowych błędów, podstaw ADR i powiązań z bankiem.

| Kontrola | Wynik |
|---|---:|
| Scenariusze | 39/39 |
| Działy z dokładnie 3 scenariuszami | 13/13 |
| Kroki postępowania na scenariusz | minimum 4, maksimum 4 |
| Brakujące/nieistniejące `question_ids` | 0 |
| `question_ids` z innego modułu | 0 |
| Brak `learner_takeaway`, `common_mistakes`, podstawy ADR lub kryteriów oceny | 0 |
| Potwierdzone sprzeczności prawne wymagające zmiany scenariusza | 0 |
| Nowe pytania dopisane | 0 |

Każdy scenariusz ma sytuację, cztery kroki, typowe błędy, podstawę prawną, kryteria oceny, podsumowanie dla kursanta, pytanie do omówienia i co najmniej jedno powiązane pytanie z właściwego działu. Nie zmieniono scenariuszy, ponieważ nie znaleziono potwierdzonej usterki merytorycznej. To kontrola redakcyjna i strukturalna, nie niezależna certyfikacja zgodności z prawem.

## 2. Losowa próbka 60 explanation

- Seed: `2026102785`; generator: LCG + Fisher–Yates.
- Do puli wykluczeń przyjęto zachowawczo wszystkie ID wymienione w dostępnych raportach 4x45, 4x46, 4x48, 4x49, 4x50, 4x51 i 4x84. To wykluczyło 380 unikalnych ID; pozostałe 229 stanowiły pulę losowania.
- Próba: 60 ID. Każde explanation przeczytano w kontekście pytania, trzech odpowiedzi, poprawnej litery i podstawy ADR.

```
ADR-B-0158, ADR-B-0117, ADR-B-0394, ADR-B-0437, ADR-B-0077, ADR-B-0140, ADR-B-0091, ADR-B-0210, ADR-B-0086, ADR-B-0163, ADR-B-0126, ADR-B-0590, ADR-B-0564, ADR-B-0547, ADR-B-0357, ADR-B-0138, ADR-B-0463, ADR-B-0354, ADR-B-0540, ADR-B-0018, ADR-B-0415, ADR-B-0205, ADR-B-0185, ADR-B-0218, ADR-B-0389, ADR-B-0145, ADR-B-0270, ADR-B-0143, ADR-B-0039, ADR-B-0073, ADR-B-0038, ADR-B-0037, ADR-B-0443, ADR-B-0424, ADR-B-0465, ADR-B-0390, ADR-B-0096, ADR-B-0315, ADR-B-0553, ADR-B-0503, ADR-B-0132, ADR-B-0244, ADR-B-0458, ADR-B-0285, ADR-B-0295, ADR-B-0150, ADR-B-0584, ADR-B-0409, ADR-B-0414, ADR-B-0013, ADR-B-0442, ADR-B-0585, ADR-B-0243, ADR-B-0418, ADR-B-0069, ADR-B-0087, ADR-B-0334, ADR-B-0048, ADR-B-0027, ADR-B-0255
```

### Wynik ręcznej kontroli

| Wynik | Liczba |
|---|---:|
| Explanation poprawione | 4 |
| Pytania z poprawionymi dystraktorami | 3 |
| Opcje błędne urealnione | 4 |
| Explanation bez zmiany | 56 |
| ID z próbki bez zmiany explanation, ale z kontrolą treści | 56 |
| Nowe pytania | 0 |

**Potwierdzone problemy dydaktyczne i poprawki:**

1. **ADR-B-0117** — „przypadkowa osoba postronna” i „odbiorca po zakończeniu rozładunku” były zbyt oczywistymi błędnymi odpowiedziami. Zastąpiono je częstą pomyłką co do tego, czy przewoźnik ma sam zgadywać dane, oraz mylnym przesunięciem obowiązku nadawcy na odbiorcę po dostawie. Klucz A bez zmian; ADR 1.4.2.1.1.
2. **ADR-B-0210** — „przenosić przesyłki do wyjścia ewakuacyjnego” było mało wiarygodne. Zastąpiono to błędem polegającym na pozostawaniu przy pojeździe zamiast ewakuacji. Klucz B bez zmian; ADR 5.4.3.4.
3. **ADR-B-0415** — wariant o umieszczeniu reklamy na bramie był oczywiście absurdalny. Zastąpiono go mylnym założeniem, że zamknięcie kontenera wystarczy bez zabezpieczenia dostępu do miejsca składowania. Klucz A bez zmian; ADR 1.10.1.3.
4. **ADR-B-0503** — usunięto powtórzone zdanie o tym, czego cyfra 3 nie oznacza, i zachowano proste rozróżnienie palności od żrącego działania i palności materiałów stałych. Klucz C bez zmian; ADR 5.3.2.3.1.

Wszystkie cztery zmienione explanation mają 2–5 zdań i co najmniej 300 znaków. Żadna zmiana nie modyfikuje poprawnej litery ani statusu prawnego.

## 3. Egzaminy próbne 001–005

Po zmianie banku zaktualizowano `source_bank_head` w każdym arkuszu i kluczu. Zmiany opcji/wyjaśnień w arkuszach odzwierciedlono w tych wariantach, w których występowały odpowiednie ID.

| Wariant | Pytania | Unikalne ID | Działy | Klucz A/B/C | Najdłuższa seria | Niezgodności po synchronizacji |
|---|---:|---:|---:|---|---:|---:|
| 001 | 30 | 30 | 13 | 10/10/10 | 3 | 0 |
| 002 | 30 | 30 | 13 | 10/10/10 | 3 | 0 |
| 003 | 30 | 30 | 13 | 10/10/10 | 3 | 0 |
| 004 | 30 | 30 | 13 | 10/10/10 | 3 | 0 |
| 005 | 30 | 30 | 13 | 10/10/10 | 3 | 0 |

Warianty zawierają łącznie 150 różnych ID — brak powtórzeń między arkuszami. W trakcie kontroli wykryto dodatkowo rozbieżność explanation w kluczu wariantu 001 dla **ADR-B-0489** (klucz nadal odwoływał się do starej litery A zamiast aktualnej litery A w banku?); klucz zsynchronizowano z aktualnym explanation banku. Nie zmieniono poprawnej treści odpowiedzi ani klucza. Końcowa kontrola synchronizacji potwierdziła zgodność wszystkich 150 wpisów z bankiem.

## 4. Quality Gate — preflight danych

- Bank: 609 pytań, 609 unikalnych ID, 0 duplikatów.
- Statusy: 609 `needs_review`, 0 `verified`.
- Explanation: minimum 300 znaków; poniżej 200: 0; jednozdaniowe w kontroli technicznej: 0; zdania ponad 35 słów: 0.
- „Poprawna = jedyna najdłuższa”: 73/609 = 11.99%.
- Wszystkie działy poniżej progu 18%.

| Dział | Pytań | Poprawna jedyna najdłuższa | Wskaźnik |
|---|---:|---:|---:|
| ADR-B-01 | 45 | 6 | 13.33% |
| ADR-B-02 | 56 | 8 | 14.29% |
| ADR-B-03 | 49 | 7 | 14.29% |
| ADR-B-04 | 46 | 6 | 13.04% |
| ADR-B-05 | 43 | 5 | 11.63% |
| ADR-B-06 | 45 | 5 | 11.11% |
| ADR-B-07 | 48 | 6 | 12.50% |
| ADR-B-08 | 42 | 5 | 11.90% |
| ADR-B-09 | 46 | 4 | 8.70% |
| ADR-B-10 | 55 | 4 | 7.27% |
| ADR-B-11 | 43 | 6 | 13.95% |
| ADR-B-12 | 44 | 6 | 13.64% |
| ADR-B-13 | 47 | 5 | 10.64% |
| **Łącznie** | **609** | **73** | **11.99%** |

### Kontrole przed CI

- Scenariusze: wszystkie referencje istnieją i należą do właściwego działu.
- Egzaminy: wszystkie source hashes wskazują aktualny blob banku; 5/5 arkuszy i kluczy ma 30 unikalnych pytań, wszystkie 13 działów i rozkład A/B/C 10/10/10.
- Snapshoty sekwencyjne oraz przeglądu A/B/C zaktualizowano dla ADR-B-0117, ADR-B-0210, ADR-B-0415 i ADR-B-0503.
- Manifest, indeks i instrukcje pakietu recenzyjnego wskazują aktualny blob banku.

Nie wykonano testów jednostkowych lokalnie: dostępna integracja daje możliwość pracy przez GitHub, ale nie udostępnia lokalnego checkoutu do uruchomienia Pythona. Pełny CI Quality Gate na PR jest obowiązkowym warunkiem scalenia. Preflight danych opisany wyżej został wykonany na pobranych plikach repozytorium; nie zastępuje CI ani recenzji specjalisty ADR.

## 5. Sprawa do specjalisty

**ADR-B-0145 — M364 i data 31.12.2026.** Explanation wskazuje warunkowy wyjątek dla naczepy i termin końcowy 31.12.2026. Nie zmieniano odpowiedzi ani nie dopisywano aktualizacji bez potwierdzonego urzędowego tekstu. Specjalista powinien sprawdzić status M364 oraz ewentualne przedłużenie/nowe porozumienie przed użyciem materiału po tej dacie.

## Status końcowy

Bank nadal zawiera 609 pytań `needs_review`, 0 `verified`, bez formalnych zatwierdzeń. Wszystkie poprawki mają charakter redakcyjny i dydaktyczny. Nie rozpoczęto kursu cystern ani innego kursu.
