import unittest
from bq_client.bigquery_client import BigQueryClient

class TestBQClient(unittest.TestCase):

    def test_table_correctly_returned(self):
        cl=BigQueryClient()
        table=cl.get_table("training-gcp-309207.dataset_1.company_ris")
        self.assertEqual(table.table_id,"company_ris")

    def test_table_not_existing(self):
        cl=BigQueryClient()
        table=cl.get_table("noproj.nodataset.notable")
        self.assertEqual(table,None)

    def test_dataset_correctly_returned(self):
        cl=BigQueryClient()
        dataset,tables=cl.get_dataset("training-gcp-309207.dataset_1")
        self.assertEqual(dataset.dataset_id,"dataset_1")

    def test_dataset_not_existing(self):
        cl=BigQueryClient()
        dataset,tables=cl.get_dataset("noproj.nodataset")
        self.assertEqual(dataset,None)
        self.assertEqual(tables,None)

if __name__ == "__main__":
    unittest.main(verbosity=2)
