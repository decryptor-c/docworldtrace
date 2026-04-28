import unittest

from docworldtrace.docverify import DocVerifyPlus


class DocVerifyPlusTest(unittest.TestCase):
    def test_search_only_evidence_for_required_read_page_is_review(self):
        payload = {
            "status": "completed",
            "seed": {
                "seed_id": "doc__cross__p1_p2",
                "task_type": "cross_page",
                "answerable": True,
                "question": "What heading follows the benchmark description?",
                "reference_answer": "1 Introduction",
                "required_tools": ["search", "read_page", "answer"],
            },
            "tool_sequence": ["search", "read_page", "answer"],
            "final_action": "answer",
            "final_answer": "1 Introduction",
            "trajectory": [
                {
                    "step": 1,
                    "action": "search",
                    "observation": {
                        "status": "success",
                        "confidence": 0.8,
                        "result": {
                            "results": [
                                {
                                    "page": 2,
                                    "snippet": "The next heading is 1 Introduction.",
                                    "score": 1.0,
                                }
                            ]
                        },
                    },
                },
                {
                    "step": 2,
                    "action": "read_page",
                    "observation": {
                        "status": "success",
                        "result": {},
                        "provenance": {"page": None, "bbox": None, "element_type": "corrupted_empty_evidence"},
                    },
                },
                {
                    "step": 3,
                    "action": "answer",
                    "action_input": {"text": "1 Introduction", "evidence_refs": [{"page": 2}]},
                    "observation": {"status": "success", "result": {"text": "1 Introduction"}},
                },
            ],
        }

        result = DocVerifyPlus().verify_rollout(payload)

        self.assertEqual(result["filter_decision"], "review")
        self.assertEqual(result["support_label"], "PARTIAL")
        self.assertEqual(result["failure_taxonomy"], "search_only_evidence")


if __name__ == "__main__":
    unittest.main()
