"""Renderer and README-update tests (offline)."""
import unittest

from radar.render import ARCHIVE, LATEST, render_digest, update_readme
from radar.sources.arxiv import Paper
from radar.sources.huggingface import Model

PAPERS = [
    Paper("Retrieval Agents", "http://arxiv.org/abs/1", "A grounded agent method.",
          "2026-07-12", ["Ada Lovelace", "Alan Turing"]),
]
MODELS = [
    Model("acme/tiny-llm", "https://huggingface.co/acme/tiny-llm", 42, 1000,
          "text-generation", "2026-07-12"),
]


class TestRenderDigest(unittest.TestCase):
    def test_contains_date_and_content(self):
        md = render_digest("2026-07-12", PAPERS, MODELS)
        self.assertIn("## 2026-07-12", md)
        self.assertIn("[Retrieval Agents](http://arxiv.org/abs/1)", md)
        self.assertIn("Ada Lovelace et al.", md)
        self.assertIn("[acme/tiny-llm]", md)
        self.assertIn("♥ 42", md)

    def test_empty_sources_are_labelled(self):
        md = render_digest("2026-07-12", [], [])
        self.assertIn("_No papers fetched today._", md)
        self.assertIn("_No models fetched today._", md)


class TestUpdateReadme(unittest.TestCase):
    def _template(self):
        return (
            "# ai-radar\n\n## Latest\n"
            f"{LATEST[0]}\nold\n{LATEST[1]}\n\n## Archive\n"
            f"{ARCHIVE[0]}\nold\n{ARCHIVE[1]}\n"
        )

    def test_injects_latest_and_archive(self):
        block = render_digest("2026-07-12", PAPERS, MODELS)
        out = update_readme(self._template(), block, ["2026-07-12", "2026-07-11"])
        self.assertIn("## 2026-07-12", out)
        self.assertIn("- [2026-07-12](archive/2026-07-12.md)", out)
        self.assertIn("- [2026-07-11](archive/2026-07-11.md)", out)
        self.assertNotIn("\nold\n", out)  # both regions replaced

    def test_idempotent_markers_survive(self):
        block = render_digest("2026-07-12", [], [])
        once = update_readme(self._template(), block, ["2026-07-12"])
        twice = update_readme(once, block, ["2026-07-12"])
        self.assertEqual(once, twice)
        self.assertIn(LATEST[0], twice)
        self.assertIn(ARCHIVE[1], twice)


if __name__ == "__main__":
    unittest.main()
