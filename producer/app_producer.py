from fake_data_generator import generate_camera_event
from producer import Producer
import os

def generate_events():
    print("Generating events...")
    events_list = []
    for _ in range(20):
        event = generate_camera_event()
        print(f"Generated event: {event}")
        events_list.append(event)
    return events_list

def send_events(events_list):
    producer = Producer(topic='camera_events', bootstrap_servers=os.getenv("BOOTSTRAP_SERVERS"))
    for event in events_list:
        print(f"Sending event: {event}")
        producer.send_message(event.to_dict())

def main():
   events = generate_events()
   send_events(events)

if __name__ == "__main__":
   main()
