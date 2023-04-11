ARG AIRFLOW_BASE_IMAGE="apache/airflow:2.2.0-python:3.7-slim-bullseye"
FROM ${AIRFLOW_BASE_IMAGE}
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt
