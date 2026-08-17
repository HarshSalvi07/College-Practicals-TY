import unittest

from src.core_logic import (
    InferenceEngine,
    validate_fact,
    validate_rule,
)


class TestInferenceEngine(unittest.TestCase):

    # --------------------------------------------------
    # Basic Inference Tests
    # --------------------------------------------------

    def test_direct_inference(self):
        engine = InferenceEngine(
            facts={
                ("Hill", "smoke")
            },
            rules={
                ("smoke", "fire")
            }
        )

        self.assertTrue(
            engine.infer(
                ("Hill", "fire")
            )
        )

    def test_query_not_inferred(self):
        engine = InferenceEngine(
            facts={
                ("Hill", "smoke")
            },
            rules={
                ("smoke", "fire")
            }
        )

        self.assertFalse(
            engine.infer(
                ("Hill", "water")
            )
        )

    def test_unrelated_subject(self):
        engine = InferenceEngine(
            facts={
                ("Hill", "smoke")
            },
            rules={
                ("smoke", "fire")
            }
        )

        self.assertFalse(
            engine.infer(
                ("Lake", "fire")
            )
        )

    # --------------------------------------------------
    # Direct Fact Tests
    # --------------------------------------------------

    def test_direct_fact(self):
        engine = InferenceEngine(
            facts={
                ("Hill", "smoke")
            },
            rules=set()
        )

        self.assertTrue(
            engine.infer(
                ("Hill", "smoke")
            )
        )

    def test_empty_knowledge_base(self):
        engine = InferenceEngine()

        self.assertFalse(
            engine.infer(
                ("Hill", "fire")
            )
        )

    # --------------------------------------------------
    # Multiple Rule Tests
    # --------------------------------------------------

    def test_multiple_rules(self):
        engine = InferenceEngine(
            facts={
                ("Hill", "smoke")
            },
            rules={
                ("smoke", "fire"),
                ("fire", "hot")
            }
        )

        self.assertTrue(
            engine.infer(
                ("Hill", "hot")
            )
        )

    def test_multi_step_inference(self):
        engine = InferenceEngine(
            facts={
                ("Metal", "heated")
            },
            rules={
                ("heated", "expanded"),
                ("expanded", "longer")
            }
        )

        self.assertTrue(
            engine.infer(
                ("Metal", "longer")
            )
        )

    # --------------------------------------------------
    # Multiple Subject Tests
    # --------------------------------------------------

    def test_multiple_subjects(self):
        engine = InferenceEngine(
            facts={
                ("Hill", "smoke"),
                ("Kitchen", "smoke")
            },
            rules={
                ("smoke", "fire")
            }
        )

        derived = engine.infer_all()

        self.assertIn(
            ("Hill", "fire"),
            derived
        )

        self.assertIn(
            ("Kitchen", "fire"),
            derived
        )

    # --------------------------------------------------
    # Stability Test
    # --------------------------------------------------

    def test_repeated_inference_is_stable(self):
        engine = InferenceEngine(
            facts={
                ("Hill", "smoke")
            },
            rules={
                ("smoke", "fire")
            }
        )

        first_result = engine.infer_all()
        second_result = engine.infer_all()

        self.assertEqual(
            first_result,
            second_result
        )

    # --------------------------------------------------
    # Invalid Fact Tests
    # --------------------------------------------------

    def test_invalid_fact_structure(self):

        with self.assertRaises(TypeError):

            validate_fact(
                ("Hill",)
            )

    def test_invalid_fact_subject(self):

        with self.assertRaises(ValueError):

            validate_fact(
                ("", "smoke")
            )

    def test_invalid_fact_property(self):

        with self.assertRaises(ValueError):

            validate_fact(
                ("Hill", "")
            )

    # --------------------------------------------------
    # Invalid Rule Tests
    # --------------------------------------------------

    def test_invalid_rule_structure(self):

        with self.assertRaises(TypeError):

            validate_rule(
                ("smoke",)
            )

    def test_invalid_rule_antecedent(self):

        with self.assertRaises(ValueError):

            validate_rule(
                ("", "fire")
            )

    def test_invalid_rule_consequent(self):

        with self.assertRaises(ValueError):

            validate_rule(
                ("smoke", "")
            )

    def test_same_rule_properties_are_rejected(self):

        with self.assertRaises(ValueError):

            validate_rule(
                ("smoke", "smoke")
            )

    # --------------------------------------------------
    # Whitespace Test
    # --------------------------------------------------

    def test_spaces_are_removed(self):

        rule = validate_rule(
            (" smoke ", " fire ")
        )

        self.assertEqual(
            rule,
            ("smoke", "fire")
        )


if __name__ == "__main__":
    unittest.main()