import unittest
import integer_operation.dosum as dosum
from click.testing import CliRunner

class TestDosum(unittest.TestCase):

    def test_dosum_click_correctly_sums_integer(self):
        runner=CliRunner()
        result=runner.invoke(dosum.main,"--nums 1 2")

        self.assertEqual(result.exit_code,0)
        self.assertEqual(result.output,"3\n")

    def test_dosum_click_parse_only_integer(self):
        runner=CliRunner()
        result=runner.invoke(dosum.main,"--nums 0.1 2")
        self.assertEqual(result.exit_code,2)

        result2=runner.invoke(dosum.main,"--nums pluto 2")
        self.assertEqual(result2.exit_code,2)

    def test_dosum_requires_param(self):
        runner=CliRunner()
        result=runner.invoke(dosum.main,"")
        self.assertEqual(result.exit_code,2)

if __name__ == "__main__":
    unittest.main(verbosity=2)
