FROM apache/airflow:3.3.0

COPY requirements/base.txt /tmp/base.txt

USER airflow

RUN pip install --no-cache-dir -r /tmp/base.txt