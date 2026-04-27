import unittest

from docworldtrace import DocEnv
from docworldtrace.pilot.h2_rollout import extract_json_object, normalize_action_call
from docworldtrace.pilot.h2_seeds import candidate_seeds_for_env, select_seed_set


class H2SeedAndParseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.env = DocEnv.from_json("pilot_exp1/sample_document.json")

    def test_candidate_seed_generation(self):
        candidates = candidate_seeds_for_env(self.env, "pilot_exp1/sample_document.json")
        task_types = {item["task_type"] for item in candidates}
        self.assertIn("text_lookup", task_types)
        self.assertIn("table_lookup", task_types)
        self.assertIn("numeric_computation", task_types)
        self.assertIn("verification", task_types)
        self.assertIn("cross_page", task_types)
        self.assertIn("unanswerable", task_types)

    def test_select_seed_set(self):
        candidates = candidate_seeds_for_env(self.env, "pilot_exp1/sample_document.json")
        selected = select_seed_set(
            candidates,
            {
                "text_lookup": 1,
                "table_lookup": 1,
                "numeric_computation": 1,
                "verification": 1,
                "cross_page": 1,
                "unanswerable": 1,
            },
        )
        self.assertEqual(len(selected), 6)

    def test_extract_and_normalize_action(self):
        payload = extract_json_object(
            '```json\n{"thought":"Read the page","action":"read-page","action_input":{"page_id":2}}\n```'
        )
        action, params = normalize_action_call(payload["action"], payload["action_input"])
        self.assertEqual(action, "read_page")
        self.assertEqual(params, {"page_ids": [2]})


if __name__ == "__main__":
    unittest.main()
