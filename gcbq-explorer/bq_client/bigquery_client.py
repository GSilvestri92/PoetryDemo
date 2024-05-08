from google.cloud import bigquery
from google.cloud.exceptions import NotFound

class BigQueryClient():

    __client= None

    def __init__(self):
        self.__client = bigquery.Client()

    def get_table(self,table_id):
        try:
            table=self.__client.get_table(table_id)  # Make an API request.
            return table
        except NotFound:
            return None

    def get_dataset(self,dataset_id):
        try:
            dataset=self.__client.get_dataset(dataset_id)  # Make an API request.
            tables=self.__client.list_tables(dataset_id)
            tables_id=[]
            if tables:
                for table in list(tables):
                    tables_id.append(table.table_id)       
            return dataset,tables_id
        except NotFound:
            return None,None