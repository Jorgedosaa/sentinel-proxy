from fastapi import FastAPI
from pydantic import BaseModel
from app.core.scanner import scanner
from app.core.llm_client import llm_client # Import our new client

app = FastAPI(title="Sentinel Security Proxy")

class PromptInput(BaseModel):
    message: str

@app.post("/v1/proxy/ask")
async def ask_gemini(input_data: PromptInput):
    """
    Security Proxy: Analyze -> Filter -> Forward to Gemini.
    """
    # 1. Security Check
    findings = scanner.scan_text(input_data.message)
    
    if len(findings) > 0:
        return {
            "status": "REJECTED",
            "reason": "Security Policy Violation: PII detected",
            "findings": findings
        }
    
    # 2. Forward to Gemini if safe
    ai_response = await llm_client.get_completion(input_data.message)
    
    return {
        "status": "SUCCESS",
        "data": {
            "prompt": input_data.message,
            "response": ai_response
        }
    }