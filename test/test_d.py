from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from test import app

client = TestClient(app)

def test_alert_success():
    """Test successful alert delivery without sending a real request to Discord."""
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
    """Test that missing required fields properly return HTTP 422 Unprocessable Entity."""
    response = client.post("/alert", json={"level": "info"})
    assert response.status_code == 422
