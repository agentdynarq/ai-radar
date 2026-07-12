"""Turn fetched papers and models into the daily digest markdown.

The renderer is pure: given a date and the day's records it returns a markdown
block, and it updates the README by replacing two clearly-marked regions. That
keeps the whole thing idempotent and unit-testable without any network.
"""
from __future__ import annotations

import re

LATEST = ("<!-- LATEST:START -->", "<!-- LATEST:END -->")
ARCHIVE = ("<!-- ARCHIVE:START -->", "<!-- ARCHIVE:END -->")


def _trim(text: str, n: int = 200) -> str:
    text = " ".join((text or "").split())
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def render_digest(day: str, papers, models) -> str:
    """Render one day's digest as a markdown block headed by the date."""
    out = [f"## {day}", "", "### New AI research · arXiv", ""]
    if papers:
        for p in papers:
            et_al = " et al." if len(p.authors) > 1 else ""
            meta = f" · {p.published}" if p.published else ""
            out.append(f"- **[{p.title}]({p.url})** — {p.first_author}{et_al}{meta}")
            if p.summary:
                out.append(f"  <br/>{_trim(p.summary)}")
    else:
        out.append("_No papers fetched today._")

    out += ["", "### New model releases · Hugging Face", ""]
    if models:
        for m in models:
            meta = " · ".join(filter(None, [
                m.pipeline_tag or None,
                f"♥ {m.likes}" if m.likes else None,
                f"↓ {m.downloads}" if m.downloads else None,
            ]))
            suffix = f" — {meta}" if meta else ""
            out.append(f"- **[{m.id}]({m.url})**{suffix}")
    else:
        out.append("_No models fetched today._")

    out.append("")
    return "\n".join(out)


def _replace_between(text: str, markers, payload: str) -> str:
    start, end = markers
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    return pattern.sub(f"{start}\n{payload}\n{end}", text)


def update_readme(readme: str, latest_block: str, archive_days) -> str:
    """Inject the latest digest and the archive index into the README markers."""
    readme = _replace_between(readme, LATEST, latest_block)
    items = "\n".join(f"- [{d}](archive/{d}.md)" for d in archive_days) or "_None yet._"
    return _replace_between(readme, ARCHIVE, items)
