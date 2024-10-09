# rekognition.py

import boto3

def analyze_image_with_rekognition(image_path):
    """
    Use AWS Rekognition to analyze an image.
    
    Parameters:
    image_path (str): Path to the image to be analyzed.
    
    Returns:
    dict: Rekognition analysis result.
    """
    client = boto3.client('rekognition')
    
    with open(image_path, 'rb') as image:
        response = client.detect_faces(Image={'Bytes': image.read()}, Attributes=['ALL'])
        
    return response
