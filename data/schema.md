# Dataset schema

File: `data/beethoven_chronology.csv` (UTF-8, comma-separated, header row, one event per row).

## Fields

| Field | Required | Format / vocabulary |
|---|---|---|
| `date` | yes | ISO 8601. Length must match `precision`: `YYYY-MM-DD` (day), `YYYY-MM` (month), `YYYY` (year) |
| `date_end` | no | Same format as `date`; only when an event spans a range (e.g. a letter written over two days) |
| `precision` | yes | `day` \| `month` \| `year` — the precision supported by the cited source |
| `event` | yes | Free text, present tense or neutral past; facts only, no evaluation |
| `place` | yes | City, with venue in parentheses or in `event` where relevant |
| `category` | yes | `life` \| `work` \| `performance` \| `travel` \| `reception` \| `legacy` |
| `works` | no | Opus numbers (`Op. 67`) and/or WoO numbers (`WoO 63`), separated by `; ` |
| `source_type` | yes | `primary` \| `secondary` |
| `source` | yes | For primary sources, the document itself. For secondary sources, a key from the registry in the README |
| `notes` | no | Disputes, caveats, identification problems, and source conflicts |

## Rules

- A row's `date` may never be more precise than its `source` supports.
- `source_type=primary` requires the actual document or record to be named in `source` (a secondary key may be appended after `; ` as corroboration).
- Rows are sorted by `date`, then by `event`.
- Posthumous events (category `legacy`) are permitted but must be marked as such in `notes` when not obvious.
