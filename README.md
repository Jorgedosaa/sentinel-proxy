# 🚀 AI Compliance & Security Sentinel

An Open-Source Security Proxy designed to intercept LLM requests and block/sanitize PII (Personally Identifiable Information) before it leaves the corporate network.

## 🛠️ Tech Stack
- **FastAPI**: High-performance API Gateway.
- **Microsoft Presidio**: PII detection using NLP and Regex.
- **Google Gemini**: Large Language Model integration.
- **Ubuntu/Linux**: Optimized for Linux environments.

## 🛡️ Features (Phase 1)
- Real-time PII Scanning (Emails, Names, Phones, etc.).
- Secure Proxying to Gemini API.
- Zero-leak policy (Credentials stored in `.env`).

## 🚀 How to run
1. Clone the repo.
2. Create a `venv` and install `requirements.txt`.
3. Set your `GOOGLE_API_KEY` in a `.env` file.
4. Run `uvicorn app.main:app --reload`.