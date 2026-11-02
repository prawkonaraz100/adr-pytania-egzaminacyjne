# 4x295 — dopuszczalność przewozu a przepisy szczególne

Data: 02.11.2026. Gałąź `stage4x295-special-provision-admissibility`, baza: main `5e4826a`.

**ADR-B-0721**, kompetencja **ADR-B-01-K07** (towary zabronione i dopuszczone do przewozu), podniesiona z pięciu do sześciu pytań.

Przewoźnik dostał numer UN i nazwę przewozową. W tabeli A ADR przy tej pozycji w kolumnie 6 podano numer przepisu szczególnego, ale nadawca nie sprawdził jego treści. Co należy zrobić przed uznaniem przewozu za dopuszczony?

- A. Uznać przewóz za dozwolony, bo numer UN i nazwa przewozowa w tabeli A wystarczają bez dalszych sprawdzeń.
- B. Pominąć przepis szczególny, jeżeli ładunek jest prawidłowo zapakowany i oznakowany, a nadawca wystawił dokument.
- C. Odczytać przepis szczególny z kolumny 6 i sprawdzić, jakie dodatkowe warunki albo ograniczenia obowiązują.

**Klucz C.** Explanation (375 znaków, 4 zdania):

Numer UN i nazwa przewozowa pomagają znaleźć towar w tabeli A, ale nie mówią jeszcze o wszystkich warunkach jego przewozu. Jeżeli w kolumnie 6 jest numer przepisu szczególnego, trzeba odczytać jego treść i sprawdzić ograniczenia przed przyjęciem ładunku. Samo opakowanie lub prawidłowe oznakowanie nie zastępują tej kontroli. Podstawa: ADR 2025, 3.2.1 (kolumna 6) oraz 3.3.1.

## Podstawa i audyt A/B/C

- Oficjalny tekst ADR 2025: https://eli.gov.pl/api/acts/DU/2025/642/text.pdf. ADR 3.2.1 (kolumna 6) oraz 3.3.1.
- A **błędna:** numer UN i nazwa nie zastępują sprawdzenia przepisu szczególnego przypisanego do danej pozycji.
- B **błędna:** oznakowanie, opakowanie i dokumenty nie zwalniają ze sprawdzenia dodatkowych warunków.
- C **poprawna:** należy odczytać przepis z rozdziału 3.3 przed decyzją o dopuszczeniu przewozu.
- Uwaga: przepisy szczególne mogą również określać warunki albo zwolnienia; nie każdy jest zakazem przewozu.

Odpowiedzi A/B/C mają 105/112/106 znaków. Poprawna nie jest ani najkrótsza, ani najdłuższa.

## Reguła końca — licznik kompetencji

**Kompetencje teoretyczne z mniej niż 6 pytaniami: 59**. Pominięte trzy kompetencje praktyczne. Pozostałe:

- ADR-B-02-K03 — Klasa 3: materiały ciekłe zapalne (5)
- ADR-B-02-K04 — Klasa 4.1: materiały stałe zapalne (5)
- ADR-B-02-K05 — Klasa 4.2: materiały samonagrzewające się / samozapalne (5)
- ADR-B-02-K07 — Klasa 5.1: materiały utleniające (5)
- ADR-B-02-K08 — Klasa 5.2: nadtlenki organiczne (5)
- ADR-B-02-K09 — Klasa 6.1: materiały trujące (5)
- ADR-B-02-K10 — Klasa 6.2: materiały zakaźne (5)
- ADR-B-02-K11 — Klasa 7: materiały promieniotwórcze (rozpoznawanie) (5)
- ADR-B-02-K12 — Klasa 8: materiały żrące (5)
- ADR-B-02-K14 — Grupy pakowania, zagrożenia dodatkowe, tabela A (5)
- ADR-B-03-K02 — Odpady niebezpieczne w dokumencie przewozowym (5)
- ADR-B-03-K03 — Oczyszczanie pojazdu po wycieku i po przewozie luzem (5)
- ADR-B-03-K04 — Ochrona kanalizacji i wód podczas wypadku (5)
- ADR-B-03-K05 — Unikanie skażenia przy rozlewie (5)
- ADR-B-04-K01 — Zakaz palenia i używania e-papierosów (5)
- ADR-B-04-K02 — Zakaz otwierania sztuk przesyłek przez kierowcę i pomocnika kierowcy (5)
- ADR-B-04-K04 — Unikanie źródeł zapłonu przy awarii (5)
- ADR-B-05-K02 — Bezpieczne zatrzymanie i wyłączenie silnika (5)
- ADR-B-05-K03 — Powiadomienie służb i informacje o ładunku (5)
- ADR-B-05-K04 — Unikanie oparów i wybór strony nawietrznej (5)
- ADR-B-05-K05 — Zakaz gaszenia pożaru ładowni (5)
- ADR-B-05-K06 — Mały pożar opon, hamulców lub silnika (5)
- ADR-B-05-K07 — Przekazanie dokumentów ratownikom (5)
- ADR-B-05-K08 — Skażona odzież i środki ochrony (5)
- ADR-B-05-K09 — Ostrzeganie osób postronnych i ewakuacja (5)
- ADR-B-05-K10 — Kamizelka i znaki ostrzegawcze (5)
- ADR-B-05-K11 — Ocena bezpieczeństwa udzielania pierwszej pomocy (5)
- ADR-B-05-K12 — Mocowanie/dostępność gaśnic (5)
- ADR-B-06-K01 — Numer UN na sztuce przesyłki (5)
- ADR-B-06-K02 — Nalepki zagrożeń na opakowaniach (5)
- ADR-B-06-K04 — Znaczenie litery X (5)
- ADR-B-06-K05 — Wymiary i rozmieszczenie tablic (5)
- ADR-B-06-K06 — Powtórzone cyfry i szczególne kombinacje numerów zagrożenia (5)
- ADR-B-06-K07 — Kolor i budowa tablicy (5)
- ADR-B-06-K08 — Znaczenie cyfry 8 (5)
- ADR-B-07-K04 — Odbiorca: przyjęcie i dalsze obowiązki (5)
- ADR-B-07-K07 — Podstawowe rozróżnienie odpowiedzialności cywilnej za szkodę i za niewykonanie zobowiązania (5)
- ADR-B-08-K02 — Gaśnica przy 1.1.3.6 (5)
- ADR-B-08-K03 — Stan techniczny, ważność i dostępność gaśnic (5)
- ADR-B-08-K04 — Klin pod koło (5)
- ADR-B-08-K05 — Kamizelki i latarki dla członków załogi (5)
- ADR-B-08-K06 — Rękawice i ochrona oczu (5)
- ADR-B-09-K02 — Mocowanie sztuk przesyłek (5)
- ADR-B-09-K03 — Kontakt z żywnością i paszami (5)
- ADR-B-09-K04 — Strzałki kierunkowe (5)
- ADR-B-09-K05 — Piętrzenie opakowań (5)
- ADR-B-09-K06 — Unikanie nadmiernego naprężenia pasów (5)
- ADR-B-09-K07 — Czyszczenie pojazdu po rozładunku, także po wycieku (5)
- ADR-B-10-K02 — Dodatkowy wpis w dokumencie przy 1.1.4.2.1 (5)
- ADR-B-11-K04 — Najbardziej restrykcyjny kod w jednostce (5)
- ADR-B-11-K06 — Wyłączenia 1.1.3 i przypadek 3.4.13 (5)
- ADR-B-11-K07 — Zachowanie podczas pożaru w tunelu (5)
- ADR-B-12-K01 — Dokument tożsamości ze zdjęciem (5)
- ADR-B-12-K02 — Zabezpieczenie placów i składowania (5)
- ADR-B-12-K04 — Weryfikacja tożsamości przewoźnika (5)
- ADR-B-13-K03 — Dane odbiorcy i nadawcy (5)
- ADR-B-13-K05 — Dokumenty i dowód tożsamości załogi (5)
- ADR-B-13-K06 — Dodatkowy wpis w transporcie kombinowanym (5)
- ADR-B-13-K07 — Dostępność dokumentów w kabinie (5)

## Integracja i metryki

- Bank: **721 pytań**, wszystkie **needs_review**, zero **verified**; ostatnie ID ADR-B-0721.
- Git blob SHA banku: `cb0edf87af4dd78faa5789596c709d50b50e9b45`.
- Rozkład A/B/C: 241/258/222.
- Poprawna = jedyna najdłuższa: **77/721 = 10,68%**, maksimum działu 13,95% (limit 18%).
- Klucze i warianty egzaminów próbnych 001–005 zsynchronizowane.
- Snapshoty `review/sequential/721-721.json` i `review/legal-clauses/721-721.json` oraz ledger i manifest specjalisty wymagają niezależnej recenzji.
- Rejestr `REJESTR-AKTUALNY-0001-0721.md` zawiera jeden rekord na ID.
- Kolejna partia **4x296**: wyłącznie pierwsza kompetencja teoretyczna z listy <6, od ID ADR-B-0722 po świeżym main. Bez dopisywania po osiągnięciu zera.
