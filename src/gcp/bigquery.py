from google.cloud import bigquery
import logging

logger = logging.getLogger(__name__)


class BigQueryConnector:

    project_id: str
    dataset: str
    environment: str

    def __init__(
            self,
            project_id,
            dataset,
            environment
    ):
        self.project_id = project_id
        self.dataset = dataset
        self.environment = environment

    def execute_query(self, query):
        """Function that execute a sql query and return and json resposne"""
        logging.info('Executing SQL in Bigquery')
        client = bigquery.Client(project=self.project_id)
        query_job = client.query(query)
        query_job.result()
        result_df = query_job.to_dataframe()
        return result_df.to_dict(orient='records')
