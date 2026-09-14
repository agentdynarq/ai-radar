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
## 2026-09-14

### New AI research · arXiv

_No papers fetched today._

### New model releases · Hugging Face

- **[Mulder2007/matching-rc1](https://huggingface.co/Mulder2007/matching-rc1)**
- **[oi-uae/Qwen-Cyber-27B](https://huggingface.co/oi-uae/Qwen-Cyber-27B)**
- **[OzodbekAImarkaz/smolvla_resting-star](https://huggingface.co/OzodbekAImarkaz/smolvla_resting-star)** — robotics
- **[nest102/god01](https://huggingface.co/nest102/god01)**
- **[mradermacher/Clary-2-Cyber-Flash-1.7B-GGUF](https://huggingface.co/mradermacher/Clary-2-Cyber-Flash-1.7B-GGUF)**
- **[lyca-byte/business-revenue-prediction-model](https://huggingface.co/lyca-byte/business-revenue-prediction-model)**
- **[yunjae-won/T14b_32badrevise_S4b_klreg0.1_stage0_checkpoint20](https://huggingface.co/yunjae-won/T14b_32badrevise_S4b_klreg0.1_stage0_checkpoint20)**
- **[wy8edhuh/DeepSeek-R1-0528-Qwen3-8B-heretic-Q6_K-GGUF](https://huggingface.co/wy8edhuh/DeepSeek-R1-0528-Qwen3-8B-heretic-Q6_K-GGUF)**

<!-- LATEST:END -->

## Archive

<!-- ARCHIVE:START -->
- [2026-09-14](archive/2026-09-14.md)
- [2026-09-13](archive/2026-09-13.md)
- [2026-09-12](archive/2026-09-12.md)
- [2026-09-11](archive/2026-09-11.md)
- [2026-09-10](archive/2026-09-10.md)
- [2026-09-08](archive/2026-09-08.md)
- [2026-09-07](archive/2026-09-07.md)
- [2026-09-06](archive/2026-09-06.md)
- [2026-09-05](archive/2026-09-05.md)
- [2026-09-04](archive/2026-09-04.md)
- [2026-09-03](archive/2026-09-03.md)
- [2026-09-02](archive/2026-09-02.md)
- [2026-09-01](archive/2026-09-01.md)
- [2026-08-27](archive/2026-08-27.md)
- [2026-08-26](archive/2026-08-26.md)
- [2026-08-25](archive/2026-08-25.md)
- [2026-08-24](archive/2026-08-24.md)
- [2026-08-23](archive/2026-08-23.md)
- [2026-08-22](archive/2026-08-22.md)
- [2026-08-21](archive/2026-08-21.md)
- [2026-08-20](archive/2026-08-20.md)
- [2026-08-19](archive/2026-08-19.md)
- [2026-08-17](archive/2026-08-17.md)
- [2026-08-16](archive/2026-08-16.md)
- [2026-08-15](archive/2026-08-15.md)
- [2026-08-14](archive/2026-08-14.md)
- [2026-08-13](archive/2026-08-13.md)
- [2026-08-12](archive/2026-08-12.md)
- [2026-08-10](archive/2026-08-10.md)
- [2026-08-06](archive/2026-08-06.md)
- [2026-08-05](archive/2026-08-05.md)
- [2026-08-04](archive/2026-08-04.md)
- [2026-08-02](archive/2026-08-02.md)
- [2026-08-01](archive/2026-08-01.md)
- [2026-07-31](archive/2026-07-31.md)
- [2026-07-30](archive/2026-07-30.md)
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
