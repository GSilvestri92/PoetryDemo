from bq_client.bigquery_client import BigQueryClient

class BigQueryDataset():

    __project_name= None
    __dataset_name= None
    __tables= None
    __labels= None

    def __init__(self,dataset_id):
        cl=BigQueryClient()
        dataset,tables=cl.get_dataset(dataset_id)
        if dataset is not None:
            self.__project_name=dataset.project
            self.__dataset_name=dataset.dataset_id
            self.__tables=tables
            self.__labels=dataset.labels


    def get_project_name(self):
        return self.__project_name
    
    def get_dataset_name(self):
        return self.__dataset_name
    
    def get_tables(self):
        return self.__tables
    
    def get_labels(self):
        return self.__labels

