# bliss_context.py

from textblob import TextBlob
import random
import time

# Simulated voice emotion state (expand with real VAD/ML audio models later)
current_emotion = "neutral"

# Session management
timeout_duration = 90  # seconds
last_active_time = 0

def refresh_session():
    global last_active_time
    last_active_time = time.time()

def is_session_active():
    return (time.time() - last_active_time) < timeout_duration

def end_session():
    global last_active_time
    last_active_time = 0

def analyze_mood(text):
    refresh_session()
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.4:
        return "happy"
    elif polarity < -0.2:
        return "frustrated"
    elif 0.0 < polarity <= 0.4:
        return "calm"
    else:
        return "tired"

def generate_emotional_response(response_text, mood, mekhi_name=True):
    tags = {
        "happy": [
            "Well, someone's in high spirits today.",
            "Feeling fantastic, are we?",
            "Cheerful as ever, monsieur."
        ],
        "frustrated": [
            "No worries, Mekhi. We’ll fix it together.",
            "I sense some heat—don’t worry, I’m cooler.",
            "Let’s keep it snappy, shall we?"
        ],
        "tired": [
            "You sound worn out, Mekhi. Want a break?",
            "Yawn... oh wait, that was you.",
            "I’ll be gentle. You need it."
        ],
        "calm": [
            "Just another breezy moment with you, Mekhi.",
            "Calm waters, smooth sailing.",
            "Nice and easy, monsieur."
        ]
    }

    remark = random.choice(tags.get(mood, ["Ready when you are, monsieur."]))
    if mekhi_name and random.random() < 0.4:
        response_text = f"{remark} {response_text}"

    return response_text


