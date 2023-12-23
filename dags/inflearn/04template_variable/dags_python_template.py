from airflow import DAG
import datetime
import pendulum
from airflow.decorators import task
from airflow.operators.python import PythonOperator

with DAG(
    dag_id="dags_python_template",
    schedule="30 9 * * *",
    tags=['template variable'],
    start_date=pendulum.datetime(2023, 12, 1, tz="Asia/Seoul"), # 시작 시간
    catchup=False
) as dag:

    def python_function1(start_date, end_date, **kwargs):
        print(start_date)
        print(end_date)

    python_t1 = PythonOperator(
        task_id='python_t1',
        python_callable=python_function1,
        op_kwargs={'start_date':'{{data_interval_start | ds}}', 'end_date':'{{data_interval_end | ds}}'}
    )

    @task(task_id='python_t2')
    def python_function2(**kwargs):
        print(kwargs)
        print('ds:' + kwargs['ds'])
        print('ts:' + kwargs['ts'])
        print('data_interval_start:' + str(kwargs['data_interval_start']))
        print('data_interval_end:' + str(kwargs['data_interval_end']))
        print('task_instance:' + str(kwargs['ti']))


    # decorator를 사용하는 경우, 메소드를 사용하면 된다.
    python_t1 >> python_function2()