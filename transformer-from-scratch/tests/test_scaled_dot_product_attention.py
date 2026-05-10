import math
import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from scaled_dot_product_attention import causal_mask, infer_shape, scaled_dot_product_attention


class ScaledDotProductAttentionTests(unittest.TestCase):
    def test_output_shape_matches_query_and_value(self):
        query = [[[1.0, 0.0], [0.0, 1.0]]]
        key = [[[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]]
        value = [[[10.0, 0.0], [0.0, 20.0], [5.0, 5.0]]]

        output, weights = scaled_dot_product_attention(query, key, value)

        self.assertEqual(infer_shape(output), (1, 2, 2))
        self.assertEqual(infer_shape(weights), (1, 2, 3))

    def test_attention_rows_sum_to_one(self):
        query = [[[1.0, 0.0], [0.0, 1.0]]]
        key = [[[1.0, 0.0], [0.0, 1.0]]]
        value = [[[1.0, 2.0], [3.0, 4.0]]]

        _, weights = scaled_dot_product_attention(query, key, value)

        for row in weights[0]:
            self.assertTrue(math.isclose(sum(row), 1.0, rel_tol=1e-9, abs_tol=1e-9))

    def test_causal_mask_blocks_future_positions(self):
        query = [[[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]]
        key = [[[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]]
        value = [[[10.0, 0.0], [0.0, 20.0], [5.0, 5.0]]]
        mask = causal_mask(size=3, batch_size=1)

        _, weights = scaled_dot_product_attention(query, key, value, mask=mask)

        self.assertEqual(weights[0][0][1], 0.0)
        self.assertEqual(weights[0][0][2], 0.0)
        self.assertEqual(weights[0][1][2], 0.0)

    def test_manual_example_matches_expected_values(self):
        query = [[[1.0, 0.0]]]
        key = [[[1.0, 0.0], [0.0, 1.0]]]
        value = [[[10.0, 0.0], [0.0, 20.0]]]

        output, weights = scaled_dot_product_attention(query, key, value)

        expected_first_weight = math.exp(1 / math.sqrt(2))
        expected_second_weight = math.exp(0.0)
        weight_sum = expected_first_weight + expected_second_weight
        expected_weights = [
            expected_first_weight / weight_sum,
            expected_second_weight / weight_sum,
        ]
        expected_output = [
            expected_weights[0] * 10.0 + expected_weights[1] * 0.0,
            expected_weights[0] * 0.0 + expected_weights[1] * 20.0,
        ]

        self.assertTrue(math.isclose(weights[0][0][0], expected_weights[0], rel_tol=1e-9))
        self.assertTrue(math.isclose(weights[0][0][1], expected_weights[1], rel_tol=1e-9))
        self.assertTrue(math.isclose(output[0][0][0], expected_output[0], rel_tol=1e-9))
        self.assertTrue(math.isclose(output[0][0][1], expected_output[1], rel_tol=1e-9))

    def test_fully_masked_row_raises_error(self):
        query = [[[1.0, 0.0]]]
        key = [[[1.0, 0.0], [0.0, 1.0]]]
        value = [[[10.0, 0.0], [0.0, 20.0]]]
        mask = [[[0, 0]]]

        with self.assertRaises(ValueError):
            scaled_dot_product_attention(query, key, value, mask=mask)


if __name__ == "__main__":
    unittest.main()
