# Etap 4x223 — drugi przegląd explanation (partia 64)

Data: 31.10.2026. Zakres: wyłącznie kurs podstawowy ADR. Bazowy `main`: `d4cd384d397aa67a4fcad93a39990af25e8abbdf`. Gałąź: `stage4x223-explanations-batch64`. Bank: 651 pytań ADR-B-0001–0651.

## Korekta metody doboru i duplikaty

Przed wyborem pytań odtworzono listę ID z raportów i wpisów Issue #10 etapów 4x156–4x222. Dla etapu 4x156 uwzględniono pełny zakres z raportu: ADR-B-0611–0638 oraz ADR-B-0646–0647. Dla 4x177, którego raportu nie znaleziono w katalogu raportów, zakres 10 zmian odtworzono z dodanych rekordów w diffie PR #646: ADR-B-0095, ADR-B-0221, ADR-B-0226, ADR-B-0262, ADR-B-0265, ADR-B-0391, ADR-B-0439, ADR-B-0517, ADR-B-0595, ADR-B-0596. Po deduplikacji zebrano **624 unikalnych ID już przejrzanych**.

Weryfikacja wykazała, że **wszystkie 10 ID z 4x221 było powtórzeniem**:
- ADR-B-0226 i ADR-B-0265 — wcześniejsza partia 4x177 (PR #646);
- ADR-B-0326, ADR-B-0344, ADR-B-0377 i ADR-B-0594 — raport 4x157;
- ADR-B-0359 — raport 4x159;
- ADR-B-0461, ADR-B-0587 i ADR-B-0602 — raport 4x158.

Te powtórzenia pozostają w rejestrze jako już przejrzane, ale nie są liczone jako nowe ID w 4x221. W następnych partiach należy porównywać pełne identyfikatory z listą poniżej, a nie tylko z ostatnim raportem.

## Wybór 4x223

Po wykluczeniu wszystkich powyższych ID pozostało 27 rekordów. Wybrano 10 z najsłabszymi wyjaśnieniami spośród nieprzejrzanych: krótkie, mało praktyczne lub wymagające dopowiedzenia. Przepisano wyłącznie pole `explanation`:

| ID | Długość nowego explanation |
|---|---:|
| ADR-B-0536 | 407 |
| ADR-B-0006 | 368 |
| ADR-B-0179 | 372 |
| ADR-B-0373 | 416 |
| ADR-B-0450 | 388 |
| ADR-B-0571 | 337 |
| ADR-B-0366 | 424 |
| ADR-B-0605 | 355 |
| ADR-B-0608 | 427 |
| ADR-B-0089 | 395 |

Każde wyjaśnienie ma 4 zdania i 337–427 znaków: praktyczny sens poprawnej odpowiedzi, wyjaśnienie mylących wariantów oraz krótka podstawa ADR. Nie zmieniono stem, opcji A/B/C, poprawnych liter, źródeł ani `verification_status`. Nie stwierdzono potwierdzonego błędu pytania lub klucza wymagającego korekty. Wszystkie rekordy nadal `needs_review`; nic nie oznaczono jako `verified`.

## Synchronizacja zależności

- Warianty i klucze egzaminów próbnych 001–005: `source_bank_head` ustawiono na aktualny blob `questions.jsonl`: `9951bd4edeaa844cfa5f07964ce4636d5637c35f`.
- Klucze 001 i 002: zaktualizowano explanation dla tych pozycji, które występują w arkuszach (ADR-B-0571, ADR-B-0605, ADR-B-0373).
- Snapshoty `review/sequential` oraz `review/legal-clauses`: odświeżono zakresy 001–030, 061–090, 151–180, 363–380, 447–454, 534–538, 570–579 i 598–609. Snapshoty odpowiadają nowemu bankowi; oznaczenie odczytu explanation pozostaje true.
- Pakiet recenzyjny: odświeżono SHA banku w manifeście PAKIET-0628, kolejkach 4x40/4x44, manifeście próbki 4x135, instrukcji, rejestrze bieżącym oraz dokumentacji przekazania i README.

## Lista ID już przejrzanych w raportach 4x156–4x222

Łącznie **624 unikalnych ID** (numery czterocyfrowe odpowiadają końcówkom ADR-B-XXXX):

0001, 0002, 0003, 0004, 0005, 0007, 0008, 0009, 0010, 0011, 0012, 0013, 0014, 0015, 0016, 0017, 0018, 0019, 0020, 0021, 0022, 0023, 0024, 0025, 0026, 0027, 0028, 0029, 0030, 0031, 0032, 0033, 0034, 0035, 0036, 0037, 0038, 0039, 0040, 0041, 0042, 0043, 0044, 0045, 0046, 0047, 0048, 0049, 0050, 0051, 0052, 0053, 0054, 0055, 0056, 0057, 0058, 0059, 0060, 0062, 0063, 0064, 0065, 0066, 0067, 0068, 0069, 0070, 0071, 0072, 0073, 0074, 0075, 0076, 0077, 0078, 0079, 0080, 0081, 0082, 0083, 0084, 0085, 0086, 0087, 0088, 0090, 0091, 0092, 0093, 0094, 0095, 0096, 0097, 0098, 0099, 0100, 0101, 0102, 0103, 0104, 0105, 0106, 0107, 0108, 0109, 0110, 0111, 0112, 0113, 0114, 0115, 0116, 0117, 0118, 0119, 0120, 0121, 0122, 0123, 0124, 0125, 0126, 0127, 0128, 0129, 0130, 0131, 0132, 0133, 0134, 0135, 0136, 0138, 0139, 0140, 0141, 0142, 0143, 0144, 0146, 0147, 0148, 0149, 0150, 0151, 0152, 0153, 0154, 0155, 0156, 0157, 0158, 0159, 0160, 0161, 0162, 0163, 0164, 0165, 0166, 0167, 0168, 0169, 0170, 0171, 0172, 0173, 0174, 0175, 0176, 0177, 0178, 0180, 0181, 0182, 0183, 0184, 0185, 0186, 0187, 0188, 0189, 0190, 0191, 0192, 0193, 0194, 0195, 0196, 0197, 0199, 0200, 0201, 0202, 0203, 0204, 0205, 0206, 0207, 0208, 0210, 0211, 0212, 0213, 0214, 0215, 0216, 0217, 0218, 0219, 0220, 0221, 0222, 0223, 0224, 0225, 0226, 0227, 0228, 0229, 0230, 0231, 0232, 0233, 0234, 0235, 0236, 0237, 0238, 0239, 0240, 0241, 0242, 0243, 0244, 0245, 0246, 0247, 0248, 0249, 0250, 0251, 0252, 0253, 0254, 0255, 0256, 0257, 0258, 0259, 0260, 0261, 0262, 0263, 0264, 0265, 0267, 0268, 0269, 0270, 0271, 0272, 0273, 0274, 0275, 0276, 0277, 0279, 0280, 0281, 0282, 0283, 0284, 0285, 0286, 0287, 0288, 0289, 0290, 0291, 0292, 0293, 0294, 0295, 0296, 0297, 0298, 0299, 0300, 0301, 0302, 0303, 0304, 0305, 0307, 0308, 0309, 0310, 0311, 0312, 0313, 0314, 0315, 0316, 0318, 0319, 0320, 0321, 0322, 0323, 0325, 0326, 0327, 0328, 0329, 0330, 0331, 0333, 0334, 0335, 0336, 0337, 0338, 0339, 0340, 0341, 0342, 0343, 0344, 0345, 0346, 0347, 0348, 0349, 0350, 0351, 0352, 0353, 0354, 0355, 0356, 0357, 0358, 0359, 0360, 0361, 0362, 0363, 0364, 0365, 0367, 0368, 0369, 0370, 0371, 0372, 0374, 0375, 0376, 0377, 0378, 0379, 0380, 0381, 0382, 0383, 0384, 0385, 0387, 0389, 0391, 0392, 0393, 0394, 0395, 0396, 0397, 0398, 0399, 0400, 0401, 0402, 0403, 0404, 0406, 0407, 0408, 0409, 0410, 0411, 0412, 0413, 0414, 0415, 0416, 0417, 0418, 0419, 0420, 0421, 0422, 0423, 0424, 0425, 0426, 0427, 0428, 0429, 0430, 0431, 0432, 0433, 0434, 0435, 0436, 0437, 0438, 0439, 0440, 0441, 0442, 0443, 0444, 0445, 0446, 0447, 0448, 0449, 0451, 0452, 0453, 0454, 0455, 0456, 0457, 0458, 0459, 0460, 0461, 0462, 0463, 0464, 0465, 0466, 0467, 0468, 0469, 0470, 0471, 0472, 0473, 0474, 0475, 0476, 0477, 0478, 0479, 0480, 0481, 0482, 0483, 0484, 0485, 0486, 0487, 0488, 0489, 0490, 0491, 0492, 0493, 0494, 0495, 0496, 0497, 0498, 0499, 0500, 0501, 0502, 0503, 0504, 0505, 0506, 0507, 0508, 0509, 0510, 0511, 0512, 0513, 0514, 0515, 0516, 0517, 0518, 0519, 0520, 0521, 0522, 0523, 0524, 0526, 0527, 0528, 0529, 0530, 0531, 0532, 0533, 0534, 0535, 0537, 0538, 0539, 0540, 0541, 0542, 0543, 0544, 0545, 0546, 0548, 0549, 0550, 0551, 0552, 0553, 0554, 0555, 0556, 0557, 0558, 0559, 0560, 0561, 0562, 0563, 0564, 0565, 0566, 0567, 0568, 0569, 0570, 0572, 0573, 0574, 0575, 0576, 0577, 0578, 0579, 0580, 0581, 0582, 0583, 0584, 0585, 0586, 0587, 0588, 0589, 0590, 0591, 0592, 0593, 0594, 0595, 0596, 0597, 0598, 0599, 0600, 0601, 0602, 0603, 0604, 0606, 0607, 0609, 0610, 0611, 0612, 0613, 0614, 0615, 0616, 0617, 0618, 0619, 0620, 0621, 0622, 0623, 0624, 0625, 0626, 0627, 0628, 0629, 0630, 0631, 0632, 0633, 0634, 0635, 0636, 0637, 0638, 0639, 0640, 0641, 0642, 0643, 0644, 0645, 0646, 0647, 0648, 0649, 0650, 0651

## Pozostałe ID do drugiego przeglądu

Po 4x223 pozostaje 17 ID: ADR-B-0061, ADR-B-0137, ADR-B-0145, ADR-B-0198, ADR-B-0209, ADR-B-0266, ADR-B-0278, ADR-B-0306, ADR-B-0317, ADR-B-0324, ADR-B-0332, ADR-B-0386, ADR-B-0388, ADR-B-0390, ADR-B-0405, ADR-B-0525, ADR-B-0547. Należy je rozdzielić między kolejne partie, bez powtarzania.

## Kontrole i ograniczenia

Nie wykonano lokalnego checkoutu ani lokalnego test runnera w tym środowisku; nie deklaruję lokalnego PASS. Pełny Quality Gate i testy integralności muszą przejść w CI na dokładnym SHA PR. Niezależna recenzja prawna ADR przez specjalistę pozostaje odrębnym, otwartym procesem.
