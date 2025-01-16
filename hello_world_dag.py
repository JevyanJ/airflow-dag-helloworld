from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
import logging


def helloWorld():
    logger = logging.getLogger(__name__)
    logger.info("Hello World")


with DAG(dag_id="test_dag",
         schedule_interval=None,
         ) as dag:

    task1 = KubernetesPodOperator(
        name="hello_world_task",
        image="python:3.7",
        task_id="hello_world",
        python_callable=helloWorld,
        dag=dag)

    task1
