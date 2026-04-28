
from dotenv import load_dotenv
load_dotenv()
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import requests
import json

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import os

API_KEY = os.getenv("OPENROUTER_API_KEY")


@app.get("/ui", response_class=HTMLResponse)
def serve_ui():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.get("/analyze")
def analyze_email(text: str, lang: str = "both"):

    prompt = f"""
You are an AI customer support assistant.

Analyze the email and return ONLY valid JSON:

{{
  "intent": "refund | complaint | query | unknown",
  "urgency": "low | medium | high",
  "category": "...",
  "confidence": 0 to 1,
  "reply_en": "...",
  "reply_ar": "..."
}}

Instructions:
- Understand the issue clearly.

- If lang = "en": generate ONLY English reply, leave reply_ar empty.
- If lang = "ar": generate ONLY Arabic reply, leave reply_en empty.
- If lang = "both": generate both English and Arabic replies.

- Do NOT return "...".
- Keep replies relevant to the issue.

Strict JSON only.

Email:
{text}

Language preference:
{lang}
"""

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-3.5-turbo",
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
        )

        data = response.json()

        
        content = data["choices"][0]["message"]["content"]

     
        parsed = json.loads(content)

        return parsed

    except Exception as e:
        return {"error": str(e)}
