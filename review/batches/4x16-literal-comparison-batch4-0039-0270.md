# Etap 4x16 — partia 4: porównanie literalne kolejnych 48 pytań

- Data: 25.10.2026.
- Punkt wyjścia: świeży `main`, commit `db4b0fc78d9d1685f85575844da82f00ec1a2a42`.
- Zakres: 48 pytań z instrukcji pisemnych i reagowania na zdarzenia, ograniczeń tunelowych, LQ/EQ, oznakowania i klas zagrożenia.
- Bank: 609 pytań; bez zmian w pytaniach i kluczach; wszystkie pozostają `needs_review`, 0 `verified`.

## Źródła

- [Dz.U. 2025 poz. 642 — ADR 2025](https://dziennikustaw.gov.pl/DU/2025/642).
- [Polski tekst ADR 2025, tom I — kopia MI](https://www.gov.pl/attachment/8856b22a-bfd8-4567-8386-b9709bba8da7).
- [Polski tekst ADR 2025, tom II — kopia MI](https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8).
- [Sprostowanie Dz.U. 2025 poz. 1575](https://eli.gov.pl/api/acts/DU/2025/1575/text.pdf).

## Wynik

- Porównano: **48** pytań.
- Zgodne w zakresie sprawdzonego punktu: **48**.
- Potwierdzone sprzeczności wymagające poprawki: **0**.
- Przypadki bez możliwości porównania: **0**.
- Zmiany w banku/kluczach/explanation: **0**.
- Licznik nierozstrzygniętych porównań: **456 → 408**.
- Statusy: wszystkie nadal `needs_review`; 0 `verified`.

## Rejestr pytanie → podstawa → wynik

| ID | Podstawa ADR | Wynik | Ustalenie |
|---|---|---|---|
| ADR-B-0039 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | 5.4.3.4 zawiera standardowy wzór instrukcji pisemnych na czterech stronach; własna skrócona notatka firmy nie zastępuje wymaganego wzoru. |
| ADR-B-0088 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | 5.4.3.2 i 5.4.3.4 określają wymagane instrukcje pisemne; przewoźnik nie może zastąpić ich dowolną, jednostronicową notatką. |
| ADR-B-0100 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Instrukcje pisemne 5.4.3.4 pozwalają ograniczać rozlew tylko wtedy, gdy można to zrobić bez narażania siebie i innych. |
| ADR-B-0101 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Przy nieznanej substancji priorytetem jest bezpieczeństwo: nie dotykaj jej ani nie rozpoznawaj po zapachu, ostrzeż innych i wezwij pomoc. |
| ADR-B-0102 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Pary palne mogą zapalić się od papierosa, e-papierosa lub iskry; nie używaj źródeł zapłonu i oddal się bezpiecznie. |
| ADR-B-0104 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Instrukcje pisemne przewidują zatrzymanie i zabezpieczenie pojazdu, w tym wyłączenie silnika, jeżeli można to zrobić bezpiecznie. |
| ADR-B-0106 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Przy oparach należy oddalić się od źródła i pozostać po stronie nawietrznej, aby ograniczyć wdychanie substancji. |
| ADR-B-0107 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Instrukcje pisemne wyraźnie zabraniają podejmowania gaszenia pożaru w przedziale ładunkowym z towarami niebezpiecznymi. |
| ADR-B-0108 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Gaśnicę można rozważyć przy małym pożarze poza przestrzenią ładunkową tylko wtedy, gdy jest to bezpieczne i zgodne z instrukcjami. |
| ADR-B-0110 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Po skażeniu odzieży należy bezpiecznie ją zdjąć i postąpić według instrukcji pierwszej pomocy; nie wolno przenosić skażenia na inne osoby. |
| ADR-B-0111 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Najpierw ostrzega się osoby w pobliżu i oddala je od zagrożenia; nie należy narażać się, by samodzielnie kierować tłumem w strefie skażenia. |
| ADR-B-0112 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Sprzęt do ograniczania rozlewu i osłony kanalizacji stosuje się tylko wtedy, gdy można to zrobić bezpiecznie, bez kontaktu z substancją. |
| ADR-B-0113 | ADR 2025, 5.4.3.4; program praktyczny zał. 1 (Dz.U. 2021 poz. 2150) | Zgodne w zakresie sprawdzonego punktu | Nie wolno wchodzić do skażonej strefy bez odpowiednich środków i przeszkolenia; najpierw trzeba zapewnić własne bezpieczeństwo i wezwać pomoc. |
| ADR-B-0130 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Przy nieznanej cieczy ogranicz kontakt i wdychanie, oddal się w bezpieczne miejsce i wezwij pomoc; nie próbuj samodzielnie identyfikować rozlewu. |
| ADR-B-0143 | ADR 2025, 5.4.3.4; program kursu lit. k | Zgodne w zakresie sprawdzonego punktu | W tunelu priorytetem jest bezpieczna ewakuacja i alarmowanie; załoga nie podejmuje gaszenia pożaru przedziału ładunkowego. |
| ADR-B-0163 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Osłonięcie odpływu można rozważyć tylko wtedy, gdy jest to bezpieczne i zgodne z instrukcjami; nie wolno wchodzić w rozlew lub opary. |
| ADR-B-0164 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | E-papieros może być źródłem zapłonu; nie używa się go przy palnych oparach, nawet gdy nie widać płomienia. |
| ADR-B-0166 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Gdy ogień obejmuje przestrzeń ładunkową, oddal się, ostrzeż innych i wezwij służby; nie próbuj gasić ładunku. |
| ADR-B-0167 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Skażoną odzież należy bezpiecznie usunąć i postępować według instrukcji pierwszej pomocy; nie rozprowadzać substancji na skórę lub innych ludzi. |
| ADR-B-0178 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Przy chmurze oparów oddal się od źródła i ustaw po stronie nawietrznej, jeśli można to zrobić bezpiecznie. |
| ADR-B-0180 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Nie zakładaj, że zwykłe rękawice chronią przed nieznanym materiałem żrącym; unikaj kontaktu, oddal się i wezwij pomoc. |
| ADR-B-0183 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Jeśli wiatr niesie opary w stronę kierowcy, należy odejść w bezpiecznym kierunku, najlepiej pod wiatr, bez przechodzenia przez chmurę. |
| ADR-B-0184 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Przy małym pożarze pojazdu poza przestrzenią ładunkową gaśnicę można użyć tylko, jeśli jest to bezpieczne, ogień jest w początkowej fazie i droga odwrotu pozostaje wolna. |
| ADR-B-0186 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Osoby postronne trzeba ostrzec i utrzymywać z dala od strefy zagrożenia, nie narażając siebie na kontakt z substancją. |
| ADR-B-0187 | ADR 2025, 5.4.3.4; program szkolenia praktycznego | Zgodne w zakresie sprawdzonego punktu | Pierwszą zasadą pomocy jest nie stawać się kolejną ofiarą; nie wchodzi się w chmurę gazu, lecz wzywa służby i przekazuje informacje. |
| ADR-B-0209 | ADR 2025, 8.6.3.3; 8.6.4 | Zgodne w zakresie sprawdzonego punktu | 8.6.4 ogranicza przewóz przez tunele kategorii E dla jednostek, które wymagają oznakowania LQ zgodnie z 3.4.13, z zastrzeżeniem 3.4.14. |
| ADR-B-0210 | ADR 2025, 5.4.3.4; 1.9.5 | Zgodne w zakresie sprawdzonego punktu | W pożarze pojazdu w tunelu należy priorytetowo ewakuować się oznakowanym wyjściem i wezwać pomoc, a nie walczyć z pożarem ładunku. |
| ADR-B-0221 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Po odejściu od źródła oparów należy pozostać w bezpiecznej, nawietrznej lokalizacji i nie wracać do strefy zagrożenia. |
| ADR-B-0222 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Pożaru obejmującego przedział ładunkowy z towarami niebezpiecznymi załoga nie gasi; ewakuuje się i alarmuje służby. |
| ADR-B-0223 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Gaśnicę można rozważyć przy małym pożarze opony, jeśli ogień nie objął ładunku, działanie jest bezpieczne i nie opóźnia ewakuacji. |
| ADR-B-0224 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Należy ostrzec osoby postronne i skłonić je do oddalenia się, zachowując własne bezpieczeństwo i nie wchodząc w strefę skażenia. |
| ADR-B-0229 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Jeśli jest to bezpieczne, kierowca udostępnia ratownikom instrukcje pisemne i informacje z dokumentów o przewożonym towarze. |
| ADR-B-0230 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Skażoną odzież należy bezpiecznie zdjąć i postępować zgodnie z instrukcjami pierwszej pomocy; nie wolno przenosić skażenia na inne osoby. |
| ADR-B-0234 | ADR 2025, 5.4.3.2; 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Wymagany jest standardowy model instrukcji pisemnych ADR; własna jednostronicowa skrócona wersja nie zastępuje wzoru z 5.4.3. |
| ADR-B-0242 | ADR 2025, 5.4.3.4 | Zgodne w zakresie sprawdzonego punktu | Ograniczanie odpływu do kanalizacji jest dopuszczalne tylko, gdy nie naraża kierowcy na kontakt z substancją i jest zgodne z instrukcjami. |
| ADR-B-0254 | ADR 2025, 8.1.5.3 | Zgodne w zakresie sprawdzonego punktu | 8.1.5.3 wymaga maski ucieczkowej dla każdego członka załogi przy nalepkach 2.3 lub 6.1. |
| ADR-B-0255 | ADR 2025, 5.3.2.2.2 | Zgodne w zakresie sprawdzonego punktu | Na numerowanej tablicy pomarańczowej numer UN znajduje się w dolnym polu; górne pole wskazuje numer rozpoznawczy zagrożenia. |
| ADR-B-0256 | ADR 2025, 5.3.2.3.1 | Zgodne w zakresie sprawdzonego punktu | Litera X przed numerem zagrożenia ostrzega, że materiał reaguje niebezpiecznie z wodą; nie należy używać wody bez sprawdzenia instrukcji. |
| ADR-B-0257 | ADR 2025, 5.3.2.2.2 | Zgodne w zakresie sprawdzonego punktu | 5.3.2.2.2 opisuje tablicę pomarańczową z czarnymi oznaczeniami w dwóch polach: zagrożenie u góry, numer UN na dole. |
| ADR-B-0258 | ADR 2025, 5.3.2.2.1 | Zgodne w zakresie sprawdzonego punktu | 5.3.2.2.1 określa standardową tablicę 400 mm szerokości i 300 mm wysokości. |
| ADR-B-0260 | ADR 2025, 3.5.1.2 | Zgodne w zakresie sprawdzonego punktu | Kod EQ E0 w kolumnie 7b oznacza, że wyłączenie dla ilości wyłączonych nie jest dozwolone dla tej pozycji. |
| ADR-B-0261 | ADR 2025, 3.4.2 | Zgodne w zakresie sprawdzonego punktu | 3.4.2 co do zasady ogranicza masę brutto sztuki przesyłki LQ do 30 kg w typowym opakowaniu zewnętrznym; osobne wyjątki dotyczą tac z folią termokurczliwą. |
| ADR-B-0265 | ADR 2025, 2.2.43.1.1 | Zgodne w zakresie sprawdzonego punktu | 2.2.43.1.1: klasa 4.3 obejmuje materiały, które w kontakcie z wodą wydzielają palne gazy. |
| ADR-B-0266 | ADR 2025, 2.2.51.1.1 | Zgodne w zakresie sprawdzonego punktu | 2.2.51.1.1: klasa 5.1 obejmuje materiały utleniające, które mogą nasilać spalanie. |
| ADR-B-0267 | ADR 2025, 2.2.8.1.1 | Zgodne w zakresie sprawdzonego punktu | 2.2.8.1.1: klasa 8 oznacza materiały żrące. |
| ADR-B-0268 | ADR 2025, 5.2.2.2.2 | Zgodne w zakresie sprawdzonego punktu | Wzór nalepki 4.1 w 5.2.2.2.2 oznacza materiały stałe zapalne. |
| ADR-B-0269 | ADR 2025, 5.2.2.2.2 | Zgodne w zakresie sprawdzonego punktu | Wzór nalepki 4.3 w 5.2.2.2.2 oznacza materiały, które w kontakcie z wodą wydzielają palne gazy. |
| ADR-B-0270 | ADR 2025, 5.2.2.2.2 | Zgodne w zakresie sprawdzonego punktu | Wzór z płomieniem nad okręgiem i cyfrą 5.1 oznacza materiały utleniające. |

## Kontrole liczbowe i szczególne

- ADR 3.4.2: zwykła sztuka przesyłki LQ ma co do zasady limit 30 kg masy brutto; inne zasady dotyczą określonych tac z folią termokurczliwą.
- ADR 3.5.1.2: kod EQ E0 oznacza, że wyłączenie dla ilości wyłączonych nie jest dozwolone dla danej pozycji.
- ADR 8.6.4: jednostki wymagające oznakowania LQ według 3.4.13 podlegają ograniczeniom tuneli kategorii E, z uwzględnieniem 3.4.14.
- ADR 5.4.3.4: instrukcje pisemne prowadzą załogę przez działania awaryjne; nie oznacza to obowiązku gaszenia pożaru obejmującego przedział ładunkowy.

## Kolejny krok

Następna partia obejmie kolejne 40–50 pozycji otwartych. Nie stwierdzono potwierdzonego błędu wymagającego zmiany banku w tej partii. Niczego nie oznaczono jako `verified`.
