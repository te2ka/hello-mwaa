import os

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

with DAG(dag_id='execute_shell', default_args=args, tags=['sample'], start_date=days_ago(1)) as dag:
    step1 = BashOperator(task_id='task1', bash_command='sample.sh --date {{ execution_date }}')

    step2 = BashOperator(task_id='task2', bash_command='sample.sh --date {{ execution_date }} -- --param1 test')

    step1 >> step2
