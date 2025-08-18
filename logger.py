import json
from datetime import datetime

def log_emotion(emotion, source):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "emotion": emotion,
        "source": source
    }
    try:
        with open("mood_log.json", "r") as f:
            logs = json.load(f)
    except:
        logs = []
    logs.append(entry)
    with open("mood_log.json", "w") as f:
        json.dump(logs, f, indent=2)
