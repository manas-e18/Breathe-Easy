import os
import requests
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1/"
    "models/gemini-2.5-flash:generateContent"
)

def get_route_plan(location: str, distance: float) -> str:
    if not GEMINI_API_KEY:
        return "Gemini API key not found. Set GEMINI_API_KEY in .env."

    prompt = f"""
You are an AI assistant helping runners avoid polluted areas.

Location: {location}
Distance: {distance} km

Tasks:
- Recommend a safe and pleasant running route
- Prefer greener, low-traffic areas
- Avoid polluted or industrial zones
- Give a brief justification based on air quality
"""

    try:
        response = requests.post(
            GEMINI_URL,
            params={"key": GEMINI_API_KEY},
            headers={"Content-Type": "application/json"},
            json={
                "contents": [
                    {
                        "parts": [
                            {"text": prompt}
                        ]
                    }
                ]
            },
            timeout=30
        )

        data = response.json()

        if "candidates" not in data:
            return f"Gemini error response: {data}"

        return data["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:
        return f"Backend exception: {str(e)}"
