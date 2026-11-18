
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_valid_prediction():
    response = client.post(
        "/predict",
        json={
            "pottery_load": 100,
            "temperature": 900,
            "moisture": 8,
            "duration": 6,
            "insulation": 0.9,
            "kiln_volume": 2,
            "ambient_temp": 25
        }
    )

    assert response.status_code == 200
    assert response.json()["predicted_energy_kwh"] >= 0

def test_invalid_input():
    response = client.post(
        "/predict",
        json={
            "pottery_load": -100,
            "temperature": 900,
            "moisture": 8,
            "duration": 6,
            "insulation": 0.9,
            "kiln_volume": 2,
            "ambient_temp": 25
        }
    )

    assert response.status_code == 422
