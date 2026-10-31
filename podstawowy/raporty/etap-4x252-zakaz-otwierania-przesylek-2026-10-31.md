# Etap 4x252 — zakaz otwierania sztuk przesyłek ADR

Data: 31.10.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: świeży `main` po PR #721, commit `36d0bb3dc7495b8d8563d280ad78dd03f71422b4`  
Kompetencja: `ADR-B-04-K02`  
Nowy scenariusz: `SC-ADR-B-04-04`

## Uzasadnienie luki

Audyt mapy kompetencji wykazał, że ADR-B-04-K02 („Zakaz otwierania przesyłek przez załogę”) ma cztery pytania, ale żaden scenariusz praktyczny nie sprawdzał bezpośrednio tej kompetencji. Dotychczasowe scenariusze modułu 4 dotyczyły palenia/e-papierosów, pracy silnika i postoju pod nadzorem. Brakowało rozmowy z odbiorcą, który prosi członka załogi o otwarcie paczki.

## Zmiana

Dodano `SC-ADR-B-04-04`: odbiorca prosi osobę z załogi, która nie prowadzi pojazdu, o otwarcie paczki, a na opakowaniu widoczny jest ślad mogący wskazywać na uszkodzenie. Kursant ma odmówić otwarcia, rozpoznać, że zakaz ADR 8.3.3 obejmuje wszystkich członków załogi, oraz bezpiecznie zgłosić podejrzenie uszkodzenia bez otwierania przesyłki.

- Pytania powiązane ze scenariuszem: ADR-B-0011, ADR-B-0048 i ADR-B-0357 (trzy pytania; ADR-B-0243 pozostaje dodatkowym pytaniem kompetencji).
- Uzupełniono mapę kompetencji ADR-B-04-K02, lekcję ADR-B-04 i materiał instruktora.
- Scenariusze kursu: **42**; moduły B-03, B-04 i B-05 mają po 4 scenariusze, pozostałe działy co najmniej 3.
- Nie dodano ani nie zmieniono pytań. Bank pozostaje 677 rekordów, wszystkie `needs_review`, zero `verified`.

## Podstawa i ograniczenia

ADR 2025, 8.3.3 — zakaz otwierania sztuk przesyłek z towarami niebezpiecznymi przez członków załogi. Przy podejrzeniu uszkodzenia lub wycieku należy postępować zgodnie z instrukcjami pisemnymi ADR (5.4.3.4). Ćwiczenie wykorzystuje czyste, puste opakowanie szkoleniowe; bez rzeczywistych towarów niebezpiecznych i bez otwierania prawdziwych przesyłek.

## Stan po partii

- Bank: 677 pytań ADR-B-0001–0677, 677 `needs_review`, 0 `verified`.
- SHA banku bez zmian: `9dbbf511b3b057e3771ee382dda1a768226a916a`.
- Scenariusze: 42, w tym 4 dla ADR-B-04.
- Warianty i klucze egzaminów 001–005 pozostają zgodne z niezmienionym SHA banku.
- Pełny Quality Gate i CI wymagane przed scaleniem PR.
