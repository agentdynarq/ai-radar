"""Build today's digest: fetch sources, render markdown, write archive + README.

Network failures are tolerated: if a source is unreachable the digest simply
records that nothing was fetched, so a transient outage never crashes the daily
job. The archive file for the day and the README are always kept in sync.
"""
from __future__ import annotations

import os
from datetime import datetime, timezone

from .render import render_digest, update_readme
from .sources.arxiv import fetch_arxiv
from .sources.huggingface import fetch_models

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_ARCHIVE_LINKS = 60


def today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _archive_days(archive_dir: str) -> list[str]:
    if not os.path.isdir(archive_dir):
        return []
    days = [f[:-3] for f in os.listdir(archive_dir) if f.endswith(".md")]
    return sorted(days, reverse=True)


def _safe(fetch, label: str):
    try:
        return fetch()
    except Exception as exc:  # network / parse issues must not break the job
        print(f"ai-radar: {label} fetch failed: {exc}")
        return []


def build(root: str = ROOT) -> tuple[str, int, int]:
    day = today()
    papers = _safe(fetch_arxiv, "arxiv")
    models = _safe(fetch_models, "huggingface")
    block = render_digest(day, papers, models)

    archive_dir = os.path.join(root, "archive")
    os.makedirs(archive_dir, exist_ok=True)
    with open(os.path.join(archive_dir, f"{day}.md"), "w", encoding="utf-8") as fh:
        fh.write(f"# AI Radar · {day}\n\n{block}\n")

    days = _archive_days(archive_dir)
    readme_path = os.path.join(root, "README.md")
    with open(readme_path, encoding="utf-8") as fh:
        readme = fh.read()
    readme = update_readme(readme, block, days[:MAX_ARCHIVE_LINKS])
    with open(readme_path, "w", encoding="utf-8") as fh:
        fh.write(readme)

    return day, len(papers), len(models)
