from kafka import KafkaProducer
import json

class Producer:
    def __init__(self, topic: str, bootstrap_servers: str):
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda x: json.dumps(x).encode('utf-8')
        )

    def send_message(self, message: dict):
        self.producer.send(self.topic, value=message)
        self.producer.flush()
