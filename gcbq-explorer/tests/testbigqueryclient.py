import unittest
from bq_client.bigquery_client import BigQueryClient

class TestBQClient(unittest.TestCase):

    def test_table_correctly_returned(self):
        cl=BigQueryClient()
        table=cl.get_table("INSERT TABLE")
        self.assertEqual(table.table_id,"nometabella")

    def test_table_not_existing(self):
        cl=BigQueryClient()
        table=cl.get_table("noproj.nodataset.notable")
        self.assertEqual(table.table_id,None)

    def test_dataset_correctly_returned(self):
        cl=BigQueryClient()
        dataset=cl.get_dataset("INSERT DATASET")
        self.assertEqual(dataset.dataset_id,"nomedataset")

    def test_dataset_not_existing(self):
        cl=BigQueryClient()
        dataset=cl.get_table("noproj.nodataset")
        self.assertEqual(dataset.dataset_id,None)

if __name__ == "__main__":
    unittest.main(verbosity=2)
