from airflow import DAG
import pendulum
from airflow.decorators import task
from airflow.operators.python import PythonOperator
from airflow.operators.branch import BaseBranchOperator

with DAG(
    dag_id='dags_base_branch_operator',
    start_date=pendulum.datetime(2023,1,1),
    schedule=None,
    catchup=False
) as dag:
    # CustomBranchOperator 자식클래스, BaseBranchOperator 부모클래스
    # 상속 받은 후 choose_branch(self, context) 메소드를 Override 하여 분기 되는 task id 정의
    class CustomBranchOperator(BaseBranchOperator):
        # 메소드 명은 꼭 choose_branch 로 정의와 context 파라메터를 빼지 않아야한다.
        # context 는 기본 파라메터를 제공해준다. ex, data_interval_start
        def choose_branch(self, context):
            import random

            item_list = ['A', 'B', 'C']
            selected_item = random.choice(item_list)
            if selected_item == 'A':
                return 'task_a'
            elif selected_item in ['B', 'C']:
                return ['task_b', 'task_c']

    custom_branch_operator = CustomBranchOperator(task_id='python_branch_task')

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

    custom_branch_operator >> [task_a, task_b, task_c]