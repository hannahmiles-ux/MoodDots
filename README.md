# MoodDots

MoodDots is a tiny solo project that helps you log and visualize how you feel using simple colored dots. It’s a minimalist daily mood tracker with a plain-text data format and a small CLI for quick entries.

This repo intentionally evolves in small, realistic steps to mirror how a person chips away at a side project over weeks. See `scripts/check-commits.sh` for a quick timeline dump.

## Goals
- Quick daily mood logging from the terminal
- File-based storage with human-readable entries
- Lightweight visualization (ASCII grid first, later optional HTML)
- No dependencies beyond the standard library

## CLI (planned)
- `mood add <value> [--note "..."]` where value is 1–5
- `mood show [--range 30d|all]`
- `mood export --format csv|json`

## Quick Start
- `bin/mood add 4 --note "rough draft done"`
- `bin/mood show`
- `bin/mood export --format json`

## Data Format
Entries are stored in `data/moods.csv` with ISO timestamps:

```
timestamp,mood,note
2024-06-11T21:07:33,4,"Wrapped a small feature."
```

## License
MIT
