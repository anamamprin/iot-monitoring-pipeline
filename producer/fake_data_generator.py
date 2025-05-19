from faker import Faker
from sensor_cam_event import SensorCamEvent

fake = Faker()

def generate_camera_event() -> SensorCamEvent:
    return SensorCamEvent(
        sensor_id=fake.uuid4(),
        timestamp=fake.date_time_between(start_date="-60d", end_date="now").isoformat(),
        motion_detected=fake.boolean(chance_of_getting_true=50),
        faces_detected=fake.random_int(0, 5),
        battery=round(fake.pyfloat(min_value=15.0, max_value=100.0), 2),
        room=fake.random_element(elements=("Living Room", "Bedroom", "Kitchen", "Garage")),
    )
