# Etap 4x30 — test regresyjny pakietu recenzyjnego

- Data: 2026-10-26.
- Świeży `main` na starcie: `34469947e0c5e353c7140fb6aada1320a8c24e89`.
- Zakres: wyłącznie kurs podstawowy ADR; nie zmieniano treści pytań ani ich statusów.

## Problem i zmiana

Pakiet recenzyjny ma wiele powiązanych plików: manifest, bank, rejestr aktualny, listę rekordów bez zapisanego dosłownego fragmentu MI, raport 4x29, instrukcję recenzji i przewodnik egzaminu. Testy sprawdzały liczbę pytań oraz obecność materiałów, ale nie pilnowały aktualności SHA banku ani spójności listy 121 otwartych pozycji z manifestem.

Dodano test `test_current_snapshot_and_open_quote_list_stay_synchronized` w `tests/test_review_packet_integrity.py`. Test blokuje:
- rozjazd `current_bank_blob_sha` lub SHA z etapu 4x29 względem aktualnego banku;
- rozjazd liczby otwartych porównań z manifestem;
- zmianę liczby 121 pozycji bez dosłownego fragmentu MI, powtórzone ID lub ID nieobecne w banku;
- brak raportu 4x29 lub instrukcji interpretacji wyniku egzaminu;
- przypadkowe zmiany statusu formalnego 609 pytań.

## Kontrola stanu wejściowego

- Bank: 609 ID, brak duplikatów; aktualny blob SHA `ed0dee6e93f21cbb758c3d088a4d02e0aaed9fc4`.
- Lista bez cytatu MI: 121 ID, 121 unikalnych, 0 brakujących w banku.
- Osobna liczba otwartych porównań pełnego tekstu urzędowego: 376.
- Celowane porównania nadal oczekujące: 10.
- Egzaminy próbne 001–005: 5 wariantów, 5 kluczy; test 4x29 potwierdził zgodność po mapowaniu liter opcji.
- Statusy: 609 `needs_review`, 0 `verified`, 0 formalnych zatwierdzeń.

## Zakres dowodów i ograniczenia

121 pozycji bez dosłownego fragmentu MI oraz 376 otwartych porównań pełnego tekstu urzędowego to różne miary. Test pilnuje integralności rejestrów, ale nie rozstrzyga poprawności prawnej. Specjalista nadal musi porównać pytania, odpowiedzi A/B/C, explanation i podstawę z urzędowym ADR 2025 (Dz.U. 2025 poz. 642 i sprostowanie poz. 1575).

## Testy

Wymagany wynik: PASS Quality Gate CI na PR. Testy lokalne nie zostały uruchomione w tym środowisku; nie przedstawiam tego jako lokalnego PASS. Wszystkie pytania pozostają `needs_review`.
