from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator",    # 실질적인 DAG 네임이 되는 부분, 명칭을 일치해주는게 좋음
    schedule="0 0 * * *",           # 크론 스케쥴 타임
    start_date=pendulum.datetime(2023, 1, 1, tz="Asia/Seoul"), # 시작 시간
    catchup=False,                  # start_date 와 현재 시간과의 공백 시간에 대한 스케쥴을 실행할 것인지
    # dagrun_timeout=datetime.timedelta(minutes=60),  # dag가 실행 도중 설정 값을 넘어가는 경우 실패
    # tags=["example", "example2"],   # 단순 tag 기능
    tags=['basic operator'],
    params={"example_key": "example_value"} # task에 공통적으로 들어가는 파라메터 묶음

) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",   # web ui 상 나타나는 테스크 이름, 객체명이랑 일치 시키는게 관례이다.
        bash_command="echo who am i"
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",  # web ui 상 나타나는 테스크 이름, 객체명이랑 일치 시키는게 관례이다.
        bash_command="echo $HOSTNAME"
    )

    bash_t1 >> bash_t2

