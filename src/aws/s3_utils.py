# s3_utils.py

import boto3
import os

s3 = boto3.client('s3')

def upload_file_to_s3(file_path, bucket_name, s3_key):
    """
    Uploads a file to an S3 bucket.
    
    Parameters:
    file_path (str): Path to the file to be uploaded.
    bucket_name (str): Name of the S3 bucket.
    s3_key (str): S3 object key for the uploaded file.
    
    Returns:
    dict: Response from S3 after upload.
    """
    try:
        response = s3.upload_file(file_path, bucket_name, s3_key)
        print(f"File uploaded successfully to {bucket_name}/{s3_key}")
        return response
    except Exception as e:
        print(f"Error uploading file to S3: {e}")
        return None

def download_file_from_s3(s3_key, bucket_name, download_path):
    """
    Downloads a file from an S3 bucket.
    
    Parameters:
    s3_key (str): S3 object key for the file to download.
    bucket_name (str): Name of the S3 bucket.
    download_path (str): Local path where the downloaded file will be saved.
    
    Returns:
    None
    """
    try:
        with open(download_path, 'wb') as f:
            s3.download_fileobj(bucket_name, s3_key, f)
        print(f"File downloaded successfully from {bucket_name}/{s3_key}")
    except Exception as e:
        print(f"Error downloading file from S3: {e}")
