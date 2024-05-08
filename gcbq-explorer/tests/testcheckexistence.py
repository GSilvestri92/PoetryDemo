import unittest
from click.testing import CliRunner
import gcbq_explorer.check_existence as check_existence

class TestMain(unittest.TestCase):
    def test_table_nonexisting_output(self):
        runner=CliRunner()
        result=runner.invoke(check_existence.main,"--type TABLE --id training-gcp-309207.dataset_2.t1")

        self.assertEqual(result.exit_code,0)
        self.assertEqual(result.output,"Table does not exist\n")

    def test_dataset_nonexisting_output(self):
        runner=CliRunner()
        result=runner.invoke(check_existence.main,"--type DATASET --id noproj.nodataset")
        self.assertEqual(result.exit_code,0)
        self.assertEqual(result.output,"Dataset does not exist\n")

    def test_dataset_exist(self):
        result=check_existence.dataset_exists("training-gcp-309207.dataset_1")
        self.assertEqual(result.get_dataset_name(),"dataset_1")

    def test_dataset_not_exist(self):
        result=check_existence.dataset_exists("training-gcp-309207.dataset_2")
        self.assertEqual(result,None)
    
    def test_table_existing_output(self):
        runner=CliRunner()
        result=runner.invoke(check_existence.main,"--type TABLE --id training-gcp-309207.dataset_1.company_ris")

        self.assertEqual(result.exit_code,0)
        self.assertEqual(result.output,"Project: training-gcp-309207\nDataset: dataset_1\nTable: company_ris\nSchema: [SchemaField('ID', 'INTEGER', 'NULLABLE', None, None, (), None), SchemaField('NAME', 'STRING', 'NULLABLE', None, None, (), None)]\nDescription: None\nRows: 2\n")

if __name__ == "__main__":
    unittest.main(verbosity=2)
