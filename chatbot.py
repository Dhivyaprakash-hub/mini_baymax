def respond_to_emotion(emotion):
    responses = {
        "happy": "I'm glad you're feeling happy! 😊",
        "sad": "I'm here for you. Want to talk about it?",
        "neutral": "Let me know if you need anything.",
        "angry": "Take a deep breath. I'm with you.",
    }
    return responses.get(emotion, "I'm here to help with however you're feeling.")
