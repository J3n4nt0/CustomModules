from fastapi import FastAPI, Header
import uvicorn
from pydantic import BaseModel
from webhook.notif_alert import send_alert_discord

app = FastAPI()

class Alert(BaseModel):
    level: str
    message: str

@app.post("/alert")
def alert(
    alert: Alert,
    x_device_name: str = Header(default="Unknown Device", alias="X-Device-Name"),
):
    send_alert_discord(alert.level, alert.message, x_device_name)
    return {"ok": True}

if __name__ == "__main__":
    uvicorn.run("test:app", port=5000, host="0.0.0.0", reload=True)
