from dataclasses import dataclass

@dataclass
class SensorCamEvent:
    sensor_id: str
    timestamp: str
    motion_detected: bool
    faces_detected: int
    battery: float
    room: str
