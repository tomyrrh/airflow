from airflow.models.dag import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *", # 분 시 일 월 요일
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"), #UTC: 세계 표준시 - 한국보다 9시간 느림
    catchup=False, # 돌리는 시간 기준 시작 시간이 더 빠를 경우, 누락 데이터 같이 돌릴 지 말 지 여부 결정(True일 경우, 순차적으로 도는 것이 아닌 누락 데이터 한꺼번에 돌아감)
    # dagrun_timeout=datetime.timedelta(minutes=60), # 60분이상 돌 경우 실패 처리 
    # tags=["example", "example2"], # tag를 눌렀을 때 해당 tag들만 filtering 가능
    # params={"example_key": "example_value"}, # task들에 공통적으로 넘겨줄 인자
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1", # graph에 표시되는 값(찾기 쉽게 task명과 일치시키기)
        bash_command="echo whoami",
    )
    bash_t2 = BashOperator(
        task_id="bash_t2", # graph에 표시되는 값(찾기 쉽게 task명과 일치시키기)
        bash_command="echo $HOSTNAME",
    )
    bash_t1 >> bash_t2