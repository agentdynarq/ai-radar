"""ai-radar: a daily, self-updating digest of new AI research and model releases.

Standard library only. Fetches recent arXiv AI papers and newly created
Hugging Face models, renders a dated digest, and keeps the README and an
archive in sync. Designed to run once a day from a GitHub Action.
"""
from .build import build, today
from .render import render_digest, update_readme

__version__ = "0.1.0"

__all__ = ["build", "today", "render_digest", "update_readme", "__version__"]
