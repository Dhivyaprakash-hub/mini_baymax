import json
from datetime import datetime, timezone
from pathlib import Path

def log_emotion(emotion, source):
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "emotion": emotion,
        "source": source
    }
    try:
        with open("mood_log.json", "r") as f:
            logs = json.load(f)
    except FileNotFoundError:
        logs = []
    except (json.JSONDecodeError, OSError):
        # Preserve a readable log on disk instead of overwriting damaged data.
        return False
    logs.append(entry)
    try:
        Path("mood_log.json").write_text(json.dumps(logs, indent=2), encoding="utf-8")
    except OSError:
        return False
    return True
