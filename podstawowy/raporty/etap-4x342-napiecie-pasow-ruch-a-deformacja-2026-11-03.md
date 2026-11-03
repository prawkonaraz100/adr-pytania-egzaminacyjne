# Etap 4x342 — napięcie pasów: ruch a deformacja (ADR 7.5.7.1)

Data: 03.11.2026. Gałąź: `stage4x342-avoid-over-tightening-restraints`. Bazowy main: `07e40bcdba7b23b398a197c2f9e66ae5126a7f1d`.

## Zakres i wynik

- Dodano ADR-B-0768 do kompetencji teoretycznej `ADR-B-09-K06` — „Unikanie nadmiernego naprężenia pasów”; liczba pytań: 5→6.
- Pytanie rozróżnia ruch, który zmienia ustawienie sztuki przesyłki lub może ją uszkodzić, od niewielkiego sprężystego luzu. Nie należy dążyć do maksymalnego napięcia, bo pasy nie mogą uszkadzać ani deformować opakowań.
- Podstawa: ADR 2025, 7.5.7.1 (Dz.U. 2025 poz. 642).
- Explanation: 352 znaków / 4 zdania; status `needs_review`.

## Audyt odpowiedzi A/B/C

- A — błędna: maksymalne napięcie nie jest wymagane i może spowodować deformację.
- B — poprawna: zabezpieczenie ma powstrzymać ruchy zmieniające ustawienie lub powodujące uszkodzenie, bez niszczenia opakowań.
- C — błędna: bezwzględny brak jakiegokolwiek ruchu i maksymalne napięcie nie są wymaganiem ADR.

## Metryki banku po partii

- Bank: **768** pytań, 768 `needs_review`, 0 `verified`; blob SHA `6bed8107be2b93ad39b5772b3e3887fabf661033`.
- Kompetencje teorii z mniej niż 6 pytaniami: **12** (3 praktyczne pominięte).
- Moduł ADR-B-09: **61** pytań.
- Rozkład prawidłowych opcji: A/B/C = **257/282/229**.
- Poprawna odpowiedź jest jedyną najdłuższą: **83/768 = 10,81%**; maksimum działu: **14,61%**.

## Synchronizacja artefaktów

- Klucze i warianty egzaminów próbnych 001–005 wskazują aktualny blob banku.
- Snapshoty: `review/sequential/768-768.json`, `review/legal-clauses/768-768.json`.
- Ledger prawny i rejestr specjalisty uzupełnione; status pozostaje `needs_review`.
- Pełne literalne porównanie polskiego tekstu i niezależna recenzja specjalisty pozostają otwarte.

## Źródło

ADR 2025, Dz.U. 2025 poz. 642, 7.5.7.1: https://eli.gov.pl/api/acts/DU/2025/642
