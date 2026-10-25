# Etap 4u — 13 lekcji: Sprawdź się i scenariusze

- Stan wyjściowy: 569 pytań kursu podstawowego po PR #281.
- W każdej z 13 lekcji na końcu dodano sekcję „Sprawdź się” z 8 ID istniejących pytań z danego działu i odnośnikiem do scenariusza `SC-ADR-B-XX`.
- Najpierw uwzględniono pytania przypisane scenariuszowi, potem dobrano inne pytania tego samego działu.
- Test `tests/test_stage4u_lesson_selfcheck.py` kontroluje kompletność 13 lekcji, 5–10 unikalnych istniejących ID w sekcji, zgodność działu i scenariusza oraz wariant 003 wraz z kluczem i brakiem powtórek z 001/002.
- Bez zmian banku, kluczy i statusów `needs_review`.

| Dział | Lista ID | Scenariusz |
|---|---|---|
| ADR-B-01 | ADR-B-0002, ADR-B-0259, ADR-B-0526, ADR-B-0001, ADR-B-0003, ADR-B-0040, ADR-B-0041, ADR-B-0091 | SC-ADR-B-01 |
| ADR-B-02 | ADR-B-0006, ADR-B-0510, ADR-B-0004, ADR-B-0005, ADR-B-0042, ADR-B-0043, ADR-B-0044, ADR-B-0094 | SC-ADR-B-02 |
| ADR-B-03 | ADR-B-0009, ADR-B-0514, ADR-B-0007, ADR-B-0008, ADR-B-0045, ADR-B-0046, ADR-B-0100, ADR-B-0101 | SC-ADR-B-03 |
| ADR-B-04 | ADR-B-0010, ADR-B-0012, ADR-B-0011, ADR-B-0047, ADR-B-0048, ADR-B-0102, ADR-B-0103, ADR-B-0130 | SC-ADR-B-04 |
| ADR-B-05 | ADR-B-0013, ADR-B-0015, ADR-B-0169, ADR-B-0014, ADR-B-0049, ADR-B-0050, ADR-B-0104, ADR-B-0105 | SC-ADR-B-05 |
| ADR-B-06 | ADR-B-0507, ADR-B-0546, ADR-B-0562, ADR-B-0016, ADR-B-0017, ADR-B-0018, ADR-B-0051, ADR-B-0052 | SC-ADR-B-06 |
| ADR-B-07 | ADR-B-0020, ADR-B-0517, ADR-B-0567, ADR-B-0568, ADR-B-0569, ADR-B-0019, ADR-B-0021, ADR-B-0054 | SC-ADR-B-07 |
| ADR-B-08 | ADR-B-0418, ADR-B-0551, ADR-B-0566, ADR-B-0022, ADR-B-0023, ADR-B-0024, ADR-B-0056, ADR-B-0057 | SC-ADR-B-08 |
| ADR-B-09 | ADR-B-0518, ADR-B-0554, ADR-B-0558, ADR-B-0025, ADR-B-0026, ADR-B-0027, ADR-B-0058, ADR-B-0059 | SC-ADR-B-09 |
| ADR-B-10 | ADR-B-0396, ADR-B-0511, ADR-B-0028, ADR-B-0029, ADR-B-0030, ADR-B-0061, ADR-B-0062, ADR-B-0119 | SC-ADR-B-10 |
| ADR-B-11 | ADR-B-0487, ADR-B-0539, ADR-B-0540, ADR-B-0031, ADR-B-0032, ADR-B-0033, ADR-B-0063, ADR-B-0064 | SC-ADR-B-11 |
| ADR-B-12 | ADR-B-0304, ADR-B-0305, ADR-B-0519, ADR-B-0034, ADR-B-0035, ADR-B-0036, ADR-B-0066, ADR-B-0067 | SC-ADR-B-12 |
| ADR-B-13 | ADR-B-0508, ADR-B-0525, ADR-B-0530, ADR-B-0037, ADR-B-0038, ADR-B-0039, ADR-B-0068, ADR-B-0069 | SC-ADR-B-13 |
