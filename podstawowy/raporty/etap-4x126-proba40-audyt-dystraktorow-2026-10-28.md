# Etap 4x126 — audyt kolejnej próbki 40 pytań kursu podstawowego

Data: 28.10.2026. Świeży main: `fd0f5ea4a5cb8e2bedb6628c37141f1a1de4e93d`. Bank 609 pytań (`ADR-B-0001–0609`). Kontrola tylko kursu podstawowego.

## Dobór próby

Seed `41262026`, deterministyczny LCG + Fisher–Yates. Wykluczono 149 różnych ID z próbek i zmian zapisanych w manifestach 4x122–4x125; zostało 460 kandydatów. Wybrano 40 unikalnych ID. Próbka obejmuje 12 działów (brak B-06 w losowaniu). Nie deklarujemy braku nakładania ze wszystkimi dużo starszymi etapami, bo wykorzystano dokładnie wskazane manifesty.

## Kontrola wyjaśnień i odpowiedzi

Przeczytano pytanie, trzy odpowiedzi i wyjaśnienie każdego ID. Wszystkie 40 explanation ma 2–5 zdań i 200–500 znaków, zaczyna się od sensu odpowiedzi oraz wskazuje podstawę ADR na końcu. Brak potwierdzonej konieczności przepisania explanation w tej próbie: **0 zmian**. Nie podnoszono żadnego statusu weryfikacji.

Do kolejnej celowanej redakcji odnotowano poniższe słabości dystraktorów. Dziś nie zmieniano opcji bez równoczesnego audytu A/B/C oraz regeneracji migawki prawnej i wariantów egzaminu; raport nie nazywa ich prawnie potwierdzonymi błędami:
- **ADR-B-0405:** Dystraktor A dotyczący pieczątki jest za mało wiarygodny. Wymaga zastąpienia realistycznym błędem dotyczącym ochrony informacji, z aktualizacją A/B/C i snapshotów.
- **ADR-B-0297:** Dystraktory B/C łatwo odrzucić z powodu skrajnie niebezpiecznych czynności. Możliwa poprawa dydaktyczna bez zmiany właściwej procedury.
- **ADR-B-0276:** Dystraktory bardzo krótkie i łatwe; do oceny wariant z prawdopodobnym pomyleniem oznakowania środowiskowego z nalepką klasy.
- **ADR-B-0333:** Dystraktory B/C są mocno oczywiste; możliwa poprawa po kontroli odpowiednich reguł pierwszeństwa.

## Lista 40 sprawdzonych pytań

| ID | Dział | Explanation | Dystraktory |
|---|---|---|---|
| ADR-B-0447 | ADR-B-10 | 358 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0574 | ADR-B-11 | 322 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0060 | ADR-B-09 | 400 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0454 | ADR-B-10 | 398 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0049 | ADR-B-05 | 307 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0354 | ADR-B-04 | 363 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0401 | ADR-B-12 | 359 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0577 | ADR-B-13 | 329 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0292 | ADR-B-09 | 347 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0223 | ADR-B-05 | 349 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0078 | ADR-B-09 | 359 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0183 | ADR-B-05 | 320 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0587 | ADR-B-13 | 308 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0404 | ADR-B-12 | 316 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0140 | ADR-B-10 | 385 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0344 | ADR-B-03 | 302 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0276 | ADR-B-03 | 312 znaków; 1 zdania | Do celowanej poprawy |
| ADR-B-0130 | ADR-B-04 | 320 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0158 | ADR-B-02 | 350 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0077 | ADR-B-08 | 327 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0111 | ADR-B-05 | 318 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0478 | ADR-B-07 | 305 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0419 | ADR-B-08 | 362 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0313 | ADR-B-01 | 468 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0283 | ADR-B-08 | 395 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0216 | ADR-B-13 | 328 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0408 | ADR-B-12 | 329 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0195 | ADR-B-07 | 342 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0163 | ADR-B-03 | 317 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0318 | ADR-B-03 | 401 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0297 | ADR-B-04 | 327 znaków; 1 zdania | Do celowanej poprawy |
| ADR-B-0390 | ADR-B-10 | 432 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0065 | ADR-B-11 | 391 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0134 | ADR-B-07 | 376 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0377 | ADR-B-07 | 304 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0177 | ADR-B-03 | 370 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0538 | ADR-B-13 | 374 znaków; 1 zdania | Bez potwierdzonej słabości |
| ADR-B-0405 | ADR-B-12 | 438 znaków; 1 zdania | Do celowanej poprawy |
| ADR-B-0333 | ADR-B-03 | 326 znaków; 1 zdania | Do celowanej poprawy |
| ADR-B-0089 | ADR-B-13 | 426 znaków; 1 zdania | Bez potwierdzonej słabości |

## Spójność z kursem i Quality Gate

Wszystkie 40 ID istnieją w banku, a każdy należy do jednego z 13 działów, dla których są lekcje. Struktura lekcji zawiera definicje, omówienia, scenariusze, pytania i podstawy prawne; ten etap **nie stanowi literalnego zatwierdzenia** wszystkich norm ADR cytowanych w pytaniach. Ponieważ bank, klucze i przypisania nie zostały zmienione, nie wymagały regeneracji warianty egzaminu ani snapshoty.

- Bank: 609 unikalnych ID, wszystkie `needs_review`, 0 `verified`.
- Poprawna jest jedyną najdłuższą: **69/609 = 11,33%**; największy wskaźnik działowy **13,95%**.
- Wyjaśnienia: minimum 300 znaków w banku (wg kontroli 4x125); w próbce wszystkie spełniają zakres 200–500 i 2–5 zdań.
- Zmiany w banku: **0**. Dalsza poprawa dystraktorów wymaga odrębnej synchronizacji z audytami i egzaminami.

## Granice weryfikacji

Jest to odbiór redakcyjny i wykaz priorytetów, nie kontrola prawna każdego zapisu. Formalne porównanie z ADR 2025 (Dz.U. 2025 poz. 642 i sprostowaniem poz. 1575) i niezależna akceptacja specjalisty pozostają otwarte. Nie oznaczono niczego jako `verified`.
