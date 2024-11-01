from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'andresbasilea',
    'start_date': datetime(2024, 10, 31)
}

def get_data():
    import json
    import requests

    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]
    return res

def format_data(res):
    data = {}
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['email'] = res['email']
    data['username'] = res['login']['username'] 
    data['picture'] = res['picture']['medium']
    
    return data

def stream_data():
    import json
    res = get_data()
    res = format_data(res)
    print(json.dumps(res, indent=3))


# with DAG('automation_user', 
#          default_args=default_args,
#          schedule_interval='@daily',
#          catchup=False) as dag:
    
#     streaming_task = PythonOperator(
#         task_id = 'stream_data_from_api',
#         python_callable=stream_data
#     )

stream_data()