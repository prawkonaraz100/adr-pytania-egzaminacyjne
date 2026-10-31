# Etap 4x250 — czyszczenie pojazdu po przewozie towarów niebezpiecznych luzem

Data: 31.10.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: świeży `main` po PR #719, commit `50ff6cf1d2442f8f9e48b3d4bfadc7e07d7c10e4`  
Nowy rekord: `ADR-B-0677`  
Kompetencja: `ADR-B-03-K03`

## Uzasadnienie luki

Dotychczasowe pytania kompetencji K03 (ADR-B-0009, 0177, 0241 i 0514) dotyczyły przede wszystkim wycieku z opakowanych towarów i zasad ADR 7.5.8.1, w tym bezpiecznego przewozu do miejsca czyszczenia oraz wpisu w dokumencie. Brakowało pytania sprawdzającego odrębny przypadek z ADR 7.5.8.2: pojazd lub kontener po przewozie towarów niebezpiecznych luzem musi być prawidłowo oczyszczony przed ponownym załadunkiem, chyba że nowy ładunek składa się z tych samych towarów niebezpiecznych co poprzedni.

## Dodane pytanie

- **ADR-B-0677** — sytuacja: po rozładunku towaru niebezpiecznego przewożonego luzem ma być załadowany inny towar. Kursant wskazuje obowiązek oczyszczenia pojazdu i wąski wyjątek dla tego samego towaru.
- Klucz: C. Długości opcji A/B/C: 141/101/118 znaków — poprawna odpowiedź nie jest najdłuższa.
- Explanation: 404 znaki, 4 zdania, prostym językiem dla kursanta.
- Status: `needs_review`; brak `verified` i brak formalnej akceptacji specjalisty.

## Zmiany materiałów i kontroli

- Kompetencja ADR-B-03-K03 rozszerzona o ADR 7.5.8.2; teraz 5 pytań.
- Lekcja ADR-B-03 i materiał instruktora uzupełnione o różnicę między 7.5.8.1 (wyciek z opakowanych towarów) i 7.5.8.2 (czyszczenie po przewozie luzem).
- Dodano scenariusz `SC-ADR-B-03-04`; scenariusze kursu: 40.
- Dodano snapshoty `review/sequential/677-677.json` i `review/legal-clauses/677-677.json`; rozszerzono suplement rejestru literalnej weryfikacji do ADR-B-0677. Brak literalnego porównania polskiego tekstu i brak niezależnej recenzji specjalisty pozostają jawne.
- Warianty i klucze egzaminów próbnych 001–005 wskazują aktualny SHA banku `9dbbf511b3b057e3771ee382dda1a768226a916a`.

## Podstawa prawna

ADR 2025, 7.5.8.2. Przepis dotyczy pojazdów i kontenerów, które były załadowane towarami niebezpiecznymi luzem; wymaga prawidłowego oczyszczenia przed ponownym załadunkiem, z wyjątkiem sytuacji, gdy nowy ładunek składa się z tych samych towarów niebezpiecznych co poprzedni. Porównanie z 7.5.8.1 zapobiega przenoszeniu zasad dotyczących wycieku z opakowanych przesyłek na przewóz luzem. Źródło prawa: Umowa ADR ogłoszona w Dz.U. 2025 poz. 642; pomocniczy tekst ADR 2025: UNECE, ECE/TRANS/352/Vol.2.

## Stan po partii

- Bank: **677** pytań, ID ADR-B-0001–0677, wszystkie `needs_review`, zero `verified`.
- Rozkład kluczy po dodaniu: A=232, B=230, C=215.
- Wskaźnik „poprawna = jedyna najdłuższa”: 73/677 = 10,78% (bez wzrostu względem poprzedniego etapu).
- Pełny Quality Gate, synchronizacja kluczy i snapshotów oraz PASS CI wymagane przed scaleniem PR.
