
import unittest

from src.metrics import mae, mmre, pred_25


class TestMetrics(unittest.TestCase):

    def setUp(self):
        self.actual = [100, 200, 300]
        self.predicted = [110, 180, 330]

    def test_mae(self):
        self.assertAlmostEqual(
            mae(self.actual, self.predicted), 20.0
        )

    def test_mmre(self):
        self.assertAlmostEqual(
            mmre(self.actual, self.predicted), 0.1
        )

    def test_pred_25(self):
        self.assertEqual(
            pred_25(self.actual, self.predicted), 1.0
        )

    def test_perfect_predictions(self):
        self.assertEqual(mae([100, 200], [100, 200]), 0.0)
        self.assertEqual(mmre([100, 200], [100, 200]), 0.0)
        self.assertEqual(pred_25([100, 200], [100, 200]), 1.0)

    def test_zero_actual_raises_error(self):
        with self.assertRaises(ValueError):
            mmre([0, 100], [10, 110])

        with self.assertRaises(ValueError):
            pred_25([0, 100], [10, 110])

    def test_empty_input_raises_error(self):
        with self.assertRaises(ValueError):
            mae([], [])

    def test_different_lengths_raise_error(self):
        with self.assertRaises(ValueError):
            mae([100, 200], [100])


if __name__ == "__main__":
    unittest.main()
