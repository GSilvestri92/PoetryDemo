from bq_client.bigquery_table import BigQueryTable
from bq_client.bigquery_dataset import BigQueryDataset

t=BigQueryTable("training-gcp-309207.dataset_1.company_ris")
print(t.get_project_name())
print(t.get_dataset_name())
print(t.get_table_name())
print(t.get_schema())
print(t.get_description())
print(t.get_rows())

d=BigQueryDataset("training-gcp-309207.dataset_1")
print(d.get_project_name())
print(d.get_dataset_name())
print(d.get_tables())
print(d.get_labels())
