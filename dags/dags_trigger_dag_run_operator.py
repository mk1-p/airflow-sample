from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

with DAG(
    dag_id='dags_trigger_dag_run_operator',
    tags=['more operator'],
    start_date=pendulum.datetime(2023,1,1),
    schedule='30 9 * * *',
    catchup=False
) as dag:

    start_task = BashOperator(
        task_id='start_task',
        bash_command='echo start!'
    )

    trigger_dag_task = TriggerDagRunOperator(
        task_id='trigger_dag_task',
        trigger_dag_id='dags_python_operator',
        trigger_run_id=None,    # None 으로 설정 시, 트리거 되는 dag 의 run_id의 시작은 manual 로 지정된다.
        execution_date='{{data_interval_start}}',   # data_interval_start 값으로 지정하여 manual__{{data_interval_start}}
        reset_dag_run=True,
        wait_for_completion=False,
        poke_interval=60,
        allowed_states=['success'],
        failed_states=None
    )

    #TODO XCOM은 dag - dag 간 값 전달이 되지 않는 것인가??
    # 확인 필요!
    end_task = BashOperator(
        task_id='end_task',
        bash_command="echo {{ ti.xcom_pull(task_ids='return_value') }}"
    )

    start_task >> trigger_dag_task >> end_task