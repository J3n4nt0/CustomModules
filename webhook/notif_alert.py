import os
import requests
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()  # Charge le fichier .env

DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK")

def send_alert_discord(
    level: str, 
    message: str, 
    x_device_name: str
):
    if not DISCORD_WEBHOOK_URL:
        raise HTTPException(status_code=500, detail="DISCORD_WEBHOOK environment variable is not configured")

    color_map = {
        "info": 3066993,
        "warning": 15105570,  
        "critical": 15158332  
    }
    
    emoji_map = {"info": "ℹ️", "warning": "⚠️", "critical": "🚨"}
    
    emoji = emoji_map.get(level.lower(), "ℹ️")
    color = color_map.get(level.lower(), 3447003)

    discord_payload = {
        "username": "Central Alert Bot",
        "embeds": [{
            "title": f"{emoji} {level.upper()}",
            "description": message,
            "footer": {"text": f"From: {x_device_name}"},
            "color": color
        }]
    }

    try:
        r = requests.post(DISCORD_WEBHOOK_URL, json=discord_payload, timeout=5)
        r.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to connect to Discord: {str(e)}")
