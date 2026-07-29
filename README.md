# ai-radar

[![tests](https://github.com/agentdynarq/ai-radar/actions/workflows/tests.yml/badge.svg)](https://github.com/agentdynarq/ai-radar/actions/workflows/tests.yml)
[![daily digest](https://github.com/agentdynarq/ai-radar/actions/workflows/digest.yml/badge.svg)](https://github.com/agentdynarq/ai-radar/actions/workflows/digest.yml)
![python](https://img.shields.io/badge/python-3.10%2B-blue)
![license](https://img.shields.io/badge/license-MIT-green)
![dependencies](https://img.shields.io/badge/runtime%20deps-none-e8ff00)

A daily, self-updating **radar for AI research and model releases**. Once a day a scheduled GitHub Action fetches the newest [arXiv](https://arxiv.org/) AI papers (cs.AI, cs.CL, cs.LG) and the newest models on the [Hugging Face](https://huggingface.co/) Hub, renders a dated digest, and commits it. The section below is regenerated automatically, so this page always shows what landed most recently.

Pure Python standard library. No API keys, no servers, no dependencies.

Part of [Dynarq](https://www.dynarq.com).

## Latest digest

<!-- LATEST:START -->
## 2026-07-29

### New AI research · arXiv

_No papers fetched today._

### New model releases · Hugging Face

- **[dfsfsdg5657/MyAwesomeModel-TestRepo](https://huggingface.co/dfsfsdg5657/MyAwesomeModel-TestRepo)**
- **[Zhouhc/xqueryer-lightweight](https://huggingface.co/Zhouhc/xqueryer-lightweight)**
- **[phonglanvq/tensorizer-scanner-bypass-poc-20260729](https://huggingface.co/phonglanvq/tensorizer-scanner-bypass-poc-20260729)**
- **[sdsssjjjj/MyAwesomeModel-TestRepo](https://huggingface.co/sdsssjjjj/MyAwesomeModel-TestRepo)** — feature-extraction
- **[kaizensuper/pmodel_630](https://huggingface.co/kaizensuper/pmodel_630)**
- **[ssghjlid/MyAwesomeModel-TestRepo](https://huggingface.co/ssghjlid/MyAwesomeModel-TestRepo)** — feature-extraction
- **[models4world/tinker_9f4e655c](https://huggingface.co/models4world/tinker_9f4e655c)**
- **[Saman11233/distilbert-imdb-sentiment](https://huggingface.co/Saman11233/distilbert-imdb-sentiment)** — text-classification

<!-- LATEST:END -->

## Archive

<!-- ARCHIVE:START -->
- [2026-07-29](archive/2026-07-29.md)
- [2026-07-28](archive/2026-07-28.md)
- [2026-07-27](archive/2026-07-27.md)
- [2026-07-23](archive/2026-07-23.md)
- [2026-07-21](archive/2026-07-21.md)
- [2026-07-20](archive/2026-07-20.md)
- [2026-07-19](archive/2026-07-19.md)
- [2026-07-18](archive/2026-07-18.md)
- [2026-07-17](archive/2026-07-17.md)
- [2026-07-16](archive/2026-07-16.md)
- [2026-07-14](archive/2026-07-14.md)
- [2026-07-13](archive/2026-07-13.md)
- [2026-07-12](archive/2026-07-12.md)
<!-- ARCHIVE:END -->

## How it works

```
 cron (daily)
     │
     ▼
 python -m radar
     │
     ├─ fetch arXiv cs.AI/cs.CL/cs.LG   (open Atom API, no key)
     ├─ fetch Hugging Face new models   (open JSON API, no key)
     ├─ render a dated markdown digest
     ├─ write archive/YYYY-MM-DD.md
     └─ refresh the README's Latest + Archive sections
     │
     ▼
 commit the real diff and push
```

The network fetch and the parsing are separate, so the parsers are unit-tested offline against fixtures. A source being briefly unreachable never breaks the job: the digest just notes that nothing was fetched that day.

## Run locally

```bash
python -m radar
```

That regenerates today's `archive/` entry and updates this README in place.

## Project structure

```
ai-radar/
  radar/
    sources/
      arxiv.py          fetch + parse arXiv Atom feed
      huggingface.py    fetch + parse Hugging Face model list
    render.py           digest markdown + README section updates
    build.py            orchestrate fetch -> render -> write
  archive/              one markdown file per day
  tests/                offline parser and renderer tests
  .github/workflows/
    digest.yml          the daily scheduled build
    tests.yml           unit tests on push / PR
```

## Tests

```bash
python -m unittest discover -s tests -v
```

## License

MIT
