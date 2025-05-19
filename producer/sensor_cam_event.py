from dataclasses import dataclass, asdict

@dataclass
class SensorCamEvent:
    sensor_id: str
    timestamp: str
    motion_detected: bool
    faces_detected: int
    battery: float
    room: str

    def to_dict(self):
        return asdict(self)
