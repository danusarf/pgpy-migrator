# Imports the Google Cloud client library
from google.cloud import storage

#step 2 upload dump files to gcp
def dump_to_cloud_storage(CLOUDSTORAGEBUCKET, DUMPFILE):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(CLOUDSTORAGEBUCKET)
    blob = bucket.blob(DUMPFILE)

    blob.upload_from_filename(DUMPFILE)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))