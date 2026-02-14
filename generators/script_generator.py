from google import genai
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Create Gemini client
client = genai.Client(api_key=api_key)


def generate_script(topic):
    prompt = f"""
    Write a 90-120 second YouTube documentary narration about: {topic}.
    
    IMPORTANT RULES:
    - Write ONLY spoken narration.
    - Do NOT include stage directions.
    - Do NOT include scene descriptions.
    - Do NOT write things like "Video starts with" or "Cut to".
    - No bullet points.
    - No headings.
    - Just clean, natural voiceover text.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print("Gemini API Error:", e)
        return None


