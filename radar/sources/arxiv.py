"""Fetch recent AI papers from the public arXiv API.

No API key and no account are needed; arXiv exposes an open Atom feed. The
network call and the XML parsing are kept separate so the parser can be tested
offline against a fixture.
"""
from __future__ import annotations

import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from xml.etree import ElementTree as ET

ATOM = "{http://www.w3.org/2005/Atom}"
API = "http://export.arxiv.org/api/query"
DEFAULT_CATEGORIES = ("cs.AI", "cs.CL", "cs.LG")


@dataclass
class Paper:
    title: str
    url: str
    summary: str
    published: str  # YYYY-MM-DD
    authors: list[str] = field(default_factory=list)

    @property
    def first_author(self) -> str:
        return self.authors[0] if self.authors else "Unknown"


def _clean(text: str) -> str:
    return " ".join((text or "").split())


def parse_arxiv_atom(xml_text: str) -> list[Paper]:
    """Parse an arXiv Atom response into Paper records."""
    root = ET.fromstring(xml_text)
    papers: list[Paper] = []
    for entry in root.findall(f"{ATOM}entry"):
        title = _clean(entry.findtext(f"{ATOM}title", ""))
        url = _clean(entry.findtext(f"{ATOM}id", ""))
        summary = _clean(entry.findtext(f"{ATOM}summary", ""))
        published = (entry.findtext(f"{ATOM}published", "") or "")[:10]
        authors = [_clean(a.findtext(f"{ATOM}name", "")) for a in entry.findall(f"{ATOM}author")]
        authors = [a for a in authors if a]
        if title and url:
            papers.append(Paper(title, url, summary, published, authors))
    return papers


def fetch_arxiv(categories=DEFAULT_CATEGORIES, max_results: int = 8, timeout: int = 30) -> list[Paper]:
    query = " OR ".join(f"cat:{c}" for c in categories)
    params = urllib.parse.urlencode({
        "search_query": query,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": max_results,
    })
    req = urllib.request.Request(f"{API}?{params}", headers={"User-Agent": "ai-radar/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        xml_text = resp.read().decode("utf-8")
    return parse_arxiv_atom(xml_text)
