from kafka import KafkaConsumer
import json
from pymongo import MongoClient


class Consumer:
    def __init__(self, topic, bootstrap_servers, mongo_uri):
        self.topic = topic
        self.bootstrap_servers = bootstrap_servers
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=self.bootstrap_servers,
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        self.mongo_client = MongoClient(mongo_uri)

    def consume(self):
        db = self.mongo_client["sensors_db"]
        collection = db["events"]
        for message in self.consumer:
            print("Message received:", message.value)
            collection.insert_one(message.value)
            print("Message inserted into MongoDB:", message.value)
