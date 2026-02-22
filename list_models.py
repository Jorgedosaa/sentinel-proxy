import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


def list_my_models():
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    print("--- Available Models in your Gemini account ---")
    try:
        # List models to see the exact name expected by the API
        for m in client.models.list():
            print(
                f"ID: {m.name} | Supports GenerateContent: {'generateContent' in m.supported_methods}"
            )
    except Exception as e:
        print(f"Error listing models: {e}")


if __name__ == "__main__":
    list_my_models()
