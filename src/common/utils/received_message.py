import os
import logging
from src.gcp.bigquery import BigQueryConnector
from src.queries.select_dataset_query import select_dataset

def get_dataset_bigquery():
    """Process Bigquery loggic"""
    try:
        logging.info(f' Access to bigquery')
        project_id = os.environ['PROJECT_ID']
        environment = os.environ['ENVIRONMENT']
        dataset = os.environ['DATASET']
        connector = BigQueryConnector(project_id, dataset, environment)
        return connector.execute_query(select_dataset())
    except Exception as e:
        raise Exception(f'[Bigquery Sap Hanna Error]: {str(e)}')
