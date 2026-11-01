# Etap 4x262 — nalepka na przywieszce przy małym lub nieregularnym opakowaniu

Data: 01.11.2026  
Zakres: wyłącznie kurs podstawowy ADR  
Baza: main `af4111ac2b804de1f305b4fccf42695ffebf7100`  
Nowe ID: `ADR-B-0688`  
Kompetencja: `ADR-B-06-K02` — nalepki zagrożeń na opakowaniach

## Wybór luki

Kompetencja miała cztery pytania, które skupiały się na obowiązku umieszczenia wszystkich wymaganych nalepek, w tym nalepek zagrożeń dodatkowych. Nie obejmowała szczególnego rozwiązania dla małej lub nieregularnie ukształtowanej sztuki przesyłki, na której nie da się prawidłowo przykleić nalepki. Nowe pytanie sprawdza dokładnie wyjątek dotyczący sposobu przymocowania nalepki, a nie zwolnienie z jej stosowania.

## Dodane pytanie

- `ADR-B-0688`: mała, nieregularna sztuka przesyłki nie ma powierzchni, na której można prawidłowo przykleić wymaganą nalepkę.
- Klucz: **B** — użyć pewnie umocowanej przywieszki lub innego odpowiedniego sposobu, aby nalepka pozostała przy przesyłce.
- Explanation: **364 znaki, 4 zdania**; wyjaśnia, że kształt opakowania nie znosi obowiązku oznakowania, wskazuje dozwolony sposób i odrzuca mylące alternatywy.
- Długości odpowiedzi A/B/C: **148/118/75** znaków. Poprawna B nie jest ani najdłuższa, ani najkrótsza.
- Status: `needs_review`; nie zmieniono statusu żadnego pytania na `verified`.

## Podstawa prawna

- **ADR 2025, 5.2.2.1.1** — co do zasady należy umieścić nalepki wskazane w kolumnie (5) tabeli A, chyba że przepis szczególny stanowi inaczej.
- **ADR 2025, 5.2.2.1.6** — gdy opakowanie ma tak nieregularny kształt lub tak mały rozmiar, że nalepki nie można zadowalająco umieścić, można ją przymocować do opakowania za pomocą pewnie umocowanej przywieszki lub innego odpowiedniego sposobu.
- Dz.U. 2025 poz. 642: https://dziennikustaw.gov.pl/DU/2025/642
- Oficjalny tekst polski ADR tom II 2025, Ministerstwo Infrastruktury: https://www.gov.pl/attachment/b7292c03-ac9d-4f80-9a29-c22f53d847b8
- Tekst ADR 2025, tom II: https://www.euraca.eu/media/frmeo2lm/adr-2025-vol-ii.pdf

Pytanie nie sugeruje, że można pominąć nalepkę; dotyczy wyłącznie alternatywnego sposobu jej zamocowania w ściśle określonej sytuacji. Nie dotyczy odrębnego obowiązku oznakowania IBC o pojemności powyżej 450 l i dużych opakowań na dwóch przeciwległych stronach (ADR 5.2.2.1.7). Pełne literalne porównanie z właściwym tekstem Dz.U. oraz niezależna recenzja specjalisty pozostają pending. Pytanie pozostaje `needs_review`.

## Synchronizacja #646

- Bank: **688** pytań ADR-B-0001–0688; wszystkie `needs_review`, 0 `verified`.
- Blob SHA `questions.jsonl`: `a041f8814aa0c5f0f648d0e98cb25c0055d3821d`.
- Rozkład prawidłowych opcji: **A=236 / B=235 / C=217**.
- „Poprawna = jedyna najdłuższa”: **72/688 = 10,47%**, poniżej limitu Quality Gate 18%; maksimum działu 13,95%.
- `ADR-B-06-K02` ma teraz 5 pytań; moduł ADR-B-06 ma 56 pytań.
- Zaktualizowano klucze i warianty egzaminów próbnych 001–005 do aktualnego SHA; dodano snapshoty `review/sequential/688-688.json` i `review/legal-clauses/688-688.json`; zaktualizowano ledger, manifesty, kolejki recenzenckie, mapę kompetencji, lekcję i materiał instruktora.
- PR i CI: do potwierdzenia po otwarciu PR. Nie uruchomiono lokalnego Quality Gate.

## Pliki audytowe

- Rejestr: `review/specialist/REJESTR-0688-0688.md`
- Ledger: `review/legal-polish/stage4w4-literal-verification-ledger-0610-0678.json`
- Snapshot sekwencyjny: `review/sequential/688-688.json`
- Snapshot prawny: `review/legal-clauses/688-688.json`
