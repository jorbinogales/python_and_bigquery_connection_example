import logging
import functions_framework
from src.common.utils.received_message import get_dataset_bigquery


@functions_framework.http
def my_function(request):
    "This is the main function"
    try:
        logging.info('Iniciando la funcion my_function()')
        get_dataset_bigquery()
    except Exception as e:
        logging.error(f'[ERROR]: {str(e)}')
        raise Exception(f'[ERROR]: {str(e)}')
    finally:
        logging.info("Saliendo de la función my_function()")
    return "Bigquery Connect suceessfull"
