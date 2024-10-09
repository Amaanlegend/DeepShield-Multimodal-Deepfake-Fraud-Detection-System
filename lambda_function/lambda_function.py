# lambda_function.py

import json
import boto3

def lambda_handler(event, context):
    """
    AWS Lambda handler to trigger processing when a new file is uploaded to S3.
    
    Parameters:
    event (dict): The event that triggered the Lambda function (usually S3 object creation).
    context (object): Information about the execution context.
    
    Returns:
    dict: A response with the processing status.
    """
    s3_client = boto3.client('s3')
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    try:
        # Process the file (deepfake detection, etc.)
        print(f"Processing file from S3: {bucket_name}/{object_key}")
        
        # Here, you would call the detection model (e.g., detect_deepfake(s3_key, bucket_name))
        result = "File processed successfully"  # Placeholder
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': result})
        }
    except Exception as e:
        print(f"Error processing file: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
