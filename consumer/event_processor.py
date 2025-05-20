from datetime import datetime
from typing import Optional

class EventProcessor:
    @staticmethod
    def extract_hour(timestamp: str) -> Optional[int]:
        try:
            return datetime.fromisoformat(timestamp).hour
        
        except (ValueError, TypeError):
            return None

    @staticmethod
    def analyse_event_risk(event: dict) -> dict:
        timestamp = event.get("timestamp")
        hour = EventProcessor.extract_hour(timestamp)

        if hour is None:
            event["risk_level"] = "IMPRECISO"
            return event

        is_night = 0 <= hour < 6
        motion = event.get('motion_detected', False)
        faces = event.get('faces_detected', 0)

        if motion and faces > 0 and is_night:
            risk = "ALTISSIMO"
        elif motion and faces > 0:
            risk = "ALTO"
        elif motion:
            risk = "MEDIO"
        else:
            risk = "BAIXO"

        event["risk_level"] = risk
        return event

    @staticmethod
    def check_battery_conditions(event: dict) -> dict:
        battery = event.get('battery')
        if battery >= 50.0:
            battery_status = 'OK'
        elif battery >= 20.0:
            battery_status = 'LOW'
        else:
            battery_status = 'CRITICAL'

        event['battery_status'] = battery_status
        return event
