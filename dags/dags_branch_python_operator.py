from airflow import DAG
import datetime
import pendulum
from airflow.decorators import task
from airflow.operators.python import BranchPythonOperator, PythonOperator

with DAG(
    dag_id='dags_branch_python_operator',
    start_date=pendulum.datetime(2023,1,1),
    schedule=None,
    catchup=False
) as dag:
    def select_random():
        import random

        item_list = ['A','B','C']
        selected_item = random.choice(item_list)
        if selected_item == 'A':
            return 'task_a'
        elif selected_item in ['B','C']:
            return ['task_b','task_c']

    python_branch_task = BranchPythonOperator(
        task_id='python_branch_task',
        python_callable=select_random
    )

    def common_func(**kwargs):
        print(kwargs['selected'])

    task_a = PythonOperator(
        task_id='task_a',
        python_callable=common_func,
        op_kwargs={'selected':'A'}
    )

    task_b = PythonOperator(
        task_id='task_b',
        python_callable=common_func,
        op_kwargs={'selected': 'B'}
    )

    task_c = PythonOperator(
        task_id='task_c',
        python_callable=common_func,
        op_kwargs={'selected': 'C'}
    )

    # branch python operator 후행으로 나오는 테스크의 리스트를 모두 적어준다.
    # branch python operator 리턴값은 조건의 task_id 값을 stirng 으로 적어준다.
    # 여러 테스크가 수행되어야 한다면 리스트로 task_id를 적어준다.
    python_branch_task >> [task_a, task_b, task_c]