import unittest

import sys
import os
import numpy as np
sys.path.insert(0, '..')

from src.logistic_regression import run

parent_dir = os.path.split(os.getcwd())
two_levels_up = os.path.split(parent_dir[0])[0]
print('parent_dir', parent_dir)
weak_ts_indices = np.load(os.path.join(two_levels_up, 'files', 'fault1_weak_ts_indices.npy'))

class TestLogisticRegression(unittest.TestCase):
    def testSmallBatchSizeStrongTS(self):
        batch_size = 100
        accuracy = run(batch_size=100)
        assert (accuracy > 0.9)

    def testBigBatchSizeStrongTS(self):
        batch_size = 1000
        accuracy = run(batch_size=1000)
        assert (accuracy > 0.85)

    def testSmallBatchSizeWeakTS(self):
        batch_size = 100
        accuracy = run(batch_size, weak_ts_indices)
        assert (accuracy > 0.9)

    def testBigBatchSizeWeakTS(self):
        batch_size = 1000
        accuracy = run(batch_size, weak_ts_indices)
        assert (accuracy > 0.85)

