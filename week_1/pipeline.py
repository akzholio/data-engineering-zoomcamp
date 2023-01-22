import requests
from prefect import flow, task


@task
def download_taxi_data():
    pass


@task
def read_csv_with_pandas():
    pass


@task
def generate_postgres_ddl():
    pass


@task
def ingest_csv_data_in_chunks():
    pass


@flow
def ingest_ny_taxi_data_to_postgres(url):
    download_taxi_data()
    read_csv_with_pandas()
    generate_postgres_ddl()
    return requests.get(url).json()
