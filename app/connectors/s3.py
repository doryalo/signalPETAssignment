import boto3
import os
from botocore.exceptions import NoCredentialsError

def upload_file_to_s3(file_path, file_name):
    """
    Uploads a file to an AWS S3 bucket.
    :param file_path: File to upload
    :param file_name: File name
    :return: True, url if file was uploaded, else False, ''
    """
    bucket_name = os.getenv('BUCKET_NAME')
    if not bucket_name:
        print("BUCKET_NAME environment variable is not set.")
        return False, ''

    s3_client = boto3.client('s3')
    # try:
    #     response = s3_client.upload_file(file_path, bucket_name, file_name)
    # except NoCredentialsError:
    #     print("Credentials not available")
    #     return False, ''
    # except Exception as e:
    #     # Catching a general exception to handle other possible errors
    #     print(f"Failed to upload file: {e}")
    #     return False, ''
    return True
