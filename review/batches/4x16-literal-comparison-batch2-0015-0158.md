# Etap 4x16 — partia 2: porównanie literalne kolejnych 48 pytań

- Data: 25.10.2026.
- Punkt wyjścia: świeży `main`, commit `1ff1339b4842bce5d7aa98d4ddef7ee77a19f076`.
- Zakres: 48 kolejnych otwartych pozycji z obszarów wyposażenia, dokumentów, odpowiedzialności, tuneli, ochrony i klasyfikacji.
- Bank: 609 pytań; bez zmian w pytaniach i kluczach; wszystkie pozostają `needs_review`, 0 `verified`.

## Źródła

- [Dz.U. 2025 poz. 642 — ADR 2025](https://dziennikustaw.gov.pl/DU/2025/642).
- [Polski tekst ADR 2025, tom I — kopia MI](https://www.gov.pl/attachment/8856b22a-bfd8-4567-8386-b9709bba8da7).
- [Polski tekst ADR 2025, tom II — kopia MI](https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8).
- [Sprostowanie Dz.U. 2025 poz. 1575](https://eli.gov.pl/api/acts/DU/2025/1575/text.pdf).

Porównano poprawną odpowiedź i explanation z przywołanym punktem w pełnym tekście ADR 2025. W miejscach z progami liczbowymi sprawdzono wartości tabelaryczne; dla kodów tunelowych sprawdzono regułę wyboru kodu całego ładunku. MI zaznacza, że jego kopie są pomocnicze, a źródłem prawa pozostaje Dziennik Ustaw. Wynik oznacza zgodność tekstową w sprawdzonym zakresie, nie formalne zatwierdzenie prawne.

## Wynik

- Porównano: **48** pytań.
- Zgodne w zakresie sprawdzonego punktu: **48**.
- Potwierdzone sprzeczności: **0**.
- Przypadki bez możliwości porównania: **0**.
- Poprawki banku/kluczy/explanation: **0**.
- Statusy zmienione na `verified`: **0**.
- Licznik nierozstrzygniętych porównań: **551 → 503**.
- Wszystkie pytania nadal wymagają niezależnej oceny specjalisty.

## Rejestr pytanie → podstawa → wynik

| ID | Podstawa ADR | Wynik | Ustalenie |
|---|---|---|---|
| ADR-B-0015 | ADR 2025, 8.1.4.5 | Zgodne w zakresie sprawdzonego punktu | 8.1.4.5 wymaga, aby gaśnice były łatwo dostępne i chronione przed warunkami, które mogłyby utrudnić bezpieczne użycie. |
| ADR-B-0019 | ADR 2025, 1.4.2.2.6; 5.4.3.2 | Zgodne w zakresie sprawdzonego punktu | 1.4.2.2.6 wskazuje przewoźnika jako podmiot, który dostarcza załodze instrukcje pisemne. |
| ADR-B-0021 | ADR 2025, 1.4.2.1.1 (a) | Zgodne w zakresie sprawdzonego punktu | 1.4.2.1.1(a) nakłada na nadawcę obowiązek sprawdzenia klasyfikacji i dopuszczenia towaru do przewozu. |
| ADR-B-0022 | ADR 2025, 8.1.4.1 | Zgodne w zakresie sprawdzonego punktu | 8.1.4.1: dla DMC powyżej 7,5 t tabela wymaga łącznie 12 kg proszku lub równoważnej pojemności środka gaśniczego; minimum dwóch gaśnic. |
| ADR-B-0023 | ADR 2025, 8.1.5.2 | Zgodne w zakresie sprawdzonego punktu | 8.1.5.2 wymaga klina dla każdego pojazdu, dobranego do DMC i średnicy kół. |
| ADR-B-0024 | ADR 2025, 8.1.5.2 | Zgodne w zakresie sprawdzonego punktu | 8.1.5.2 wymienia rękawice ochronne jako osobiste wyposażenie każdego członka załogi. |
| ADR-B-0025 | ADR 2025, 7.5.2 | Zgodne w zakresie sprawdzonego punktu | 7.5.2 wymaga oceny zgodności wspólnego załadunku według przepisów i tabeli, a nie według kolorów opakowań. |
| ADR-B-0031 | ADR 2025, 1.9.5.2.2; 8.6 | Zgodne w zakresie sprawdzonego punktu | 8.6.2 określa kategorię A jako tunel bez dodatkowej tabliczki kategorii B–E; kod ograniczeń sprawdza się według 8.6.3. |
| ADR-B-0047 | ADR 2025, 8.3.6 | Zgodne w zakresie sprawdzonego punktu | 8.3.6 wymaga wyłączenia silnika podczas załadunku/rozładunku, jeżeli nie jest potrzebny do obsługi urządzeń. |
| ADR-B-0048 | ADR 2025, 8.3.3 | Zgodne w zakresie sprawdzonego punktu | 8.3.3 wprost zabrania kierowcy i pomocnikowi otwierania sztuk przesyłek z towarami niebezpiecznymi. |
| ADR-B-0055 | ADR 2025, 1.4.2.1.1 | Zgodne w zakresie sprawdzonego punktu | 1.4.2.1.1(b) przypisuje nadawcy przekazanie przewoźnikowi czytelnych informacji i wymaganych dokumentów. |
| ADR-B-0056 | ADR 2025, 8.1.5.2 | Zgodne w zakresie sprawdzonego punktu | 8.1.5.2 wymaga klina pod koło; znaki ostrzegawcze i pasy do mocowania nie pełnią tej samej funkcji. |
| ADR-B-0057 | ADR 2025, 8.1.5.2 | Zgodne w zakresie sprawdzonego punktu | 8.1.5.2 wymaga kamizelki ostrzegawczej dla każdego członka załogi. |
| ADR-B-0062 | ADR 2025, 1.1.4.2 | Zgodne w zakresie sprawdzonego punktu | 1.1.4.2 przewiduje ograniczone uznanie wymagań transportu morskiego na drodze; nie jest to automatyczne zwolnienie z oznakowania. |
| ADR-B-0064 | ADR 2025, 8.6.3.2–8.6.3.3 | Zgodne w zakresie sprawdzonego punktu | 8.6.3.2: przy różnych kodach tunelowych stosuje się kod odpowiadający największym ograniczeniom. |
| ADR-B-0071 | ADR 2025, 8.1.4.1 | Zgodne w zakresie sprawdzonego punktu | 8.1.4.1: dla DMC do 3,5 t tabela wymaga łącznie co najmniej 4 kg proszku lub równoważnej pojemności. |
| ADR-B-0072 | ADR 2025, 8.1.4.1 | Zgodne w zakresie sprawdzonego punktu | 8.1.4.1: dla DMC powyżej 3,5 t do 7,5 t tabela wymaga łącznie co najmniej 8 kg proszku lub równoważnej pojemności. |
| ADR-B-0074 | ADR 2025, 8.1.4.4; 8.1.4.5 | Zgodne w zakresie sprawdzonego punktu | 8.1.4.4–8.1.4.5 wymagają aktualnych kontroli i łatwego dostępu; nienaruszona plomba nie zastępuje ważnego przeglądu. |
| ADR-B-0075 | ADR 2025, 8.1.5.2 | Zgodne w zakresie sprawdzonego punktu | 8.1.5.2 wymaga jednej kamizelki dla każdego członka załogi, więc dwie osoby potrzebują dwóch kamizelek. |
| ADR-B-0076 | ADR 2025, 8.1.5.2 | Zgodne w zakresie sprawdzonego punktu | 8.1.5.2 wymienia ochronę oczu, np. okulary ochronne; okulary przeciwsłoneczne nie są automatycznym zamiennikiem. |
| ADR-B-0077 | ADR 2025, 8.1.5.3 | Zgodne w zakresie sprawdzonego punktu | 8.1.5.3 wymaga maski ucieczkowej dla każdego członka załogi przy nalepkach 2.3 lub 6.1. |
| ADR-B-0078 | ADR 2025, 7.5.7.2 | Zgodne w zakresie sprawdzonego punktu | 7.5.7.2 dotyczy zabezpieczenia ładunku i zapobiega uszkodzeniu opakowań przez nieodpowiednie piętrzenie. |
| ADR-B-0082 | ADR 2025, 7.5.4; 7.5.11 CV28; tabela A kol. (18) | Zgodne w zakresie sprawdzonego punktu | 7.5.4 i przepis CV28 w tabeli A określają, kiedy niektóre towary trzeba oddzielić od żywności, pasz i innych towarów konsumpcyjnych. |
| ADR-B-0085 | ADR 2025, 8.6.3.3 | Zgodne w zakresie sprawdzonego punktu | 8.6.3.3 wyłącza z ograniczeń tunelowych towary przewożone na podstawie 1.1.3, z wyjątkiem sytuacji wymagającej oznakowania według 3.4.13 z zastrzeżeniem 3.4.14. |
| ADR-B-0086 | ADR 2025, 8.6.3.2–8.6.3.3 | Zgodne w zakresie sprawdzonego punktu | 8.6.3.2 nakazuje zastosować do całego ładunku kod powodujący największe ograniczenia. |
| ADR-B-0087 | ADR 2025, 8.1.2.1(d); 1.10.1.4 | Zgodne w zakresie sprawdzonego punktu | 8.1.2.1(d) wymaga dokumentu ze zdjęciem umożliwiającego identyfikację każdego członka załogi w przypadkach określonych w 1.10.1.4. |
| ADR-B-0090 | ADR 2025, 5.4.3.1; 8.1.2.3 | Zgodne w zakresie sprawdzonego punktu | 8.1.2.3 wymaga przechowywania instrukcji pisemnych w łatwo dostępnym miejscu. |
| ADR-B-0091 | ADR 2025, 1.1.3.1 (a) | Zgodne w zakresie sprawdzonego punktu | 1.1.3.1(a) dotyczy określonych przewozów osób prywatnych na własny użytek, nie stanowi ogólnego zwolnienia dla towarów kupionych przez firmę do odsprzedaży. |
| ADR-B-0105 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | 5.4.3.4 każe załodze postępować według instrukcji pisemnych; ratownikom potrzebne są dostępne informacje o zdarzeniu i ładunku. |
| ADR-B-0109 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | 5.4.3.4 przewiduje dostęp do informacji o przewożonym towarze, które pomagają ratownikom ocenić zagrożenie. |
| ADR-B-0116 | ADR 2025, 1.4.2.2.1(c); 1.4.2.2.3–1.4.2.2.4 | Zgodne w zakresie sprawdzonego punktu | 1.4.2.2 wymaga, by przewoźnik sprawdził, czy towar i przesyłki mogą być przewożone bez naruszenia ADR; uszkodzenie z wyciekiem trzeba wyjaśnić przed przewozem. |
| ADR-B-0121 | ADR 2025, 1.10.2.2 | Zgodne w zakresie sprawdzonego punktu | 1.10.2.2 dotyczy szkolenia z ochrony: pracownicy mają rozpoznawać zagrożenia i wiedzieć, jak zgłosić incydent. |
| ADR-B-0122 | ADR 2025, 1.10.3.2.1 | Zgodne w zakresie sprawdzonego punktu | 1.10.3.2.1 wymaga planu ochrony dla przewozu towarów dużego ryzyka, jeśli przepis ma zastosowanie. |
| ADR-B-0126 | ADR 2025, 2.2.1.1.5 | Zgodne w zakresie sprawdzonego punktu | 2.2.1.1.5 definiuje podklasę 1.1 jako materiały i przedmioty stwarzające zagrożenie wybuchem masowym. |
| ADR-B-0129 | ADR 2025, 2.1.3.5.5 | Zgodne w zakresie sprawdzonego punktu | 2.1.3.5.5 pozwala klasyfikować odpady o słabo określonym składzie na podstawie wiedzy nadawcy i dostępnych danych; nie daje automatycznego prawa do grupy III. |
| ADR-B-0142 | ADR 2025, 1.1.4.2.1 | Zgodne w zakresie sprawdzonego punktu | 1.1.4.2.1 ma zastosowanie tylko przy spełnieniu warunków uznania wymagań IMDG na odcinku drogowym; dokument i oznakowanie trzeba sprawdzić dla konkretnego łańcucha. |
| ADR-B-0145 | ADR 2025, 8.1.2.2(a); Umowa wielostronna M364, pkt 1 (warunkowy wyjątek dla naczepy do 31.12.2026) | Zgodne w zakresie sprawdzonego punktu | 8.1.2.2(a) wymaga świadectwa dopuszczenia w kabinie, gdy ADR wymaga jego sporządzenia. Wyjątek M364 wymaga odrębnej kontroli aktualnych warunków umowy. |
| ADR-B-0146 | ADR 2025, 8.1.2.2(b); 8.2.1 | Zgodne w zakresie sprawdzonego punktu | 8.1.2.2(b) wymaga przewożenia w kabinie zaświadczenia o przeszkoleniu kierowcy, gdy jest wymagane. |
| ADR-B-0147 | ADR 2025, 1.2.1, definicja transport unit | Zgodne w zakresie sprawdzonego punktu | 1.2.1 definiuje jednostkę transportową tak, że zestaw ciągnik+naczepa jest traktowany jako jedna jednostka. |
| ADR-B-0150 | ADR 2025, 2.2.1.1.5 | Zgodne w zakresie sprawdzonego punktu | 2.2.1.1.5 rozróżnia podklasę 1.1 (wybuch masowy) od 1.4 (ograniczone zagrożenie wybuchem). |
| ADR-B-0151 | ADR 2025, 5.2.2.2.2, wzór nr 2.3; 2.2.2 | Zgodne w zakresie sprawdzonego punktu | Wzór nalepki 2.3 w 5.2.2.2.2 oznacza gaz trujący; 2.2.2 opisuje klasyfikację gazów. |
| ADR-B-0152 | ADR 2025, 2.2.3; 8.3.5 | Zgodne w zakresie sprawdzonego punktu | 8.3.5 ogranicza palenie podczas manipulowania towarami niebezpiecznymi i w ich pobliżu; gaśnica nie znosi tego zakazu. |
| ADR-B-0153 | ADR 2025, 2.2.41.1.1; 2.2.43.1.1 | Zgodne w zakresie sprawdzonego punktu | 2.2.41 opisuje klasę 4.1, a 2.2.43.1.1 klasę 4.3 jako materiały reagujące z wodą z wydzielaniem gazów palnych. |
| ADR-B-0154 | ADR 2025, 2.2.42.1.1 | Zgodne w zakresie sprawdzonego punktu | 2.2.42 opisuje materiały klasy 4.2 podatne na samozapalenie lub samonagrzewanie. |
| ADR-B-0155 | ADR 2025, 2.2.43.1.1; 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | 2.2.43.1.1 ostrzega, że kontakt klasy 4.3 z wodą może wydzielać palny gaz; dolanie wody może zwiększyć zagrożenie. |
| ADR-B-0156 | ADR 2025, 2.2.51.1.1 | Zgodne w zakresie sprawdzonego punktu | 2.2.51.1.1 dotyczy materiałów utleniających, które mogą nasilać spalanie. |
| ADR-B-0157 | ADR 2025, 2.2.51; 2.2.52 | Zgodne w zakresie sprawdzonego punktu | 2.2.51 i 2.2.52 rozdzielają materiały utleniające od nadtlenków organicznych; to odrębne klasy. |
| ADR-B-0158 | ADR 2025, 5.2.2.2.2 wzór nr 6.1; 2.2.61.1.1 | Zgodne w zakresie sprawdzonego punktu | Wzór nalepki 6.1 w 5.2.2.2.2 oraz 2.2.61 oznaczają materiały trujące, a nie zakaźne 6.2 lub żrące 8. |

## Kontrole liczbowe i warunków

- Gaśnice według 8.1.4.1: do 3,5 t — 4 kg łącznie; powyżej 3,5 t do 7,5 t — 8 kg; powyżej 7,5 t — 12 kg, z dodatkowymi warunkami dotyczącymi liczby i pojemności poszczególnych gaśnic.
- Przy przewozie korzystającym z 1.1.3.6 pozostaje wymóg minimum jednej gaśnicy 2 kg lub równoważnej skuteczności (8.1.4.2).
- Wyposażenie z 8.1.5.2 obejmuje klin dla każdego pojazdu, dwa stojące znaki ostrzegawcze, płyn do płukania oczu (z wyjątkami) oraz wyposażenie osobiste każdego członka załogi.
- Przy mieszanych kodach tunelowych stosuje się kod odpowiadający największym ograniczeniom (8.6.3.2); towary objęte 1.1.3 są wyłączane z obliczenia zgodnie z 8.6.3.3, z określonym wyjątkiem dla oznakowania LQ.
- Świadectwo dopuszczenia i zaświadczenie ADR przewozi się w kabinie, gdy są wymagane (8.1.2.2). Dla ADR-B-0145 trzeba dodatkowo sprawdzić warunki czasowe umowy M364, bo nie jest ona częścią tekstu ADR samego w sobie.

## Następny krok

Kolejna partia obejmie kolejne 40–50 pozycji otwartych. Nie stwierdzono potwierdzonego błędu wymagającego zmiany banku w tej partii. Nie oznaczono żadnego pytania jako `verified`.
