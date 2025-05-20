import pytest
from consumer.event_processor import EventProcessor

@pytest.mark.parametrize("event, expected_risk", [
    ({"timestamp": "2024-05-20T01:00:00", "motion_detected": True, "faces_detected": 2}, "ALTISSIMO"),
    ({"timestamp": "2024-05-20T10:00:00", "motion_detected": True, "faces_detected": 2}, "ALTO"),
    ({"timestamp": "2024-05-20T22:00:00", "motion_detected": True, "faces_detected": 0}, "MEDIO"),
    ({"timestamp": "2024-05-20T12:00:00", "motion_detected": False, "faces_detected": 3}, "BAIXO"),
    ({"timestamp": None, "motion_detected": False, "faces_detected": 3}, "IMPRECISO"),
    ({"timestamp": "invalid-timestamp", "motion_detected": True, "faces_detected": 1}, "IMPRECISO"),
])

def test_analyse_event_risk(event, expected_risk):
    result = EventProcessor.analyse_event_risk(event.copy())
    assert result["risk_level"] == expected_risk

@pytest.mark.parametrize("event, expected_status", [
    ({"battery": 75.0}, "OK"),
    ({"battery": 45.0}, "LOW"),
    ({"battery": 10.0}, "CRITICAL"),
])
def test_check_battery_conditions(event, expected_status):
    result = EventProcessor.check_battery_conditions(event.copy())
    assert result["battery_status"] == expected_status

@pytest.mark.parametrize("timestamp, expected_hour", [
    ("2024-05-20T13:45:00", 13),        
    ("not-a-timestamp", None),           
    ("", None),                           
    (None, None),                         
])
def test_extract_hour(timestamp, expected_hour):
    result = EventProcessor.extract_hour(timestamp)
    assert result == expected_hour
