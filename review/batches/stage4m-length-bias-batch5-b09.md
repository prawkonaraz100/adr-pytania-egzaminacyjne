# Etap 4m — partia 5: ADR-B-09 (0235–0240)

Data: 24.10.2026. Fresh main przed partią: 545 pytań, 545 needs_review, 0 verified, 0 otwartych PR.

## Zmiany

Skorygowano wyłącznie warianty A/B/C w istniejących sześciu pytaniach ADR-B-0235–0240. Warianty poprawne skrócono przy zachowaniu kontekstu w stem; dystraktory ADR-B-0237 B oraz ADR-B-0240 A doprecyzowano. Bez zmian identyfikatorów, kluczy A/B/C, wyjaśnień, źródeł i statusów. Zsynchronizowano pełne migawki `review/sequential/235-240.json` i `review/legal-clauses/235-240.json` z brzmieniem opcji.

| Pomiar | Przed | Po |
|---|---:|---:|
| Globalny: najdłuższa poprawna | 365/545 (67,0%) | 359/545 (65,9%) |
| ADR-B-09 | 32/39 (82,1%) | 26/39 (66,7%) |

Metryka: poprawna opcja jest **ściśle** najdłuższa według długości po trim, bez remisów. Próg 40% nadal **NIEOSIĄGNIĘTY** globalnie i w ADR-B-09; bramki `--strict` jeszcze nie aktywowano.

Zmiany nie oznaczają prawnej weryfikacji: nie przeprowadzono dosłownego zestawienia z urzędowym polskim tekstem Dz.U. 2025 poz. 642 ani sprostowaniem 1575. Niezależny recenzent musi ocenić klucz A/B/C i jednoznaczność dystraktorów. Wszystkie rekordy pozostają `needs_review`. Nie zmieniono kursów innych niż podstawowy.

CI: wynik należy odnotować po wykonaniu workflow dla PR. Scalenie wyłącznie po potwierdzonym Quality Gate PASS.
