# Etap 4l — raport gotowości po 4h–4k i uzupełniająca kontrola integralności SVG

Data: 23.10.2026. Stan odczytany bezpośrednio z main przy rozpoczęciu partii: **542 pytania**, ciągłe ADR-B-0001–0542, **542 needs_review**, **0 verified**, brak otwartych PR, **0 rzeczywistych akceptacji**.

## Przegląd zamkniętych obszarów technicznych

| Obszar | Wynik i dowód | Gotowość |
|---|---|---|
| 13 działów i 106 celów w mapie | 103 kompetencje teoretyczne z przypisaniami, 3 praktyczne poza quizem | Strukturalnie spójne |
| Działy 01 i 13 | 35 pytań w każdym, po etapie 4h | Liczbowo uzupełnione, bez odbioru jakości |
| Aktualny wykaz specjalisty | `review/specialist/REJESTR-AKTUALNY-0001-0542.md` — 542 rekordy i klucze; bieżąca kontrola spójności w CI | Do przekazania specjaliście |
| Pliki graficzne przypisane do pytań | **10 istniejących** autorskich SVG z tagami title/desc; w 4j katalog 22 modeli nalepek i 12 innych ilustracji jest głównie **specyfikacją**, nie gotową produkcją | 10 szkiców, wszystkie wymagają fachowego sprawdzenia wzoru |
| System egzaminu próbnego | `scripts/mock_exam.py` wyłącznie z `release_gate.eligible()`; przy braku verified nie generuje arkusza | Technicznie zabezpieczony, publikacja zablokowana |
| 13 scenariuszy i 13 lekcji | Istnieją pytania i karty dydaktyczne; przesiew heurystyczny 4i nie jest niezależnym sprawdzeniem semantycznej różnorodności | Wymagana recenzja praktyczna i dydaktyczna |
| Dosłowna kontrola polskiego ADR 2025 | **0/542** potwierdzonych porównań z urzędowym polskim PDF; pełny rejestr `review/legal-polish/stage4k-literal-verification-ledger-0001-0542.json` | **ZABLOKOWANE** |
| Niezależna recenzja A/B/C | 542 needs_review; 0 approvals | **ZABLOKOWANE** |

## Potwierdzona luka techniczna wykryta po scaleniu pakietu 4l

Walidator strukturalny banku sprawdzał, czy ścieżka `image` zaczyna się od `assets/`, ale **nie wymuszał istnienia ani poprawnego podstawowego formatu graficznego**. Nieistniejący obraz mógł przejść walidację danych i ulec uszkodzeniu dopiero w interfejsie. W tej partii:

1. `scripts/course_consistency.py` sprawdza dla każdego niepustego `image` rzeczywisty plik SVG, brak traversal i ścieżek absolutnych, poprawną składnię XML, znaczniki dostępności `title`/`desc` oraz blokuje aktywną zawartość i zewnętrzne odwołania;
2. `tests/test_course_consistency.py` testuje brakujący plik, SVG bez opisu, element `script` i przypadek prawidłowy;
3. **10/10 aktualnych załączników zostało wcześniej odczytanych jako istniejące SVG z `title` i `desc`**. Jest to kontrola techniczna, **nie kontrola prawnego wzoru ADR**.

Zmiana nie edytuje żadnego pytania, klucza, pliku historycznego audytu ani statusu. Nie generuje nowych obrazów na podstawie niezweryfikowanego prawa.

## Otwarte luki merytoryczne i zalecana kolejność

**P1 — blokada prawna:** uzyskać rzeczywiste tomy urzędowego polskiego Dz.U. 2025 poz. 642 i sprostowanie poz. 1575, sprawdzić stronę i punkt wszystkich 23 nowych pytań 0520–0542, oddzielnie A/B/C oraz wyłączenia; potem kontynuować pozostałe 519. Brak odczytu źródła oznacza *niewykonane*, nie „pozytywnie zweryfikowane”.

**P2 — jakość dydaktyczna:** zweryfikować ręcznie scenariusze pod kątem rzeczywistej decyzji kierowcy; odrzucić fałszywe trafienia heurystyki. Ponowić ręczny audyt dystraktorów z 4a i nie traktować wyważonych liter A/B/C jako dowodu poprawności odpowiedzi.

**P3 — grafiki:** dla pozostałych modeli z katalogu 4j przygotować własne kompletne SVG i przeprowadzić niezależny audyt zgodności z 5.2/5.3/3.4/3.5 oraz kategoriami tuneli, bez odwołań do cudzych grafik i bez używania obrazów do prawdziwego oznakowania. Aktualnie tylko 10 pytań ma przypięty obraz — **nie udawać pełnego pokrycia katalogu**.

**P4 — odbiór kursu:** specjalista ADR, prowadzący ćwiczenia P1–P3, rzeczywista dokumentacja i podpisy. Procedura kontrolowanych wersji/hashów i oddzielne bezpieczeństwo ekspozycji klucza w przyszłym egzaminie.

## Werdykt

**Strukturalnie przygotowany do niezależnej recenzji. Nie jest zatwierdzony merytorycznie, nie jest gotowy do egzaminowania publicznego ani nie ma potwierdzenia legalnej realizacji zajęć.** Wszystkie pytania pozostają `needs_review`, żadnych `verified`. Żadnego kursu cystern ani innej specjalizacji.

Dowody: `review/batches/stage4l-specialist-and-mock-exam.md`, `review/specialist/PAKIET-0542-MANIFEST.json`, `review/legal-polish/stage4k-literal-verification-ledger-0001-0542.json`, `review/batches/stage4j-original-svgs-0541-0542.md`, `review/batches/stage4i-scenario-audit-0539-0540.md`. Wynik wymaganej kontroli CI należy dopisać do Issue #10 dopiero po faktycznym PASS.
