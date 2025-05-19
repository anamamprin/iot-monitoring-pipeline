import os
from consumer import Consumer

def consume_events():
    consumer = Consumer(topic='camera_events', bootstrap_servers=os.getenv("BOOTSTRAP_SERVERS"), mongo_uri=os.getenv("MONGO_URI"))
    print("Starting to consume events...")
    consumer.consume()

def main():
   consume_events()

if __name__ == "__main__":
   main()