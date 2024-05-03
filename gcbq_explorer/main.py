from bq_client.bigquery_table import BigQueryTable
from bq_client.bigquery_dataset import BigQueryDataset
import sys
import logging as log
import click

def table_exists(table_id):
    table=BigQueryTable(table_id)
    if table.get_project_name() is not None:
        return table
    return None

def dataset_exists(dataset_id):
    dataset=BigQueryDataset(dataset_id)
    if dataset.get_project_name() is not None:
        return dataset
    return None

@click.command()
@click.option('--id',
              required=True,
              help='Full table id. Format: project.dataset.table')
@click.option('--verbosity',
              default='INFO',
              help='Set logging level')
def print_table_properties(table_id,verbosity):

    log.basicConfig(
    format='%(asctime)s -- %(levelname)s:%(message)s',
    level=str(verbosity).upper(),
    datefmt='%Y-%m-%d %H:%M:%S',
    stream=sys.stdout)

    log.info("Requesting table '{}' ".format(table_id))
    table=table_exists(table_id)
    log.debug("Result is object '{}' ".format(table))

    if table is None:
        print("Table does not exist")
    else:
        print("Project: {}".format(table.get_project_name()))
        print("Dataset: {}".format(table.get_dataset_name()))
        print("Table: {}".format(table.get_table_name()))
        print("Schema: {}".format(table.get_schema()))
        print("Description: {}".format(table.get_description()))
        print("Rows: {}".format(table.get_rows()))

@click.command()
@click.option('--id',
              required=True,
              help='Full dataset id. Format: project.dataset')
@click.option('--verbosity',
              default='INFO',
              help='Set logging level')
def print_dataset_properties(dataset_id,verbosity):

    log.basicConfig(
    format='%(asctime)s -- %(levelname)s:%(message)s',
    level=str(verbosity).upper(),
    datefmt='%Y-%m-%d %H:%M:%S',
    stream=sys.stdout)

    log.info("Requesting dataset '{}' ".format(dataset_id))
    dataset=table_exists(dataset_id)
    log.debug("Result is object '{}' ".format(dataset))

    if dataset is None:
        print("Dataset does not exist")
    else:
        print("Project: {}".format(dataset.get_project_name()))
        print("Dataset: {}".format(dataset.get_dataset_name()))
        print("Tables: {}".format(dataset.get_tables()))
        print("Labels: {}".format(dataset.get_labels()))


print_table_properties("training-gcp-309207.dataset_1.company_ris")


t=BigQueryTable("training-gcp-309207.dataset_1.company_ris")
print(t.get_project_name())
print(t.get_dataset_name())
print(t.get_table_name())
print(t.get_schema())
print(t.get_description())
print(t.get_rows())


print_dataset_properties("training-gcp-309207.dataset_1")

d=BigQueryDataset("training-gcp-309207.dataset_1")
print(d.get_project_name())
print(d.get_dataset_name())
print(d.get_tables())
print(d.get_labels())

