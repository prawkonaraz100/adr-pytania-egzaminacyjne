# Etap 4x9 — lista kontrolna dla specjalisty ADR (kurs podstawowy)

**Status: do niezależnego sprawdzenia.** Lista nie oznacza zatwierdzenia prawnego ani pewności zmian ADR 2027. Bank: 609 `needs_review`, 0 `verified`.

## Obowiązkowy przebieg dla każdej pozycji

1. Zanotuj ID, aktualny tekst pytania, każdą z opcji A/B/C oraz wyjaśnienie.
2. Otwórz dokładny punkt z urzędowego polskiego ADR 2025 (Dz.U. poz. 642) i sprawdź, czy ma zastosowanie sprostowanie Dz.U. poz. 1575.
3. Sprawdź warunki, wyjątki, jednostki, progi, terminy, dokumenty i role odpowiedzialnych osób, a nie tylko pojedynczą liczbę.
4. Po urzędowej publikacji kolejnej edycji (np. ADR 2027) porównaj ten sam punkt z nowym tekstem. Nie zakładaj zmiany bez porównania.
5. Oceniaj **A, B i C osobno**; odnotuj, czy nadal jest tylko jedna prawidłowa odpowiedź i czy explanation dla kursanta nadal tłumaczy błędne opcje.
6. Zanotuj dokładne źródło, punkt, datę, wynik i dane recenzenta. Tylko niezależny specjalista może zatwierdzić treść; sam skrypt i komentarz PR nie zmieniają statusu `needs_review`.
7. Sprawdź lekcję działu, klucze wariantów egzaminacyjnych 001–005 i snapshoty audytu, jeśli zmiana dotyczy używanego pytania.

## Wysoki priorytet: wartości i szczegółowe wymogi

- `ADR-B-0018` (ADR-B-06): Jakie są standardowe wymiary tablicy pomarańczowej ADR? — ADR 2025, 5.3.2.2.1
- `ADR-B-0191` (ADR-B-06): Standardowa pomarańczowa tablica ADR ma 400 × 300 mm. Czy w 5.3.2.2.1 przewidziano też dopuszczalne rozwiązanie dla pojazdu, na którym nie ma miejsca na standardową tablicę? — ADR 2025, 5.3.2.2.1
- `ADR-B-0258` (ADR-B-06): Zespół przygotowuje standardową pomarańczową tablicę ADR o szerokości 40 cm. Jaka jest jej standardowa wysokość przed uwzględnieniem wyjątków i tolerancji? — ADR 2025, 5.3.2.2.1
- `ADR-B-0022` (ADR-B-08): Jaka jest minimalna łączna pojemność gaśnic (w przeliczeniu na proszek) dla jednostki transportowej ADR o DMC powyżej 7,5 t, gdy stosuje się pełne wymagania 8.1.4.1? — ADR 2025, 8.1.4.1
- `ADR-B-0071` (ADR-B-08): Jednostka transportowa o DMC 3,5 t przewozi ADR na pełnych zasadach 8.1.4.1. Jaka minimalna łączna pojemność gaśnic jest wymagana? — ADR 2025, 8.1.4.1
- `ADR-B-0072` (ADR-B-08): Jednostka transportowa ma DMC 6 t i przewozi ADR na pełnych zasadach 8.1.4.1. Jaka jest minimalna łączna pojemność gaśnic? — ADR 2025, 8.1.4.1
- `ADR-B-0073` (ADR-B-08): Jaka jest **minimalna** pojemność przenośnej gaśnicy proszkowej wymagana przez ADR 8.1.4.2 dla jednostki transportowej przewożącej towary niebezpieczne zgodnie z 1.1.3.6? — ADR 2025, 8.1.4.2
- `ADR-B-0417` (ADR-B-08): Jednostka transportowa ADR o DMC dokładnie 3,5 t jest objęta pełnym reżimem 8.1.4.1. Ile gaśnic minimalnie wymaga tabela? — ADR 2025, 8.1.4.1
- `ADR-B-0418` (ADR-B-08): Pojazd ADR DMC 6 t w pełnym reżimie 8.1.4.1 ma jedną gaśnicę 8 kg. Czy spełnia minimalną liczbę? — ADR 2025, 8.1.4.1
- `ADR-B-0419` (ADR-B-08): Dla jednostki ADR o DMC dokładnie 7,5 t stosuje się pełny reżim 8.1.4.1. Jaka minimalna łączna pojemność gaśnic? — ADR 2025, 8.1.4.1
- `ADR-B-0420` (ADR-B-08): Jednostka ADR powyżej 7,5 t ma dwie gaśnice: 2 kg i 6 kg. Czy łączna masa proszku spełnia minimum pełnego reżimu? — ADR 2025, 8.1.4.1
- `ADR-B-0421` (ADR-B-08): Towary ADR jadą w ilościach korzystających z wyłączenia 1.1.3.6. Ile minimum przenośnych gaśnic według 8.1.4.2? — ADR 2025, 8.1.4.2
- `ADR-B-0261` (ADR-B-01): Towar niebezpieczny dopuszczony do przewozu jako LQ umieszczono w zwykłym odpowiednim opakowaniu zewnętrznym z opakowaniami wewnętrznymi. Ile może wynosić co do zasady maksymalna masa brutto takiej sztuki przesyłki zgodnie z ADR 3.4.2? — ADR 2025, 3.4.2
- `ADR-B-0315` (ADR-B-02): Nowe regulacje ADR 2025 wymieniają baterie sodowo-jonowe z elektrolitem organicznym jako UN 3551. Do której klasy należą zgodnie z wykazem? — ADR 2025, 2.2.9.1.7.2; tabela A UN 3551
- `ADR-B-0575` (ADR-B-11): Gdzie znaleźć przypisany towarowi ADR kod ograniczenia przewozu przez tunele? — ADR 2025, 3.2.1 kolumna 15; 8.6.3.1
- `ADR-B-0603` (ADR-B-11): W kolumnie 15 tabeli A przy towarze widnieje kod tunelowy „(-)”. Co oznacza to dla ograniczeń tunelowych ADR? — ADR 2025, 3.2.1, kolumna 15; 8.6.3.1

## Pozostałe flagi automatyczne

Pełne wykazy do selekcji przez specjalistę:
- [B-01–B-04 — 100 flag](../../podstawowy/raporty/etap-4x9-wrazliwosc-01-04.json)
- [B-05–B-08 — 42 flag](../../podstawowy/raporty/etap-4x9-wrazliwosc-05-08.json)
- [B-09–B-13 — 116 flag](../../podstawowy/raporty/etap-4x9-wrazliwosc-09-13.json)

Łącznie 258 automatycznych flag (258 różnych ID). To **szerokie kandydatury do porównania**, nie 258 potwierdzonych zmian przepisów. Wykaz zawiera pozycje oznaczone ostrożnościowo, które mogą nie wymagać zmiany po recenzji. Pozostałe rekordy nie są przez sam brak flagi zwolnione z przeglądu prawnego.

Źródła urzędowe: [Dz.U. 2025 poz. 642](https://dziennikustaw.gov.pl/DU/2025/642) oraz [Dz.U. 2025 poz. 1575](https://dziennikustaw.gov.pl/DU/2025/1575).
