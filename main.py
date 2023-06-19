import boto3

def lambda_handler(event, context):

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    # Create an SNS client
    sns_client = boto3.client('sns')
    s3_client = boto3.client('s3')

    url = s3_client.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': object_key},
        ExpiresIn=86400
    )


    print(url)
    sns_client.publish(
        TopicArn='<SNS_TOPIC_ARN>', 
        Message=f"""
        Hi,
        
        Your Scan report is generated and saved in the bucket.
        
        You can check your report here - {url}
        
        """ 
    )
