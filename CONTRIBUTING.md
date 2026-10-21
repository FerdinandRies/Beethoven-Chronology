# Contributing

Thank you for helping make this dataset more accurate. The project's value is its sourcing discipline, so contributions are reviewed against three rules:

1. **Every claim needs a source.** Name a primary document (register, autograph, announcement, letter) or a standard scholarly authority from the registry in the README. Unsourced dates — however familiar — will not be merged.
2. **Precision must be honest.** If the source supports only a year, the entry is a year. Do not pad a date to look exact.
3. **Disagreements go in `notes`.** If authorities conflict, or a famous anecdote lacks documentary support, say so in the `notes` field instead of silently picking the version you prefer.

## Practical points

- Follow the field definitions in [data/schema.md](data/schema.md).
- Keep rows sorted by `date`.
- One event per row; a multi-day event uses `date` + `date_end`.
- Corrections to existing entries are as valuable as new ones — please include the source that shows the current entry is wrong.
- New source keys must be added to the registry in the README in the same pull request.

## What is out of scope

- Entries about works' *reception after 1888* (the dataset ends with the transfer of the remains; later reception history belongs in a different project).
- Evaluative claims ("his greatest symphony") — the dataset records events, not judgements.
