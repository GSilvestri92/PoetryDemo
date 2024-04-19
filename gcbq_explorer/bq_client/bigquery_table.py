from bq_client.bigquery_client import BigQueryClient

class BigQueryTable():

    __project_name= None
    __dataset_name= None
    __table_name= None
    __schema= None
    __description= None
    __rows= None

    def __init__(self,table_id):
        cl=BigQueryClient()
        table=cl.get_table(table_id)
        if table is not None:
            self.__project_name=table.project
            self.__dataset_name=table.dataset_id
            self.__table_name=table.table_id
            self.__schema=table.schema
            self.__description=table.description
            self.__rows= table.num_rows

    def get_project_name(self):
        return self.__project_name
    
    def get_dataset_name(self):
        return self.__dataset_name
    
    def get_table_name(self):
        return self.__table_name
    
    def get_schema(self):
        return self.__schema
    
    def get_description(self):
        return self.__description
    
    def get_rows(self):
        return self.__rows
    
