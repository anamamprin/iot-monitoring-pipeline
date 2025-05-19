from datetime import datetime
import random
from faker import Faker

fake = Faker()

def generate_camera_event() -> dict:
    return {
        "camera_id": fake.uuid4(),
        "timestamp": datetime.now().isoformat(),
        "motion_detected": random.choice([True, False]),
        "faces_detected": random.randint(0, 3),
        "sound_detected": random.choice([True, False]),
        "battery": round(random.uniform(20.0, 100.0), 2),
        "room": "Living Room"
    }


