ARG AIRFLOW_BASE_IMAGE="apache/airflow:2.0.0-python3.8"
FROM ${AIRFLOW_BASE_IMAGE}
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt
