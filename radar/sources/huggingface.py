"""Fetch newly created models from the public Hugging Face API.

No API key is needed to list public models. As with the arXiv source, the
network call and the JSON parsing are separate so the parser is testable
offline against a fixture.
"""
from __future__ import annotations

import json
import urllib.parse
import urllib.request
from dataclasses import dataclass

API = "https://huggingface.co/api/models"


@dataclass
class Model:
    id: str
    url: str
    likes: int
    downloads: int
    pipeline_tag: str
    created_at: str  # YYYY-MM-DD


def parse_hf_models(payload) -> list[Model]:
    """Parse a Hugging Face /api/models response into Model records."""
    data = json.loads(payload) if isinstance(payload, (str, bytes)) else payload
    models: list[Model] = []
    for item in data:
        mid = item.get("id") or item.get("modelId") or ""
        if not mid:
            continue
        models.append(Model(
            id=mid,
            url=f"https://huggingface.co/{mid}",
            likes=int(item.get("likes") or 0),
            downloads=int(item.get("downloads") or 0),
            pipeline_tag=item.get("pipeline_tag") or "",
            created_at=(item.get("createdAt") or "")[:10],
        ))
    return models


def fetch_models(limit: int = 8, timeout: int = 30) -> list[Model]:
    params = urllib.parse.urlencode({"sort": "createdAt", "direction": -1, "limit": limit})
    req = urllib.request.Request(f"{API}?{params}", headers={"User-Agent": "ai-radar/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        payload = resp.read().decode("utf-8")
    return parse_hf_models(payload)
