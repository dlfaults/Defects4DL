import unittest

import sys
sys.path.insert(0, '..')

from src.logistic_regression import run


class TestLogisticRegression(unittest.TestCase):
    def testSmallBatchSize(self):
        batch_size = 100
        accuracy = run(batch_size)
        assert (accuracy > 0.9)

    def testBigBatchSize(self):
        batch_size = 1000
        accuracy = run(batch_size)
        assert (accuracy > 0.85)

