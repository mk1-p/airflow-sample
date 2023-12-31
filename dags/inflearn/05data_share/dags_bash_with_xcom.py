from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id='dags_bash_with_xcom',
    schedule='10 0 * * *',
    tags=['data share'],
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    bash_push = BashOperator(
        task_id='bash_push',
        bash_command="echo START && "
                     "echo XCOM_PUSHED "
                     "{{ ti.xcom_push(key='bash_pushed', value='first_bash_message') }} && "
                     "echo COMPLETE" # 마지막 echo 값이 return_value 로 들어간다.
    )

    bash_pull = BashOperator(
        task_id='bash_pull',
        env={'PUSHED_VALUE':"{{ ti.xcom_pull(key='bash_pushed') }}",
             'RETURN_VALUE':"{{ ti.xcom_pull(task_ids='bash_push') }}"},
        bash_command="echo $PUSHED_VALUE && echo $RETURN_VALUE ",
        do_xcom_push=False  # echo 프린트되는 내용을 xcom에 push되지 않도록 함 = return_value 로 들어가지 않음!
    )

    bash_push >> bash_pull