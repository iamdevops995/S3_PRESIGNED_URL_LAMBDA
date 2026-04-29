import json
import boto3
import os

s3 = boto3.client('s3')
BUCKET = "my-presigned-demo-bucket"

def lambda_handler(event, context):
    file_name = event.get("queryStringParameters", {}).get("fileName", "test.txt")

    url = s3.generate_presigned_url(
        ClientMethod='put_object',
        Params={
            'Bucket': BUCKET,
            'Key': file_name
            # 'ContentType': 'application/octet-stream'
        },
        ExpiresIn=300
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'uploadUrl': url})
    }
