from airflow import DAG
import datetime
import pendulum
from airflow.decorators import task

with DAG(
    dag_id="dags_show_templates",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2023, 12, 1, tz="Asia/Seoul"), # 시작 시간
    catchup=True
) as dag:

    @task(task_id='python_task')
    def show_templates(**kwargs):
        from pprint import pprint
        pprint(kwargs)

    show_templates()