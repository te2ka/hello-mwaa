from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'airflow',
}

with DAG(dag_id='sample', default_args=args, tags=['sample'], start_date=days_ago(1)) as dag:
    step1 = BashOperator(task_id='task1', bash_command='echo task1')

    step2 = BashOperator(task_id='task2', bash_command='echo task2')
    step3 = BashOperator(task_id='task3', bash_command='echo task3')

    step4 = BashOperator(task_id='task4', bash_command='echo task4')

    step1 >> [step2, step3] >> step4

