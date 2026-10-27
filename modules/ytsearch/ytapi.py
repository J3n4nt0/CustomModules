import requests , json
from dotenv import load_dotenv
import os 

load_dotenv()

API_KEY = os.environ.get("YT_API_KEY")

def search(query : str, maxResult: int = 10):
    global API_KEY

    API_KEY = API_KEY
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {"part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": maxResult,
        "key": API_KEY
    }
    try:
        r = requests.get(url, params=params)
        return {
            "data": r.json(),
            "status": r.status_code,
            "ok": r.ok
            }
    except Exception as e:
        return {
                "Exception_error ": e, 
                "status": None
                }
