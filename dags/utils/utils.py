import os

from airflow.hooks.S3_hook import S3Hook


def _local_to_s3(
    bucket_name: str, key: str, file_name: str, remove_local: bool = False
) -> None:
    my_conn_id = 'my_aws_conn'
    s3 = S3Hook(my_conn_id)
    s3.load_file(
        filename=file_name, bucket_name=bucket_name, replace=True, key=key
    )
    if remove_local:
        if os.path.isfile(file_name):
            os.remove(file_name)
