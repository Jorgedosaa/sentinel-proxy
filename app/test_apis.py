import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


def test_gemini_v2():
    print("--- Testing Gemini (Final Attempt) ---")
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        print("Error: GOOGLE_API_KEY not found in .env")
        return

    client = genai.Client(api_key=api_key)

    try:
        # 1. Dynamically search for the exact model name to avoid 404 errors
        target_model = "gemini-1.5-flash-001"  # More specific default
        try:
            detected = None
            print("🔎 Listing available models...")
            for m in client.models.list():
                # Get model name robustly
                name = (
                    getattr(m, "name", None)
                    or getattr(m, "model", None)
                    or getattr(m, "id", None)
                    or str(m)
                )

                # Try to get supported methods (varies between versions)
                methods = None
                try:
                    methods = getattr(m, "supported_generation_methods", None)
                except Exception:
                    methods = None

                # If it is dict-like, try other keys
                try:
                    if methods is None and isinstance(m, dict):
                        methods = (
                            m.get("supported_generation_methods")
                            or m.get("supportedMethods")
                            or m.get("capabilities")
                        )
                except Exception:
                    pass

                # Normalize to list of strings
                if methods is None:
                    methods_list = []
                elif isinstance(methods, (list, tuple)):
                    methods_list = [str(x) for x in methods]
                else:
                    methods_list = [str(methods)]

                print(f" - {name}  methods={methods_list}")

                # Selection conditions: gemini model and generation support
                if detected is None:
                    has_generate = any(
                        "generate" in s.lower() or "content" in s.lower()
                        for s in methods_list
                    )
                    if "gemini" in str(name).lower() and has_generate:
                        detected = name
                    elif detected is None and "gemini" in str(name).lower():
                        # fallback to any gemini model if it doesn't explicitly list methods
                        detected = name

            if detected:
                target_model = detected
            print(f"🎯 Using detected model: {target_model}")
        except Exception as e:
            print(f"⚠️ Could not list models: {e}")

        response = client.models.generate_content(
            model=target_model, contents="Hello, respond 'Connection Successful'"
        )
        print(f"✅ Gemini responds: {response.text}")
    except Exception as e:
        print(f"❌ Persistent error: {e}")
        print("\nTip: Check in Google AI Studio if your API Key is active.")


if __name__ == "__main__":
    test_gemini_v2()
