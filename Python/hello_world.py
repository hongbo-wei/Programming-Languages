# AWS Lambda function that returns a simple "Hello World!" message
def lambda_heandler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello World!'
    }