ARG AIRFLOW_BASE_IMAGE="apache/airflow:2.2.0"
FROM ${AIRFLOW_BASE_IMAGE}
COPY requirements.txt /
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt 
