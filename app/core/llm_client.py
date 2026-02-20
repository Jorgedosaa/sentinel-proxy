import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class GeminiClient:
    def __init__(self):
        # Configure the Google AI SDK
        api_key = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    async def get_completion(self, prompt: str) -> str:
        """
        Sends the sanitized prompt to Gemini and returns the response.
        """
        try:
            # For this MVP, we use a simple generate_content call
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error connecting to Gemini: {str(e)}"

# Global instance
llm_client = GeminiClient()