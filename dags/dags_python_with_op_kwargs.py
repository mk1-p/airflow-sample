from airflow import DAG
import datetime
import pendulum
from airflow.operators.python import PythonOperator
from common.common_func import regist2

with DAG(
    dag_id="dags_python_with_op_args",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    regist_t2 = PythonOperator(
        task_id="regist_t2",
        python_callable=regist2,
        op_args=['mk1', 'man', 'kr', 'seoul'],  # regist 에 들어갈 값을 op_args 에 인자를 리스트 형태로 넘겨준다.
        op_kwargs={'email': 'sample@gmail.com', 'phone': '010-1234-5678'} # 딕셔너리 형태로 입력을 한다.
    )

    regist_t2