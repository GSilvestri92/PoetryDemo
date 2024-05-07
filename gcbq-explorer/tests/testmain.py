import unittest
from bq_client.bigquery_client import BigQueryClient
from click.testing import CliRunner
import main

class TestMain(unittest.TestCase):

    def test_table_nonexisting_output(self):
        runner=CliRunner()
        result=runner.invoke(main,"--type TABLE --id notable")

        self.assertEqual(result.exit_code,0)
        self.assertEqual(result.output,"Table does not exist\n")

    def test_dataset_nonexisting_output(self):
        runner=CliRunner()
        result=runner.invoke(main,"--type DATASET --id nodataset")

        self.assertEqual(result.exit_code,0)
        self.assertEqual(result.output,"Dataset does not exist\n")
    
    def test_table_existing_output(self):
        runner=CliRunner()
        result=runner.invoke(main,"--type TABLE --id notable")

        self.assertEqual(result.exit_code,0)
        self.assertEqual(result.output,"Project: {}\nDataset: {}\nTable: {}\nSchema: {}\nDescription: {}\nRows: {}\n")

if __name__ == "__main__":
    unittest.main(verbosity=2)
