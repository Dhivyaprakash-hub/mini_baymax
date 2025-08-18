from emotion_face import detect_face_emotion
from emotion_voice import detect_voice_emotion
from chatbot import respond_to_emotion
from logger import log_emotion

def main():
    print("👋 Hi! I'm Mini-Baymax. Let's check how you're feeling today.")

    face_emotion, face_conf = detect_face_emotion()
    print(f"Facial emotion: {face_emotion} (confidence: {round(face_conf*100)}%)")
    log_emotion(face_emotion, "face")

    voice_emotion, voice_conf = detect_voice_emotion()
    print(f"Voice emotion: {voice_emotion} (confidence: {round(voice_conf*100)}%)")
    log_emotion(voice_emotion, "voice")

    final_emotion = face_emotion
    response = respond_to_emotion(final_emotion)
    print("Baymax:", response)
    log_emotion(final_emotion, "chatbot_response")

if __name__ == "__main__":
    main()
