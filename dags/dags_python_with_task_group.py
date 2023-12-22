from airflow import DAG
import pendulum
from airflow.decorators import task_group, task
from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup

with DAG(
    dag_id='dags_python_with_task_group',
    tags=['using task'],
    start_date=pendulum.datetime(2023,1,1),
    schedule=None,
    catchup=False
) as dag:
    def inner_func(**kwargs):
        msg = kwargs.get('msg') or ''
        print(msg)

    @task_group(group_id='first_group')
    def group_1():
        # docstring - Airflow Web UI 상에 설명으 나타낸다.
        ''' task_group decorator를 이용한 첫 번째 그룹입니다. '''

        @task(task_id='inner_function1')
        def inner_func1(**kwargs):
            print("첫 번째 TaskGroup 내 첫 번째 task입니다.")

        inner_function2 = PythonOperator(
            task_id='inner_function2',
            python_callable=inner_func,
            op_kwargs={'msg':'첫 번째 TaskGroup내 두 번째 task입니다.'}
        )

        inner_func1() >> inner_function2

    with TaskGroup(group_id='second_group', tooltip='두 번째 그룹입니다.') as group_2:
        ''' 여기에 적은 docstring은 표시되지 않습니다. '''
        @task(task_id='inner_function1')
        def inner_func1(**kwargs):
            print("두 번째 TaskGroup 내 첫 번째 task입니다.")

        inner_function2 = PythonOperator(
            task_id='inner_function2',
            python_callable=inner_func,
            op_kwargs={'msg':'두 번째 TaskGroup내 두 번째 task입니다.'}
        )

        inner_func1() >> inner_function2

    group_1() >> group_2