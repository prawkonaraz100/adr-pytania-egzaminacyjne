# Etap 4x19 — uzgodnienie manifestu i rejestru dowodów recenzji

- Zakres: wyłącznie kurs podstawowy ADR.
- Punkt wyjścia: świeży `main` `c1a9ddc60ed760d9e7fcfa4c3daf9fd109b29b75`.
- Bank: 609 pytań, 13 działów; 609 `needs_review`, 0 `verified`, 0 formalnych akceptacji.
- Rejestr źródłowy: `review/legal-polish/stage4w4-literal-verification-ledger-0001-0609.json`.
- Manifest: `review/specialist/PAKIET-0609-MANIFEST.json`.

## Co wykazała kontrola

Rejestr zawiera dokładnie 609 wpisów — po jednym na każde ID banku. W polu `official_polish_pdf_exact_section_access` są trzy odrębne stany dowodowe:

| Stan w rejestrze | Liczba | Co wolno z tego wywnioskować |
|---|---:|---|
| `not_retrieved_not_literally_compared` | 376 | Dokładny tekst urzędowy nie został pobrany i nie wykonano literalnego porównania. |
| `targeted_source_checked_full_literal_comparison_pending` | 10 | Źródło sprawdzono, ale pełne porównanie nadal czeka na wykonanie. |
| Porównanie tekstu polskiego opublikowanego przez MI, z potwierdzeniem w Dz.U. i recenzją specjalisty nadal oczekującymi | 223 | Istnieje zapis porównania ukierunkowanego, lecz nie jest to pełna akceptacja prawna ani zatwierdzenie A/B/C. |
| **Razem** | **609** | Wszystkie rekordy nadal wymagają właściwego poziomu weryfikacji. |

W 223 wpisach znajduje się `literal_comparison_result`; oznacza to zapis wyniku sprawdzenia określonego zakresu, a nie formalne zatwierdzenie. We wszystkich 609 rekordach `abc_independent_specialist_review` pozostaje `pending`, `release_approved` jest `false`, a status pytania to `needs_review`.

## Uzgodnienie manifestu

Pole `unresolved_literal_comparisons: 376` zachowano z jednoznaczną definicją: liczy wyłącznie rekordy, których dokładny tekst urzędowy nie został pobrany i literalnie porównany. Dodano osobne liczniki dla 10 porównań oczekujących i 223 wpisów z zapisanym wynikiem porównania ukierunkowanego. Zapobiega to błędnemu sumowaniu różnych stanów dowodowych i myleniu pokrycia manifestem z prawną weryfikacją.

Raport etapu 4x16 mówi o pokryciu 599/599 pozycji w zakresie tamtego manifestu. To jest licznik pokrycia wpisami, **nie** twierdzenie, że wszystkie 599 pytań przeszły pełne literalne porównanie z prawnie autorytatywnym tekstem Dz.U. Zaktualizowano tekst wyjaśniający tę różnicę.

## Test CI

Dodano test `test_ledger_evidence_counts_match_manifest_without_implying_approval` w `tests/test_review_packet_integrity.py`. Sprawdza, że:
- rejestr ma po jednym wpisie na każde pytanie;
- liczniki manifestu są wyliczone z rzeczywistych wpisów;
- suma stanów dowodowych wynosi 609;
- wszystkie rekordy pozostają `needs_review`, recenzja A/B/C jest `pending`, a `release_approved` jest `false`.

## Następne działanie specjalisty

Dla 376 rekordów należy uzyskać dokładny tekst właściwego punktu w urzędowym polskim ADR i porównać go literalnie. Dla kolejnych 10 trzeba dokończyć porównanie. Dla 223 wpisów z wynikiem ukierunkowanym należy niezależnie potwierdzić zakres w tekście ogłoszonym w Dz.U., sprostowanie oraz wszystkie odpowiedzi A/B/C. Dopiero rzeczywisty specjalista może nadać `verified` zgodnie z procedurą; automatyczne testy nie mogą tego robić.
