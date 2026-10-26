# Etap 4x24 — raport końcowy: wydobywanie dosłownych fragmentów MI ADR 2025 PL

- Data: 2026-10-26.
- Świeży `main` przed raportem: `e60ca5ab1f85a9271b0306d4f17f0ed58210d115`.
- Zakres: 172 rekordy z otwartej puli po etapie 4x23; dodatkowo ADR-B-0567–0569 sprawdzone osobno pod kątem Kodeksu cywilnego.
- Źródła pomocnicze MI ADR 2025 PL:
  - Tom I: https://www.gov.pl/attachment/f833868b-a0c1-4ff2-ab4c-90b913bb0a10
  - Tom II: https://www.gov.pl/attachment/b4638c72-30e3-4bff-afd1-1b9ba4100e70
- Źródło KC: tekst jednolity Dz.U. 2025 poz. 1071: https://api.sejm.gov.pl/eli/acts/DU/2025/1071/text.pdf
- Nie pobierano ponownie PDF Dz.U. ADR i nie wpisywano stron Dz.U.

## Wynik łączny

| Wskaźnik | Wynik |
|---|---:|
| Rekordy z puli 172 przejrzane w pięciu partiach | 172 |
| Dosłowne fragmenty MI wydobyte | 44 |
| Rekordy nadal bez dosłownego fragmentu MI | 128 |
| Pytania KC sprawdzone osobno | 3 |
| Potwierdzone sprzeczności | 0 |
| Pytania/klucze zmienione | 0 |
| Rekordy oznaczone `verified` | 0 |
| Status porównania z Dz.U. ADR | `pending` |

### Partie

| Partia | Rekordy | Dosłowne cytaty MI | Nadal bez cytatu |
|---|---:|---:|---:|
| 1 — stage4x24-mi-literal-batch1-0013-0608-2026-10-26.json | 37 | 15 | 22 |
| 2 — stage4x24-mi-literal-batch2-0202-0410-2026-10-26.json | 40 | 17 | 23 |
| 3 — stage4x24-mi-literal-batch3-0427-0501-2026-10-26.json | 40 | 7 | 33 |
| 4 — stage4x24-mi-literal-batch4-0502-0578-2026-10-26.json | 40 | 1 | 39 |
| 5 — stage4x24-mi-literal-batch5-0579-0599-2026-10-26.json | 15 | 7 | 8 |
| **Razem** | **172** | **44** | **128** |

## Kodeks cywilny — ADR-B-0567–0569

Źródło: tekst jednolity Kodeksu cywilnego, Dz.U. 2025 poz. 1071.

- **Art. 415:** „Kto z winy swej wyrządził drugiemu szkodę, obowiązany jest do jej naprawienia.”
- **Art. 471:** „Dłużnik obowiązany jest do naprawienia szkody wynikłej z niewykonania lub nienależytego wykonania zobowiązania, chyba że niewykonanie lub nienależyte wykonanie jest następstwem okoliczności, za które dłużnik odpowiedzialności nie ponosi.”

Wniosek: pytania 0567–0569 zachowują ostrożne brzmienie. Nie twierdzą, że każda kolizja lub każde naruszenie ADR automatycznie przesądza o odpowiedzialności osobistej i pełnym odszkodowaniu. Nie potwierdzono sprzeczności; pytań nie zmieniano. Status nadal `needs_review`.

## Dlaczego 125 rekordów nadal jest otwartych

W dostępnej warstwie tekstowej MI nie udało się wydobyć dokładnego brzmienia właściwego podpunktu albo właściwego wiersza tabeli dla 125 rekordów. Dotyczy to m.in. kodów tunelowych, tabeli wspólnego załadunku, kodów BK/VC, świadectw i kategorii pojazdów, progów ilościowych, dokumentacji przewozowej, oznakowania oraz baterii sodowo-jonowych. W tych przypadkach nie zastępowano cytatu parafrazą, nie wyciągano wniosku o zgodności i nie zmieniano odpowiedzi na podstawie pamięci.

**Lista 128 ID bez dosłownego fragmentu:**
- ADR-B-0026
- ADR-B-0032
- ADR-B-0033
- ADR-B-0036
- ADR-B-0058
- ADR-B-0060
- ADR-B-0079
- ADR-B-0083
- ADR-B-0084
- ADR-B-0127
- ADR-B-0131
- ADR-B-0137
- ADR-B-0138
- ADR-B-0139
- ADR-B-0141
- ADR-B-0144
- ADR-B-0148
- ADR-B-0162
- ADR-B-0172
- ADR-B-0173
- ADR-B-0181
- ADR-B-0202
- ADR-B-0239
- ADR-B-0262
- ADR-B-0292
- ADR-B-0301
- ADR-B-0310
- ADR-B-0312
- ADR-B-0315
- ADR-B-0317
- ADR-B-0319
- ADR-B-0324
- ADR-B-0345
- ADR-B-0346
- ADR-B-0347
- ADR-B-0348
- ADR-B-0349
- ADR-B-0350
- ADR-B-0351
- ADR-B-0353
- ADR-B-0374
- ADR-B-0379
- ADR-B-0402
- ADR-B-0403
- ADR-B-0409
- ADR-B-0410
- ADR-B-0427
- ADR-B-0428
- ADR-B-0433
- ADR-B-0437
- ADR-B-0438
- ADR-B-0439
- ADR-B-0440
- ADR-B-0441
- ADR-B-0442
- ADR-B-0443
- ADR-B-0447
- ADR-B-0448
- ADR-B-0449
- ADR-B-0450
- ADR-B-0451
- ADR-B-0452
- ADR-B-0453
- ADR-B-0454
- ADR-B-0473
- ADR-B-0474
- ADR-B-0475
- ADR-B-0476
- ADR-B-0482
- ADR-B-0487
- ADR-B-0488
- ADR-B-0489
- ADR-B-0490
- ADR-B-0495
- ADR-B-0496
- ADR-B-0497
- ADR-B-0498
- ADR-B-0500
- ADR-B-0501
- ADR-B-0502
- ADR-B-0508
- ADR-B-0510
- ADR-B-0512
- ADR-B-0520
- ADR-B-0521
- ADR-B-0522
- ADR-B-0523
- ADR-B-0524
- ADR-B-0525
- ADR-B-0528
- ADR-B-0529
- ADR-B-0530
- ADR-B-0531
- ADR-B-0532
- ADR-B-0533
- ADR-B-0534
- ADR-B-0536
- ADR-B-0537
- ADR-B-0538
- ADR-B-0541
- ADR-B-0542
- ADR-B-0546
- ADR-B-0547
- ADR-B-0549
- ADR-B-0550
- ADR-B-0554
- ADR-B-0555
- ADR-B-0556
- ADR-B-0557
- ADR-B-0558
- ADR-B-0559
- ADR-B-0560
- ADR-B-0561
- ADR-B-0562
- ADR-B-0564
- ADR-B-0565
- ADR-B-0577
- ADR-B-0578
- ADR-B-0579
- ADR-B-0580
- ADR-B-0581
- ADR-B-0588
- ADR-B-0591
- ADR-B-0595
- ADR-B-0598
- ADR-B-0599
- ADR-B-0600
- ADR-B-0602
## Ograniczenia i status formalny

- Fragment MI jest pomocniczym źródłem polskojęzycznym, ale nie zastępuje porównania z ogłoszonym tekstem prawnym.
- Nie przypisano stron Dz.U.; status porównania z Dz.U. ADR 2025 (Dz.U. poz. 642 i sprostowanie poz. 1575) pozostaje `pending`.
- Brak cytatu nie jest dowodem sprzeczności ani zgodności.
- Nie zmieniono pytań, odpowiedzi, explanation ani kluczy.
- Wszystkie rekordy pozostają `needs_review`; formalną weryfikację przeprowadza specjalista.

## Rejestry

- Partia 1: `review/batches/stage4x24-mi-literal-batch1-0013-0608-2026-10-26.json`
- Partia 2: `review/batches/stage4x24-mi-literal-batch2-0202-0410-2026-10-26.json`
- Partia 3: `review/batches/stage4x24-mi-literal-batch3-0427-0501-2026-10-26.json`
- Partia 4: `review/batches/stage4x24-mi-literal-batch4-0502-0578-2026-10-26.json`
- Partia 5: `review/batches/stage4x24-mi-literal-batch5-0579-0599-2026-10-26.json`
- Indeks łączny: `review/batches/stage4x24-mi-literal-index-2026-10-26.json`
