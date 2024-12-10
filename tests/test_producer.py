from producer import get_success, create_request
from unittest.mock import patch

class mock_sqs:
    def __init__(self):
        self.queue = mock_queue()

    def get_queue_by_name(self, QueueName):
        return self.queue
    
class mock_queue:
    def __init__(self):
        self.data = None

    def send_message(self, MessageBody):
        self.data = MessageBody


def test_get_success():
    assert get_success(True) == {
            'statusCode': 200,
            'body': "Success"
        }
    assert get_success(False) == {
        'statusCode' : 200,
        'body' : "Failure"
    }

def test_create_request():
    event = {'value' : 'name', 'expert' : "something"}
    sqs = mock_sqs()
    create_request(event, sqs)
    assert sqs.queue.data == '{\"value\": \"name\", \"expert\": \"something\"}'