# Etap 4x94 — status zmian ADR 2027 i mapa wpływu na bank podstawowy

- Data: 27.10.2026.
- Punkt wejścia: świeży `main`, `9d50facbffa5e9f223904e5f7fad31a92e896222`.
- Bank blob: `4a1a5d7f1ca8a5124eb096cd228aa92952fac6da`.
- Zakres: wyłącznie kurs podstawowy ADR.

## 1. Ważna aktualizacja statusu ADR 2027

Wcześniejsze raporty mówiły o propozycjach zmian i oczekiwaniu na zakończenie terminu na sprzeciw. Stan trzeba teraz zaktualizować: oficjalny rejestr traktatowy ONZ wymienia **C.N.395.2026.TREATIES-XI.B.14 z 9 października 2026 r. jako „Entry into force”** dla zmian załączników A i B ADR. Oznacza to, że zmiany przyjęte w tym pakiecie mają wejść w życie **1 stycznia 2027 r.** Nie należy już opisywać całego pakietu wyłącznie jako nieprzyjętej propozycji.

Źródła urzędowe:
- [UN Treaty Collection — status ADR i C.N.395.2026.TREATIES-XI.B.14](https://treaties.un.org/Pages/ViewDetails.aspx?chapter=11&clang=_en&mtdsg_no=XI-B-14&src=IND)
- [UNECE — wykaz plików ADR 2027, ECE/TRANS/WP.15/274 oraz corrigenda/addenda](https://unece.org/adr-2025-files)
- [UNECE — podsumowanie obszarów zmian ADR 2027](https://unece.org/transport/dangerous-goods)
- [Ministerstwo Infrastruktury — polskie materiały ADR 2025 i sprostowanie](https://www.gov.pl/web/infrastruktura/towary-niebezpieczne)

Skonsolidowany tekst polski ADR 2027 nie został w tej kontroli potwierdzony jako opublikowany w Dzienniku Ustaw. Do mapowania wpływu używa się zatem oficjalnych wykazów zmian ECE/TRANS/WP.15/274, Corr.1, Add.1 i Add.1/Corr.1; przed formalną aktualizacją kursu należy ponownie porównać tekst urzędowy.

## 2. Stan Quality Gate i banku

- Quality Gate `main`: PASS, [run #40545223911](https://github.com/prawkonaraz100/adr-pytania-egzaminacyjne/actions/runs/40545223911).
- Liczba pytań / unikalnych ID: 609 / 609.
- Status: 609 `needs_review`, 0 `verified`.
- Explanation minimum: 300 znaków; poniżej 200: 0.
- „Poprawna = jedyna najdłuższa”: 73/609 = 11.99%; maksimum działu 14,29%.

## 3. Mapa wpływu zmian — rekordy do porównania z pakietem 2027

UNECE opisuje w pakiecie zmian m.in. aktualizacje dotyczące baterii litowo-jonowych, sodowo-jonowych i hybrydowych (w tym baterii zainstalowanych w jednostkach ładunkowych), rozwiązań wodorowych, niektórych opakowań z tworzyw z recyklingu oraz wymagań bezpieczeństwa pojazdów. To wyznacza obszary kontroli; samo ogólne podsumowanie nie wystarcza do zmiany odpowiedzi.

### Baterie — priorytet wysoki do dokładnego porównania punkt po punkcie

| ID | Obecny zakres pytania | Co porównać z listą zmian 2027 |
|---|---|---|
| ADR-B-0099 | Klasa zagrożenia dla nalepek wzoru 9 i 9A | Czy zmieniły się klasyfikacja, użycie nalepek lub zakres wyjątków dla baterii |
| ADR-B-0162 | Nalepka 9A i UN 3551/3552 | Tabela A, 2.2.9.1.7, 5.2.2 i przepisy szczególne dla baterii |
| ADR-B-0315 | Bateria sodowo-jonowa z elektrolitem organicznym, UN 3551 | Dokładne brzmienie klasyfikacji i wpisu UN po zmianach 2027 |
| ADR-B-0499 | Bateria w urządzeniu a bateria przewożona osobno | Rozróżnienie UN dla baterii umieszczonej w urządzeniu i przewożonej oddzielnie |
| ADR-B-0500 | Badania typu baterii i ogniw | Wymagania badań i uwagi w przepisie o bateriach |
| ADR-B-0501 | Ochrona ogniwa przed zewnętrznym zwarciem | Wymagania techniczne i ich numeracja |
| ADR-B-0502 | Ochrona przy równoległym połączeniu ogniw przed prądem wstecznym | Wymagania techniczne i ich numeracja |

W tym etapie **nie rozstrzygnięto**, które z powyższych punktów zmienia się dokładnie w pakiecie 2027. To lista do sprawdzenia w treści ECE/TRANS/WP.15/274 wraz z corrigenda/addenda, nie stwierdzenie, że istnieje błąd w ADR 2025. Żadnego z tych pytań nie zmieniono.

### M369 — przewóz oleju napędowego

- Oficjalna lista UNECE wskazuje M369 jako umowę dotyczącą przewozu oleju napędowego, podpisaną przez Polskę 30.06.2026 i ważną do **31.12.2026**: [UNECE — umowy wielostronne ADR](https://unece.org/transport/road-transport/adr-multilateral-agreements).
- Polska publikacja: [Obwieszczenie MI z 30.06.2026, Dziennik Urzędowy MI poz. 17](https://www.gov.pl/web/infrastruktura/obwieszczenie-ministra-infrastruktury-z-dnia-30-czerwca-2026-r).
- Skryptowe wyszukiwanie po całym banku nie znalazło pytań zawierających `M369`, `UN 1202`, EN 590, EN 15940, EN 16709/16734 ani odniesień do oleju napędowego/parafinowego. **Nie ma więc pytania wymagającego korekty z powodu M369 w obecnym banku.**
- M369 i M364 to różne umowy i dotyczą innych kwestii. Obie mają termin 31.12.2026 w aktualnym rejestrze; nie zakładać ich przedłużenia bez urzędowego potwierdzenia.

### Inne potencjalne obszary 2027

| Obszar z oficjalnego podsumowania UNECE | Wynik przeszukania banku | Działanie |
|---|---|---|
| Rozwiązania wodorowe | Brak pytań bezpośrednio dopasowanych po terminach „wodór”/„hydrogen” | Nie dodawać pytania bez sprawdzenia sylabusa i konkretnego przepisu |
| Opakowania z tworzyw z recyklingu | Brak bezpośrednich trafień na terminy recyklingowe | Specjalista powinien ustalić, czy zmiany wchodzą w program kursu podstawowego |
| Bezpieczeństwo/konstrukcja pojazdów | Są pytania o wymagania pojazdu, ale brak potwierdzonej kolizji z nową numeracją | Porównać właściwe zmienione punkty części 8–9; nie zmieniać na podstawie ogólnego podsumowania |

## 4. Egzaminy, lekcje i scenariusze

- Nie znaleziono pytań o M369/UN 1202, więc nie wymaga to synchronizacji egzaminów.
- Bank nie został zmieniony; warianty 001–005, klucze i snapshoty pozostają bez zmian.
- Poprzednie kontrole potwierdziły 609/609 referencji pytań w 13 lekcjach oraz 39/39 scenariuszy z poprawnymi powiązaniami.
- Gdy specjalista potwierdzi zmianę w konkretnym punkcie ADR 2027, należy aktualizować wyłącznie pytania/lekcje/scenariusze dotknięte tym punktem, potem odświeżyć warianty i snapshoty dla zmienionych ID.

## 5. Wynik

- Potwierdzone sprzeczności w banku na podstawie porównania z konkretnym przepisem 2027: **0**.
- Pytania zmienione: **0**.
- Priorytet do dalszej pracy: szczegółowy crosswalk siedmiu pytań o baterie z oficjalnym pakietem ECE/TRANS/WP.15/274; kontrola statusu M364/M369 przed 31.12.2026.
- Wszystkie pytania pozostają `needs_review`; nie nadano `verified`.
