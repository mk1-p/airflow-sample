# Airflow Sample
인프런 강의 및 개인 공부에 대한 샘플 코드 공간입니다.

## Env
* MacOS(Sonoma, M1 MacSilicon)
* Docker version 20.10.22
* Python 3.9

## Install
### Use Docker Compose File
```
$ docker compose up -d
```
if use local env, Install venv in Test Base
* MacOS
```
$ python -m venv [your-local-airflow-root-path]/venv
$ source [your-local-airflow-root-path]venv/bin/activate
```
* Windows
```
$ python -m venv [your-local-airflow-root-path]/venv
$ Scripts\activate.bat
```

### Email Operator Setting (SMTP)
input your smtp information in your docker-compose.yaml
```
    AIRFLOW__SMTP__SMTP_HOST: 'smtp.gmail.com'
    AIRFLOW__SMTP__SMTP_USER: '${your_account}@gmail.com'
    AIRFLOW__SMTP__SMTP_PASSWORD: '${app_password}'
    AIRFLOW__SMTP__SMTP_PORT: '587'
    AIRFLOW__SMTP__SMTP_MAIL_FROM: '{your_account}@gmail.com'
```

### .env File
add python path to plugins dir for local code test
because aiflow container default path is plugins

```
AIRFLOW_UID=[your-id-number]

WORKSPACE_FOLDER=[your-venv-path] # ex, ~/Airflow

PYTHONPATH=${WORKSPACE_FOLDER}/plugins
```
