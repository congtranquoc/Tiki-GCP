from google.cloud import bigquery
import os

def load_data_to_bigquery(event, context):
    bucket = event['bucket']
    file_name = event['name']

    project_id = "my-project-25072023-393906"
    dataset_id = "tiki-dataset"
    table_id = "tiki-products"

    client = bigquery.Client(project=project_id)

    source_uri = f"gs://{bucket}/{file_name}"



    # Tạo job load dữ liệu từ GCS vào BigQuery
    job_config = bigquery.LoadJobConfig(
        autodetect=True,
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    )

    table_ref = client.dataset(dataset_id).table(table_id)
    job = client.load_table_from_uri(
        source_uri, table_ref, job_config=job_config
    )

    job.result()
    )

    job.result()
    print(f"Data loaded from {source_uri} to BigQuery table {table_id}")