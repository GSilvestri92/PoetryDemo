import unittest
import mathoperator.operator as op
import sys

class TestOperator(unittest.TestCase):

    def test_sum_large_integers(self):
        testinstance=op.Operator(10**100,10**100)
        self.assertEqual(testinstance.get_sum(),2*10**100)

    def test_sum_floats_manages_virtual_infinte(self):
        testinstance=op.Operator(sys.float_info.max,sys.float_info.max)
        self.assertEqual(testinstance.get_sum(),float("inf"))
    


if __name__ == "__main__":
    unittest.main(verbosity=2)