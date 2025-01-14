from airflow import DAG
from airflow.operators.python import PythonOperator


def helloWorld():
    print("Hello World")


with DAG(dag_id="hello_world_dag",
         schedule_interval=None,
         ) as dag:

    task1 = PythonOperator(
        task_id="hello_world",
        python_callable=helloWorld,
        dag=dag)

    task1
