from kafka import KafkaConsumer
import json
from pymongo import MongoClient, errors as pymongo_errors
from event_processor import EventProcessor


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
            try:
                event = message.value
                print("Message received:", event)

                event = EventProcessor.check_battery_conditions(event)
                event = EventProcessor.analyse_event_risk(event)

                collection.insert_one(event)
                print("Message inserted into MongoDB:", event)

            except json.JSONDecodeError:
                print("[ERROR] Failed to decode message JSON:", message )

            except Exception as e:
                print(f"[ERROR] Unexpected error while processing event: {e}")

            except pymongo_errors.PyMongoError as e:
                print(f"[ERROR] MongoDB error: {e}") 

