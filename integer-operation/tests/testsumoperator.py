import unittest
import mathoperator.sumoperator as op
import sys

class TestOperator(unittest.TestCase):

    def test_sum_large_integers(self):
        test_list=[10**100,10**100]
        testinstance=op.SumOperator()
        self.assertEqual(testinstance.operation(test_list),2*10**100)

    def test_sum_floats_manages_virtual_infinte(self):
        test_list=[sys.float_info.max,sys.float_info.max]
        testinstance=op.SumOperator()
        self.assertEqual(testinstance.operation(test_list),float("inf"))
    


if __name__ == "__main__":
    unittest.main(verbosity=2)