"""Parser tests. These run fully offline against fixtures (no network)."""
import unittest

from radar.sources.arxiv import parse_arxiv_atom
from radar.sources.huggingface import parse_hf_models

ARXIV_FIXTURE = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <id>http://arxiv.org/abs/2607.00001v1</id>
    <published>2026-07-12T10:00:00Z</published>
    <title>A Study of Retrieval-Augmented Agents</title>
    <summary>  We present a method   for grounding agents in retrieved context.  </summary>
    <author><name>Ada Lovelace</name></author>
    <author><name>Alan Turing</name></author>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2607.00002v1</id>
    <published>2026-07-11T09:00:00Z</published>
    <title>Efficient LoRA Fine-Tuning</title>
    <summary>Low-rank adaptation at scale.</summary>
    <author><name>Grace Hopper</name></author>
  </entry>
</feed>
"""

HF_FIXTURE = """[
  {"id": "acme/tiny-llm", "likes": 42, "downloads": 1000,
   "pipeline_tag": "text-generation", "createdAt": "2026-07-12T08:00:00.000Z"},
  {"modelId": "acme/vision-net", "likes": 0, "downloads": 5,
   "pipeline_tag": "image-classification", "createdAt": "2026-07-12T07:00:00.000Z"},
  {"likes": 3}
]"""


class TestArxivParser(unittest.TestCase):
    def setUp(self):
        self.papers = parse_arxiv_atom(ARXIV_FIXTURE)

    def test_count_and_order(self):
        self.assertEqual(len(self.papers), 2)
        self.assertEqual(self.papers[0].title, "A Study of Retrieval-Augmented Agents")

    def test_fields_cleaned(self):
        p = self.papers[0]
        self.assertEqual(p.published, "2026-07-12")
        self.assertEqual(p.first_author, "Ada Lovelace")
        self.assertEqual(len(p.authors), 2)
        self.assertNotIn("  ", p.summary)  # whitespace collapsed

    def test_empty_feed(self):
        self.assertEqual(parse_arxiv_atom(
            '<feed xmlns="http://www.w3.org/2005/Atom"></feed>'), [])


class TestHuggingFaceParser(unittest.TestCase):
    def setUp(self):
        self.models = parse_hf_models(HF_FIXTURE)

    def test_skips_entries_without_id(self):
        self.assertEqual(len(self.models), 2)  # the third has no id

    def test_fields(self):
        m = self.models[0]
        self.assertEqual(m.id, "acme/tiny-llm")
        self.assertEqual(m.url, "https://huggingface.co/acme/tiny-llm")
        self.assertEqual(m.likes, 42)
        self.assertEqual(m.created_at, "2026-07-12")

    def test_accepts_modelid_alias(self):
        self.assertEqual(self.models[1].id, "acme/vision-net")

    def test_accepts_parsed_list(self):
        self.assertEqual(len(parse_hf_models([{"id": "x/y"}])), 1)


if __name__ == "__main__":
    unittest.main()
