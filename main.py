import os
import random
import tweepy
from google import genai
from google.genai import types

# 1. Setup Clients
client_gemini = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
    http_options={"api_version": "v1"}
)

client_x = tweepy.Client(
    consumer_key=os.getenv("X_API_KEY"), 
    consumer_secret=os.getenv("X_API_SECRET"),
    access_token=os.getenv("X_ACCESS_TOKEN"), 
    access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET")
)

INTEREST_PROFILE = """
Persona: AI Tech Founder. 
Voice: High-signal, builder-focused, zero-fluff, slightly contrarian. 
Topics: Agentic AI, FinTech infra, Future of Work.
"""

def generate_thesis():
    topic = random.choice(["Agentic AI", "AI Startups", "FinTech", "Autonomous Agents"])
    prompt = f"""
{INTEREST_PROFILE}
Write ONE sharp tweet about {topic}. Under 240 characters. No emojis. Use exactly 2 hashtags. Output ONLY the tweet text.
"""

    try:
        response = client_gemini.models.generate_content(
            # Use a stable supported model
            model="models/gemini-2.5-flash-lite",  
            contents=prompt,
            config=types.GenerateContentConfig(
                max_output_tokens=100,
                temperature=0.7
            )
        )
        return response.candidates[0].content.parts[0].text.strip().replace('"', '')

    except Exception as e:
        print(f"❌ Gemini Error: {e}")
        return None

def run_bot():
    print("🚀 Wake up, Founder. Generating original thesis...")
    content = generate_thesis()
    
    if content:
        try:
            client_x.create_tweet(text=content[:240])
            print(f"✅ SUCCESSFUL POST:\n{content}")
        except Exception as e:
            print(f"❌ X API Error: {e}")
            print("💡 TIP: If you see 'Forbidden', regenerate your X tokens in the dev portal.")

if __name__ == "__main__":
    run_bot()

