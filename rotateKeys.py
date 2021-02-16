"""
### Rotación de llaves
Tarea para disparar la rotación de llaves de expediente digital
"""
from datetime import timedelta
from airflow import DAG
import os

from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.bash import BashOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.utils.dates import days_ago


# Argumentos por defecto
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['manager@openfinance.mx'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'http_conn_id': 'URL',
    'schedule_interval': '@daily',
}

# [START instantiate_dag]
dag = DAG(
    'Rotar_Llaves',
    default_args=default_args,
    description='Dispara el proceso de rotación de llaves',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['rao'],
)

t1 = BashOperator( 
    task_id='rotate_keys',
    bash_command='curl -k -X POST http://console-service/api/minio/rotate',
    dag=dag,
)

dag.doc_md = __doc__

t1.doc_md = """\
#### Task Documentation
Tarea simple que dispara el proceso de rotación de llaves,
Ésta tarea no conoce ningún detalle del proceso de rotación de llaves y solo es utilizada como disparador de evento
"""


#task_post_op
t1