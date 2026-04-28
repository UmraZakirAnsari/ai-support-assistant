#  AI Customer Support Chat Assistant

##  Summary
This project is an AI-powered customer support assistant that allows users to chat directly with an AI system. It understands user queries, detects intent and urgency, and generates helpful responses. The system also supports multilingual replies (English and Arabic) and maintains conversation context.

---

## Features
- Intent detection (refund, complaint, query, unknown)
- Urgency classification (low, medium, high)
- Context-aware reply generation (not generic)
- Multi-turn conversation (chat memory)
- English + Arabic responses (user-controlled)
- Structured JSON output for backend use
- Chat-style UI for real-time interaction
- Fallback handling for edge cases

---

##  Tech Stack
- Python (FastAPI)
- OpenRouter API (LLM)
- HTML + JavaScript (Frontend)

---

##  Setup Instructions

### 1. Install dependencies

pip install -r requirements.txt

### run the server

uvicorn app:app --reload

### open the UI
http://127.0.0.1:8000/ui