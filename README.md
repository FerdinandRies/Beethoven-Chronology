# Beethoven Chronology — A Source-Cited Life Dataset

A machine-readable chronology of the life of **Ludwig van Beethoven (1770–1827)** in which **every entry carries its source**.

Most Beethoven timelines on the web repeat dates without saying where they come from. This dataset takes the opposite approach: no date enters the file without a named primary document or a standard scholarly authority behind it, and every date declares how precise it actually is.

## What is in the dataset

`data/beethoven_chronology.csv` — one row per event, with fields:

| Field | Meaning |
|---|---|
| `date` | Start date, ISO 8601 (`YYYY-MM-DD`, or shorter when the precision is lower) |
| `date_end` | End date for events spanning several days (optional) |
| `precision` | `day`, `month`, or `year` — the precision the sources actually support |
| `event` | A factual description of the event |
| `place` | Where it happened |
| `category` | `life`, `work`, `performance`, `travel`, `reception`, or `legacy` |
| `works` | Opus / WoO numbers involved, where applicable |
| `source_type` | `primary` (a surviving document or record) or `secondary` (scholarly literature) |
| `source` | The source itself: a document, or a key from the source registry below |
| `notes` | Caveats, disputes, and anything a responsible user of the data should know |

## Source registry

| Key | Source |
|---|---|
| `CAEYERS2020` | Jan Caeyers, *Beethoven: A Life* (University of California Press, 2020) — the biographical baseline for this project |
| `THAYER-FORBES` | Alexander Wheelock Thayer, *Thayer's Life of Beethoven*, rev. Elliot Forbes (Princeton University Press, 1964) |
| `BRANDENBURG` | *Beethoven: Briefwechsel — Gesamtausgabe*, ed. Sieghard Brandenburg (Henle, 1996–1998) — the complete letters |
| `KINSKY-HALM` | Georg Kinsky, completed by Hans Halm, *Das Werk Beethovens: Thematisch-bibliographisches Verzeichnis* (Henle, 1955) — composition and first-edition years of the works entries |
| Primary records | Baptismal and death registers, autograph documents, concert announcements — named in full in the `source` field |

## Editorial rules

1. **No unsourced entries.** If a date cannot be tied to a primary document or a standard authority, it does not go in.
2. **Precision is declared, never implied.** A date known only to the year is stored as a year, not padded to a plausible-looking day.
3. **Disputes are recorded, not resolved by silence.** Where scholarship disagrees — or where a famous anecdote lacks documentary support — the `notes` field says so explicitly (see, for example, the 1787 Mozart meeting and the "Immortal Beloved" letter, whose addressee the dataset deliberately does not identify).

The current release (v0.3) covers **206 entries** from the grandfather's appointment as Bonn Kapellmeister (1761) to the transfer of the remains to Vienna's Central Cemetery (1888). The bulk of the entries are drawn from a systematic pass through Caeyers (2020), each cited to its chapter; entries resting on primary documents are marked as such. Coverage will keep expanding; the rules above will not change.

## Quick start

```bash
python3 examples/query_examples.py            # print the full timeline
python3 examples/query_examples.py 1800 1810  # print one decade
python3 examples/query_examples.py --category performance
```

The CSV is plain UTF-8 with a header row and loads directly into pandas, R, SQLite, or any spreadsheet.

## Contributing

Contributions are welcome — corrections with better sources most of all. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. The short version: cite a source for every claim, declare the precision honestly, and put disagreements in `notes`.

## Licence

- Code (including the example scripts): AGPL-3.0-only — see [LICENSE](LICENSE).
- Dataset (`data/`): CC BY-SA 4.0 — see [DATA_LICENSE.md](DATA_LICENSE.md). Attribution: "Beethoven Chronology dataset, FerdinandRies/beethoven-chronology".

## Maintainer

Maintained by [Ferdinand Ries](https://github.com/FerdinandRies). The project grows out of ongoing Beethoven scholarship monitoring and source criticism; issues and pull requests are reviewed against the editorial rules above.
