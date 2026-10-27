from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_alert_success():
    with patch("webhook.notif_alert.requests.post") as mock_post:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        response = client.post(
            "/alert",
            json={"level": "info", "message": "Test alert message"},
            headers={"X-Device-Name": "CI-Runner"}
        )

        assert response.status_code == 200
        assert response.json() == {"ok": True}
        assert mock_post.called

def test_alert_invalid_payload():
    response = client.post("/alert", json={"level": "info"})
    assert response.status_code == 422

def test_awk():
    from awk.awk import awk
    columns = awk("../LICENSE" , 1)
    assert len(columns) == 21

def test_ytapi():
    from ytsearch.ytapi import search
    data = search("hello")
    assert data["status"] == 200

