import boto3

def lambda_handler(event, context):
    sqs = boto3.resource("sqs")
    return get_success(create_request(event, sqs))

def get_success(status):
    if status == True:
        return {
            'statusCode': 200,
            'body': "Success"
        }
    return {
        'statusCode' : 200,
        'body' : "Failure"
    }

def create_request(request, sqs):
    try:
        queue = sqs.get_queue_by_name(QueueName="cs5250-requests")
        queue.send_message(MessageBody=str(request).replace("'", "\""))
        return True
    except Exception as e:
        print(e)
        return False
