import unittest

import numpy as np

from bloch.bloch import bloch


class Numpy2CompatibilityTest(unittest.TestCase):
    """Regression tests for the NumPy C-extension boundary."""

    def test_non_float64_non_contiguous_inputs(self):
        b1 = np.array([0.0, 0.5, 1.0], dtype=np.float32)[::2]
        gr = np.array([0.0, 0.0, 0.0], dtype=np.float32)[::2]
        df = np.array([-10.0, 0.0, 10.0], dtype=np.float32)[::2]
        dp = np.array([-0.5, 0.0, 0.5], dtype=np.float32)[::2]

        mx, my, mz = bloch(b1, gr, 1e-6, 1.0, 1.0, df, dp, 0)

        self.assertEqual((2, 2), mx.shape)
        self.assertEqual(mx.shape, my.shape)
        self.assertEqual(mx.shape, mz.shape)
        self.assertTrue(np.isfinite(mx).all())
        self.assertTrue(np.isfinite(my).all())
        self.assertTrue(np.isfinite(mz).all())


if __name__ == "__main__":
    unittest.main()
