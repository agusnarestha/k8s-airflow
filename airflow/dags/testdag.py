from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

default_args = {
    'start_date': datetime(2023, 1, 1),
    'retries': 0, 
}

with DAG(   
    dag_id='test-dag',
    default_args=default_args,
    catchup=False,
    schedule_interval=None,
) as dag:
    hello = BashOperator(task_id="hello", bash_command="echo hello")

    @task()
    def airflow():
        print("airflow")

    hello >> airflow()