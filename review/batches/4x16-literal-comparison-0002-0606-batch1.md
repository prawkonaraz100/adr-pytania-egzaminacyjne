# Etap 4x16 — partia 1: porównanie literalne pytań wysokiego ryzyka

- Data: 25.10.2026.
- Punkt wyjścia: świeży `main`, commit `136e4fe0481563c118c8fd653db2c1c69b11df6a`.
- Zakres: 48 pytań dotyczących klasyfikacji, dokumentów, oznakowania i wyłączenia ilościowego ADR 1.1.3.6.
- Bank: 609 pytań, bez zmian w pytaniach i kluczach; wszystkie pozostają `needs_review`, 0 `verified`.

## Źródła i metoda

1. [Dz.U. 2025 poz. 642 — publikacja ADR 2025](https://dziennikustaw.gov.pl/DU/2025/642).
2. [Pełny polski tekst ADR 2025, tom I, kopia udostępniona przez Ministerstwo Infrastruktury](https://www.gov.pl/attachment/8856b22a-bfd8-4567-8386-b9709bba8da7).
3. [Sprostowanie Dz.U. 2025 poz. 1575](https://eli.gov.pl/api/acts/DU/2025/1575/text.pdf).

Porównano pytanie, odpowiedzi A/B/C, klucz i explanation z odpowiednim punktem polskiego tekstu ADR 2025 oraz sprawdzono zakres sprostowania. Ministerstwo zaznacza, że jego kopie mają charakter pomocniczy, a źródłem prawa pozostaje tekst ogłoszony w Dzienniku Ustaw. Dlatego wynik oznacza **zgodność tekstową w sprawdzonym zakresie**, nie formalne zatwierdzenie prawne.

## Podsumowanie

- Porównano: **48** pytań.
- Zgodne w zakresie sprawdzonego punktu: **48**.
- Potwierdzone sprzeczności wymagające poprawki: **0**.
- Przypadki, których nie dało się porównać tekstowo: **0**.
- Zmienione pytania, odpowiedzi, explanation lub klucze: **0**.
- Zmiany statusów weryfikacji: **0**.
- Formalne zatwierdzenia specjalisty: **0**.
- Liczba nierozstrzygniętych porównań w manifeście: **599 → 551**. Jest to licznik porównań tekstowych, a nie licznik pytań formalnie zatwierdzonych.

## Rejestr pytanie → podstawa → wynik

| ID pytania | Podstawa ADR | Wynik | Ustalenie |
|---|---|---|---|
| ADR-B-0002 | ADR 2025, 1.1.3 | Zgodne w zakresie sprawdzonego punktu | 1.1.3: zwolnienia zależą od konkretnych warunków; mała ilość sama nie zwalnia ze wszystkich wymagań. |
| ADR-B-0003 | ADR 2025, 8.2.1 | Zgodne w zakresie sprawdzonego punktu | 8.2.1: zaświadczenie potwierdza wymagane szkolenie kierowcy, ale nie zastępuje prawa jazdy ani innych dokumentów. |
| ADR-B-0004 | ADR 2025, 2.2.3.1.1 | Zgodne w zakresie sprawdzonego punktu | 2.2.3.1.1: klasa 3 obejmuje materiały ciekłe zapalne; klasy 8 i 6.2 opisują inne zagrożenia. |
| ADR-B-0005 | ADR 2025, 2.2.8.1.1 | Zgodne w zakresie sprawdzonego punktu | 2.2.8: klasa 8 dotyczy materiałów żrących, nie promieniotwórczych ani zakaźnych. |
| ADR-B-0006 | ADR 2025, 2.2.43.1.1 | Zgodne w zakresie sprawdzonego punktu | 2.2.43.1.1: klasa 4.3 obejmuje materiały reagujące z wodą z wydzielaniem gazów palnych. |
| ADR-B-0007 | ADR 2025, 5.2.1.8 | Zgodne w zakresie sprawdzonego punktu | 5.2.1.8: znak środowiskowy ostrzega o zagrożeniu dla środowiska i nie zastępuje klasyfikacji. |
| ADR-B-0008 | ADR 2025, 5.4.1.1.3.1 | Zgodne w zakresie sprawdzonego punktu | 5.4.1.1.3.1: słowo ODPAD ma zastosowanie w określonych przypadkach i nie usuwa wymaganych danych towaru. |
| ADR-B-0016 | ADR 2025, 5.3.2.2.2 | Zgodne w zakresie sprawdzonego punktu | 5.3.2.2.2: górny numer oznacza zagrożenie, dolny czterocyfrowy numer UN identyfikuje towar. |
| ADR-B-0017 | ADR 2025, 5.3.2.3.1 | Zgodne w zakresie sprawdzonego punktu | 5.3.2.3.1: litera X ostrzega o niebezpiecznej reakcji z wodą. |
| ADR-B-0018 | ADR 2025, 5.3.2.2.1 | Zgodne w zakresie sprawdzonego punktu | 5.3.2.2.1: standardowy rozmiar tablicy to 400 × 300 mm; przepisy przewidują ograniczone wyjątki. |
| ADR-B-0037 | ADR 2025, 5.4.1.1.1 (a) | Zgodne w zakresie sprawdzonego punktu | 5.4.1.1.1(a): numer UN w dokumencie poprzedzają litery UN. |
| ADR-B-0038 | ADR 2025, 5.4.1.1.1 (b) | Zgodne w zakresie sprawdzonego punktu | 5.4.1.1.1(b): dokument wymaga prawidłowej nazwy przewozowej, nie tylko nazwy handlowej. |
| ADR-B-0042 | ADR 2025, 2.2.2.1.1 | Zgodne w zakresie sprawdzonego punktu | 2.2.2: gazy należą do klasy 2. |
| ADR-B-0043 | ADR 2025, 2.2.62.1.1 | Zgodne w zakresie sprawdzonego punktu | 2.2.62: materiały zakaźne należą do klasy 6.2, a trujące do 6.1. |
| ADR-B-0044 | ADR 2025, 2.2.51.1.1 | Zgodne w zakresie sprawdzonego punktu | 2.2.51: klasa 5.1 dotyczy materiałów utleniających. |
| ADR-B-0045 | ADR 2025, 5.2.1.8 | Zgodne w zakresie sprawdzonego punktu | 5.2.1.8: wymagany znak środowiskowy umieszcza się na sztuce przesyłki zgodnie z zasadami znakowania. |
| ADR-B-0046 | ADR 2025, 5.4.1.1.1 (a); 5.4.1.1.3.1 | Zgodne w zakresie sprawdzonego punktu | 5.4.1.1.1(a), 5.4.1.1.3.1: słowo ODPAD nie zastępuje numeru UN. |
| ADR-B-0051 | ADR 2025, 5.3.2.3.1 | Zgodne w zakresie sprawdzonego punktu | 5.3.2.3.1: powtórzenie cyfry zwykle nasila odpowiadające jej zagrożenie. |
| ADR-B-0052 | ADR 2025, 5.3.2.2.2 | Zgodne w zakresie sprawdzonego punktu | 5.3.2.2: tablica jest pomarańczowa z czarnymi oznaczeniami. |
| ADR-B-0053 | ADR 2025, 5.3.2.3.1 | Zgodne w zakresie sprawdzonego punktu | 5.3.2.3.1: cyfra 8 oznacza właściwości żrące; cały numer należy odczytać w kontekście. |
| ADR-B-0061 | ADR 2025, 5.4.1.1.7 | Zgodne w zakresie sprawdzonego punktu | 5.4.1.1.7: gdy stosuje się 1.1.4.2.1, dokument wymaga dodatkowego wpisu odnoszącego się do tego przepisu. |
| ADR-B-0068 | ADR 2025, 5.4.1.1.1 (h) | Zgodne w zakresie sprawdzonego punktu | 5.4.1.1.1(h): co do zasady dokument zawiera nazwę i adres odbiorcy. |
| ADR-B-0069 | ADR 2025, 5.4.1.1.1 (e) | Zgodne w zakresie sprawdzonego punktu | 5.4.1.1.1(e): dokument podaje liczbę i opis sztuk przesyłek, gdy występują. |
| ADR-B-0070 | ADR 2025, 5.4.1.1.1 (f) | Zgodne w zakresie sprawdzonego punktu | 5.4.1.1.1(f): całkowitą ilość podaje się w jednostce właściwej dla rodzaju towaru. |
| ADR-B-0073 | ADR 2025, 8.1.4.2 | Zgodne w zakresie sprawdzonego punktu | 8.1.4.2: także przy wyłączeniu 1.1.3.6 wymagane jest minimum jednej przenośnej gaśnicy o pojemności 2 kg lub równoważnej skuteczności. |
| ADR-B-0089 | ADR 2025, 5.4.1.1.7 | Zgodne w zakresie sprawdzonego punktu | 5.4.1.1.7: zapis dla 1.1.4.2.1 nie jest zamienny z odwołaniem do innych punktów. |
| ADR-B-0093 | ADR 2025, 3.4; 1.1.3.6 | Zgodne w zakresie sprawdzonego punktu | 3.4 (LQ) i 1.1.3.6 mają odrębne warunki, limity i sposób obliczania. |
| ADR-B-0094 | ADR 2025, 2.2.41.1.1 | Zgodne w zakresie sprawdzonego punktu | 2.2.41: klasa 4.1 obejmuje materiały stałe zapalne; 4.2 i 4.3 opisują inne zagrożenia. |
| ADR-B-0095 | ADR 2025, 2.2.42.1.1 | Zgodne w zakresie sprawdzonego punktu | 2.2.42: klasa 4.2 dotyczy materiałów podatnych na samozapalenie. |
| ADR-B-0096 | ADR 2025, 2.2.52.1.1 | Zgodne w zakresie sprawdzonego punktu | 2.2.52: klasa 5.2 obejmuje nadtlenki organiczne, nie klasę 5.1 ani 6.1. |
| ADR-B-0097 | ADR 2025, 2.2.61.1.1 | Zgodne w zakresie sprawdzonego punktu | 2.2.61: klasa 6.1 obejmuje materiały trujące; 6.2 oznacza materiały zakaźne. |
| ADR-B-0098 | ADR 2025, 2.2.7.1 | Zgodne w zakresie sprawdzonego punktu | 2.2.7: materiały promieniotwórcze należą do klasy 7. |
| ADR-B-0099 | ADR 2025, 2.2.9.1.1; 5.2.2.2.2 | Zgodne w zakresie sprawdzonego punktu | 2.2.9 i 5.2.2.2.2: wzory 9/9A odnoszą się do klasy 9; szczególne zastosowanie 9A zależy od towaru. |
| ADR-B-0114 | ADR 2025, 5.2.1.1 | Zgodne w zakresie sprawdzonego punktu | 5.2.1.1: gdy wymagane jest oznakowanie numerem UN, podaje się właściwy czterocyfrowy numer z prefiksem UN. |
| ADR-B-0115 | ADR 2025, 5.2.2.1.1 | Zgodne w zakresie sprawdzonego punktu | 5.2.2.1.1: brakującą wymaganą nalepkę trzeba uzupełnić; numer UN i dokument jej nie zastępują. |
| ADR-B-0124 | ADR 2025, 2.1.1; 3.2 tabela A | Zgodne w zakresie sprawdzonego punktu | 2.1.1 i 3.2: przed wyborem sposobu przewozu ustala się klasyfikację i właściwą pozycję towaru. |
| ADR-B-0125 | ADR 2025, 3.2.1, tabela A kol. (1) | Zgodne w zakresie sprawdzonego punktu | 3.2.1 tabela A, kolumna 1: numer UN identyfikuje pozycję towaru. |
| ADR-B-0128 | ADR 2025, 3.2.1 tabela A kol. (3a) | Zgodne w zakresie sprawdzonego punktu | 3.2.1 tabela A, kolumna 3a: wskazuje klasę zagrożenia. |
| ADR-B-0132 | ADR 2025, 5.3.1.2 | Zgodne w zakresie sprawdzonego punktu | 5.3.1.2: duże nalepki co do zasady umieszcza się na obu bokach i obu końcach odpowiedniej jednostki. |
| ADR-B-0133 | ADR 2025, 5.3.1.3 | Zgodne w zakresie sprawdzonego punktu | 5.3.1.3: gdy nalepki kontenera nie są widoczne z zewnątrz, może być wymagane powtórzenie ich na pojeździe. |
| ADR-B-0149 | ADR 2025, 3.2 tabela A kol. (7a); 3.4.1 | Zgodne w zakresie sprawdzonego punktu | 3.2 tabela A, kolumna 7a i dział 3.4: limit LQ zależy od towaru i warunków pakowania. |
| ADR-B-0259 | ADR 2025, 1.1.3.6.3 | Zgodne w zakresie sprawdzonego punktu | 1.1.3.6.3: dla kategorii 3 wartość wynosi co do zasady 1000, z uwzględnieniem przypisów i pozycji szczególnych. |
| ADR-B-0271 | ADR 2025, 1.1.3.6.4 | Zgodne w zakresie sprawdzonego punktu | 1.1.3.6.4: 100 × 3 + 600 = 900, więc wynik nie przekracza 1000. |
| ADR-B-0272 | ADR 2025, 1.1.3.6.4 | Zgodne w zakresie sprawdzonego punktu | 1.1.3.6.4: 200 × 3 + 500 = 1100, więc wynik przekracza 1000. |
| ADR-B-0323 | ADR 2025, 1.1.3.6.4 | Zgodne w zakresie sprawdzonego punktu | 1.1.3.6.4: dla różnych kategorii trzeba obliczyć sumę ważoną, a nie sprawdzać każdą kategorię osobno. |
| ADR-B-0606 | ADR 2025, 1.1.3.6.3–1.1.3.6.4 | Zgodne w zakresie sprawdzonego punktu | 1.1.3.6.3–1.1.3.6.4: trzeba ustalić kategorię i ilość w odpowiedniej jednostce; masa całego ładunku nie wystarcza. |
| ADR-B-0197 | ADR 2025, 8.1.4.2 | Zgodne w zakresie sprawdzonego punktu | ADR 8.1.4.2: alternatywny środek gaśniczy musi mieć równoważną skuteczność dla wymaganych klas pożarów; sama masa nie wystarcza. |
| ADR-B-0282 | ADR 2025, 8.1.4.2 | Zgodne w zakresie sprawdzonego punktu | ADR 8.1.4.2: wyłączenie 1.1.3.6 nie znosi wymogu co najmniej jednej przenośnej gaśnicy 2 kg proszku lub równoważnej skuteczności. |


## Szczególna kontrola ADR 1.1.3.6

- **ADR-B-0002:** zwolnienia zależą od warunków ADR; sama mała ilość nie zwalnia ze wszystkich wymagań.
- **ADR-B-0093:** LQ (ilości ograniczone, dział 3.4) to inny mechanizm niż 1.1.3.6.
- **ADR-B-0073:** przy zastosowaniu 1.1.3.6 nadal obowiązuje wymóg gaśnicy z 8.1.4.2.
- **ADR-B-0197:** alternatywny środek gaśniczy musi wykazywać równoważną skuteczność.
- **ADR-B-0282:** wyłączenie ilościowe nie usuwa wymogu minimalnej gaśnicy.
- **ADR-B-0259:** dla kategorii 3 tabela 1.1.3.6.3 wskazuje co do zasady wartość 1000, z uwzględnieniem przypisów i pozycji szczególnych.
- **ADR-B-0271:** 100 × 3 + 600 = 900.
- **ADR-B-0272:** 200 × 3 + 500 = 1100.
- **ADR-B-0323:** przy różnych kategoriach stosuje się sumowanie ważone z 1.1.3.6.4.
- **ADR-B-0606:** sama masa całego ładunku nie wystarcza; trzeba ustalić kategorie i ilości zgodnie z ADR.

## Sprostowanie

W zakresie tej partii nie stwierdzono bezpośredniej sprzeczności z punktami objętymi sprostowaniem poz. 1575. Końcowe potwierdzenie zastosowania sprostowania do każdego pytania pozostaje po stronie specjalisty.

## Kolejny krok

Następna partia obejmie kolejne 40–50 nierozstrzygniętych pytań o progach, dokumentacji, oznakowaniu i warunkach wyłączeń. Wszystkie pytania nadal wymagają niezależnej oceny A/B/C przez specjalistę; żadnego nie oznaczono jako `verified`.
