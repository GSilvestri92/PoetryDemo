import unittest
from unittest import mock
from click.testing import CliRunner
import gcbq_explorer.check_existence as check_existence

class TestMain(unittest.TestCase):
    
    @mock.patch('gcbq_explorer.check_existence.BigQueryTable')
    def test_table_existing_output(self,mock_table):
         mock_table.return_value.get_project_name.return_value="project_1"
         mock_table.return_value.get_dataset_name.return_value="dataset_1"
         mock_table.return_value.get_table_name.return_value="table_1"
         mock_table.return_value.get_schema.return_value="mock_schema"
         mock_table.return_value.get_description.return_value="mock_des"
         mock_table.return_value.get_rows.return_value="20"
         runner=CliRunner()
         result=runner.invoke(check_existence.main,"--type TABLE --id project_1.dataset_1.table_1")

         self.assertEqual(result.exit_code,0)
         self.assertEqual(result.output,"Project: project_1\nDataset: dataset_1\nTable: table_1\nSchema: mock_schema\nDescription: mock_des\nRows: 20\n")
    
    @mock.patch('gcbq_explorer.check_existence.BigQueryDataset')
    def test_dataset_exist(self,mock_dataset):
        mock_dataset.return_value.get_project_name.return_value="dataset_1"
        result=check_existence.dataset_exists("proj1.dataset_1")
        self.assertEqual(result.get_project_name(),"dataset_1")

    @mock.patch('gcbq_explorer.check_existence.BigQueryDataset')
    def test_dataset_not_exist(self,mock_dataset):
        mock_dataset.return_value.get_project_name.return_value=None
        result=check_existence.dataset_exists("proj1.dataset_1")
        self.assertEqual(result,None)

    @mock.patch('gcbq_explorer.check_existence.BigQueryTable')
    def test_table_exist(self,mock_table):
        mock_table.return_value.get_project_name.return_value="table_1"
        result=check_existence.table_exists("proj1.dataset_1.table_1")
        self.assertEqual(result.get_project_name(),"table_1")
        
    @mock.patch('gcbq_explorer.check_existence.BigQueryTable')
    def test_table_not_exist(self,mock_table):
        mock_table.return_value.get_project_name.return_value=None
        result=check_existence.table_exists("proj1.dataset_1.table_1")
        self.assertEqual(result,None)

if __name__ == "__main__":
    unittest.main(verbosity=2)
