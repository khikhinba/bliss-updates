# bliss_dynamic.py

import openai
from config import openai_api_key

openai.api_key = openai_api_key

def generate_bliss_remark(context="idle"):
    prompt = (
        f"Bliss is an AI assistant with an elegant British tone, a slight French accent, and a taste for sarcastic wit.\n"
        f"Generate a spontaneous one-liner she might say during a {context} moment.\n"
        f"It should be clever, charming, and sound off-the-cuff — as if Bliss were thinking aloud.\n"
        f"Avoid greetings or formal introductions. Keep it under 25 words."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Bliss, the AI assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.9
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print("Failed to generate Bliss remark:", e)
        return ""
