# Etap 4x282 — wymagany wpis przy przewozie zgodnie z ADR 1.1.4.2.1

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `76d7fae5ea609c047ef6142eb5cfac07001af76c`  
Gałąź: `stage4x282-vehicle-documents-before-journey`  
Nowe ID: `ADR-B-0708`  
Kompetencja: `ADR-B-10-K02` — dodatkowy wpis w dokumencie przy 1.1.4.2.1

## Wybór luki

Kompetencja miała cztery pytania o dodatkową adnotację w dokumencie przewozowym. Przeważały pytania odtwórcze o samo brzmienie wpisu albo o to, że nie wystarcza sam dojazd do portu. Dodano sytuację z terminalu: przewóz faktycznie odbywa się zgodnie z 1.1.4.2.1, ale wymaganej adnotacji brakuje przed rozpoczęciem odcinka drogowego.

## Dodane pytanie

- `ADR-B-0708`: kierowca odbiera kontener po odcinku morskim; dokumentacja potwierdza zastosowanie 1.1.4.2.1, ale brak wpisu wymaganego przez 5.4.1.1.7.
- Klucz: **B** — przed wyjazdem uzyskać dokument zawierający dokładny wpis „PRZEWÓZ ZGODNY Z 1.1.4.2.1”.
- Explanation: **330 znaków**, 4 zdania; najpierw praktyczny powód poprawnej odpowiedzi, następnie pułapki błędnych, na końcu podstawa ADR.
- Długości A/B/C: **105/102/105** znaków; odpowiedzi są wyrównane, poprawna B nie jest najdłuższa.
- Audyt A/B/C: A — błędnie zakłada automatyczne zastąpienie wpisu dokumentem morskim; B — zawiera dokładną adnotację przewidzianą w 5.4.1.1.7; C — ogólna adnotacja o promie nie zastępuje wymaganego brzmienia.
- Status: `needs_review`; nic nie oznaczono jako `verified`.

## Podstawa prawna

- ADR 2025, 5.4.1.1.7: w przypadku przewozu zgodnie z 1.1.4.2.1 dokument przewozowy musi zawierać informację „PRZEWÓZ ZGODNY Z 1.1.4.2.1”.
- ADR 2025, 1.1.4.2.1: warunki szczególnego traktowania przewozu w łańcuchu transportowym obejmującym przewóz morski lub lotniczy.
- Oficjalny tekst aktu: Dz.U. 2025 poz. 642, ADR 2025: https://eli.gov.pl/api/acts/DU/2025/642/text.pdf
- Strona Ministerstwa Infrastruktury z tekstami ADR 2025: https://www.gov.pl/web/infrastruktura/towary-niebezpieczne
- UNECE ADR 2025: https://unece.org/adr-2025-files

Wyszukiwalny tekst Dz.U. 2025 poz. 642 zawiera dokładne brzmienie wymaganego wpisu w 5.4.1.1.7. Pełne literalne porównanie wraz ze sprostowaniem i niezależna recenzja specjalisty pozostają wymagane.

## Synchronizacja #646

- Bank: 708 pytań ADR-B-0001–0708; wszystkie `needs_review`, 0 `verified`.
- Blob SHA banku: `ee7a6a90e270e62cb6b24b0c2db1e15d9f8ae02c`.
- Warianty i klucze egzaminów próbnych 001–005 wskazują ten SHA.
- Snapshoty sequential/legal 708-708, rejestr źródeł, manifesty, indeksy i metryki odświeżane w tej gałęzi.
- Rozkład prawidłowych opcji A/B/C: 238/251/219.
- „Poprawna = jedyna najdłuższa”: 75/708 = 10,59%; maksimum modułu: 13,95%.
