from airflow import DAG
from airflow.operators.python import PythonOperator
import logging


def helloWorld():
    logger = logging.getLogger(__name__)
    logger.info("Hello World")


with DAG(dag_id="test_dag",
         schedule_interval=None,
         ) as dag:

    task1 = PythonOperator(
        task_id="hello_world",
        python_callable=helloWorld,
        dag=dag)

    task1
