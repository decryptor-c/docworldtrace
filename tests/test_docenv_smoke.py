import json
import unittest

from docworldtrace import DocEnv


class DocEnvSmokeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.env = DocEnv.from_json("pilot_exp1/sample_document.json")

    def test_search_and_cache(self):
        first = self.env.search("FY2023 revenue", top_k=3)
        second = self.env.search("FY2023 revenue", top_k=3)
        self.assertEqual(first["status"], "success")
        self.assertFalse(first["cache_hit"])
        self.assertTrue(second["cache_hit"])
        pages = [item["page"] for item in first["result"]["results"]]
        self.assertIn(2, pages)

    def test_parse_table(self):
        result = self.env.parse_table(2, [40, 140, 340, 290])
        self.assertEqual(result["status"], "success")
        self.assertGreaterEqual(len(result["result"]["rows"]), 4)

    def test_compute(self):
        result = self.env.compute(
            "(fy2023 - fy2022) / fy2022 * 100",
            {"fy2022": 2.8, "fy2023": 3.2},
        )
        self.assertEqual(result["status"], "success")
        self.assertAlmostEqual(result["result"]["value"], 14.2857142857, places=4)

    def test_verify(self):
        result = self.env.verify(
            "FY2023 revenue was 3.2",
            [{"page": 2, "bbox": [40, 140, 340, 290]}],
        )
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["result"]["label"], "SUPPORTED")


if __name__ == "__main__":
    unittest.main()
