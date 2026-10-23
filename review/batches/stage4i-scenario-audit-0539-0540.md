# Etap 4i — inwentaryzacja scenariuszy 13 działów, partia 0539–0540

Przesiew wykonano na świeżym main 538 pytań / ostatni ADR-B-0538 / 0 verified. Wszelkie liczby poniżej są **heurystyczną listą kandydatów do ręcznego potwierdzenia**, nie pełnym semantycznym zatwierdzeniem.

Reguła: pytanie zawiera słowo oznaczające miejsce, uczestnika lub fazę przewozu oraz drugie słowo opisujące decyzję, problem lub zdarzenie. Reguła może pominąć synonimy i uznać ogólnik za scenariusz.

| Dział | Ogółem | Kandydaci sytuacyjni | ID kandydatów |
|---|---:|---:|---|
| ADR-B-01 | 35 | 7 | ADR-B-0124, ADR-B-0148, ADR-B-0301, ADR-B-0526, ADR-B-0527, ADR-B-0529, ADR-B-0535 |
| ADR-B-02 | 54 | 7 | ADR-B-0152, ADR-B-0154, ADR-B-0162, ADR-B-0218, ADR-B-0265, ADR-B-0302, ADR-B-0502 |
| ADR-B-03 | 49 | 8 | ADR-B-0009, ADR-B-0101, ADR-B-0163, ADR-B-0177, ADR-B-0178, ADR-B-0179, ADR-B-0241, ADR-B-0327 |
| ADR-B-04 | 44 | 13 | ADR-B-0180, ADR-B-0181, ADR-B-0280, ADR-B-0296, ADR-B-0352, ADR-B-0353, ADR-B-0354, ADR-B-0356, ADR-B-0357, ADR-B-0472, ADR-B-0473, ADR-B-0474, ADR-B-0476 |
| ADR-B-05 | 40 | 9 | ADR-B-0106, ADR-B-0110, ADR-B-0167, ADR-B-0185, ADR-B-0219, ADR-B-0220, ADR-B-0229, ADR-B-0232, ADR-B-0494 |
| ADR-B-06 | 32 | 4 | ADR-B-0115, ADR-B-0193, ADR-B-0506, ADR-B-0507 |
| ADR-B-07 | 43 | 27 | ADR-B-0020, ADR-B-0055, ADR-B-0116, ADR-B-0117, ADR-B-0118, ADR-B-0135, ADR-B-0195, ADR-B-0196, ADR-B-0245, ADR-B-0246, ADR-B-0285, ADR-B-0363, ADR-B-0366, ADR-B-0369, ADR-B-0370, ADR-B-0371, ADR-B-0372, ADR-B-0374, ADR-B-0375, ADR-B-0376, ADR-B-0377, ADR-B-0378, ADR-B-0478, ADR-B-0479, ADR-B-0480, ADR-B-0482, ADR-B-0517 |
| ADR-B-08 | 36 | 8 | ADR-B-0056, ADR-B-0074, ADR-B-0176, ADR-B-0198, ADR-B-0253, ADR-B-0283, ADR-B-0422, ADR-B-0423 |
| ADR-B-09 | 39 | 9 | ADR-B-0080, ADR-B-0138, ADR-B-0201, ADR-B-0202, ADR-B-0235, ADR-B-0238, ADR-B-0239, ADR-B-0291, ADR-B-0424 |
| ADR-B-10 | 55 | 8 | ADR-B-0204, ADR-B-0206, ADR-B-0278, ADR-B-0391, ADR-B-0395, ADR-B-0398, ADR-B-0446, ADR-B-0453 |
| ADR-B-11 | 33 | 1 | ADR-B-0435 |
| ADR-B-12 | 43 | 7 | ADR-B-0034, ADR-B-0120, ADR-B-0211, ADR-B-0300, ADR-B-0414, ADR-B-0416, ADR-B-0519 |
| ADR-B-13 | 35 | 16 | ADR-B-0087, ADR-B-0145, ADR-B-0146, ADR-B-0216, ADR-B-0228, ADR-B-0234, ADR-B-0250, ADR-B-0306, ADR-B-0508, ADR-B-0523, ADR-B-0524, ADR-B-0530, ADR-B-0532, ADR-B-0533, ADR-B-0536, ADR-B-0538 |

## Nowe scenariusze
- ADR-B-0539: kierowca ma dwa kody tunelowe D/E oraz B/D dla przewozu w sztukach i ma podjąć decyzję na trasie z tunelem kategorii C — ADR 8.6.3.2 i 8.6.4.
- ADR-B-0540: kierowca prowadzi oznakowaną jednostkę LQ (3.4.13/3.4.14) i na rozjeździe przed tunelem E ma wybrać dopuszczalną trasę — ADR 8.6.4.

Dwa pytania, sześć osobnych ocen A/B/C, źródła i exact snapshots w `review/legal-clauses/539-540.json` oraz `review/sequential/539-540.json`. Stan `needs_review`; literalne sprawdzenie urzędowego polskiego ADR 2025 (Dz.U. 642 i sprostowanie poz. 1575) oraz recenzja specjalisty pozostają otwarte.

Po tej partii ADR-B-11 będzie zawierał 35 pytań. Pozostałe moduły wciąż wymagają ręcznej oceny głębi przypadków; nie twierdzimy, że sam heurystyczny licznik gwarantuje minimum trzech wartościowych scenariuszy na dział. Żadnych innych kursów.
