from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_with_template",
    schedule="10 0 * * *",
    tags=['template variable'],
    start_date=pendulum.datetime(2023, 1, 1, tz="Asia/Seoul"), # 시작 시간
    catchup=False
) as dag:
    # Jinja Template
    # data_interval_start 이전 배치일
    # data_interval_end 현재 배치 작업되고 있는 일자
    # | ds  날짜 포멧
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command='echo "data_interval_end: {{ data_interval_end }}  "'
    )

    bash_t2 = BashOperator(
        task_id='bash_t2',
        env={
            "START_DATE": '{{data_interval_start | ds}}',
            "END_DATE": '{{data_interval_end | ds}}'
        },
        bash_command='echo $START_DATE && echo $END_DATE'
    )

    bash_t1 >> bash_t2