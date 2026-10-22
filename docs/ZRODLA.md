# Rejestr źródeł i polityka weryfikacji

Stan identyfikacji źródeł: 22.10.2026. Linki prowadzą do źródeł pierwotnych. Przed oceną konkretnego pytania należy sprawdzić aktualność aktu prawnego i odpowiednie przepisy szczegółowe.

| Kod | Dokument | Zastosowanie | Adres |
|---|---|---|---|
| ADR-2025-PL | ADR 2025, ogłoszenie w Dz.U. 2025 poz. 642 | Podstawowe źródło prawa dla polskiego ADR 2025 | https://dziennikustaw.gov.pl/DU/2025/642 |
| ADR-2025-CORR | Sprostowanie polskiego tekstu ADR 2025, Dz.U. 2025 poz. 1575 | Obowiązkowa kontrola ewentualnych zmian słownictwa, numerów UN i warunków | https://eli.gov.pl/api/acts/DU/2025/1575/text.pdf |
| ADR-2025-MI | Pomocnicze teksty polskie ADR 2025 (tomy I i II) | Wyszukiwanie punktów i porównania techniczne; nie są samoistnym źródłem prawa | https://www.gov.pl/web/infrastruktura/towary-niebezpieczne |
| ADR-2025-UNECE | ADR 2025, UNECE | Tekst referencyjny, porównanie numeracji i zakresu | https://unece.org/adr-2025-files |
| PL-KURSY | Rozporządzenie o prowadzeniu kursów, Dz.U. 2021 poz. 2150, załącznik nr 1 | Urzędowy ramowy program i minimalny czas kursu | https://eli.gov.pl/api/acts/DU/2021/2150/text.pdf |
| PL-EGZAMINY | Rozporządzenie MI 26.06.2024, Dz.U. 2024 poz. 964 | Forma i zasady egzaminu (szczególnie § 9–11) | https://eli.gov.pl/api/acts/DU/2024/964/text.html |
| PL-USTAWA | Ustawa o przewozie towarów niebezpiecznych z 19.08.2011 (sprawdzić tekst i późniejsze zmiany) | Obowiązki, kompetencje, podstawy prawne uprawnień | https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20112271367 |

## Ważne zastrzeżenia

1. **Sprostowanie jest obowiązkowe**: akt z 18.11.2025 (Dz.U. poz. 1575) zmienia m.in. wybrane dane w Tabeli A oraz brzmienie 8.2.2.7.2.3, w którym „10 pytań” zastąpiono „15 pytań”. Każdy właściwy zapis w bazie kontrolujemy także względem sprostowania.
2. Ministerstwo Infrastruktury zastrzega, że pomocnicze PDF-y ADR na stronie MI **nie są same w sobie źródłem prawa**. Podstawą jest ogłoszenie w Dzienniku Ustaw. W razie rozbieżności potwierdzamy właściwe ogłoszenie i sprostowania.
3. W 2026 roku materiał merytoryczny opieramy na ADR 2025 i właściwych zmianach lub dopuszczonych odstępstwach. Następne wydanie ADR wymaga osobnego przeglądu migracyjnego.
4. Oznaczenie „verified” dotyczy **konkretnego twierdzenia** i **konkretnego stanu prawnego**, nie całego działu naraz.
5. Jeżeli przepis jest sporny, odpowiedź zależy od warunków pominiętych w pytaniu albo źródła nie da się zweryfikować — status blocked.
6. Numery punktów muszą dotyczyć rzeczywiście otwartych i przeczytanych przepisów; nie należy zgadywać numeracji z pamięci.

## Publiczne pytania szkoleniowe (źródła pomocnicze)

Darmowe przykłady mogą służyć analizie zakresu i poziomu trudności, ale bez dowodu pochodzenia **nie są oficjalną państwową pulą pytań**. Nie kopiujemy ich masowo do repozytorium.

- https://vivo-szkolenia-adr.wroclaw.pl/ — opublikowane testy szkoleniowe.
- https://kursadr.pl/ — przykładowe testy kursowe.
- https://gotowinatest.pl/egzamin-adr — ćwiczenia autora serwisu.

## Procedura kontroli źródła

- Zanotować dokładny zapis typu: „ADR 2025, 8.1.5.2” albo „Dz.U. 2024 poz. 964, § 9 ust. 3 pkt 1”.
- Zapisać datę odczytu, link do aktu, wersję i opis warunków stosowania.
- Rozważyć wyjątki, ilości ograniczone, wyłączenia, przepisy przejściowe i rozbieżności krajowe.
- Zabezpieczyć przed plagiatem: własne objaśnienia, własne ilustracje lub udokumentowane licencje.
- Powtórzyć weryfikację przed publikacją, po zmianie ADR lub po zgłoszeniu błędu.


## Audyt partii 001

[Przegląd 39 pytań: źródła, niejednoznaczności i konkretne korekty](AUDYT-MERYTORYCZNY-PARTIA-001.md).

Przy próbach weryfikacji ogromny bezpośredni plik `https://eli.gov.pl/api/acts/DU/2025/642/text.pdf` bywa niedostępny (timeout); nie uznajemy nieudanego odczytu za przegląd prawa. W bazie pytań zapisany jest stabilny adres strony ogłoszenia w Dzienniku Ustaw wraz z konkretnym punktem normy.
