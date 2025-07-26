import json, os, datetime

# directory
HISTORY_DIR = os.path.join(os.path.dirname(__file__), "..", ".glassbox_history")
os.makedirs(HISTORY_DIR, exist_ok=True)

# filename
time = datetime.datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
_session_file = os.path.join(HISTORY_DIR, f"history_{time}.json")

# current session history
_history = []

def write_history(entry: dict) -> None:
    _history.append(entry)
    with open(_session_file, "w", encoding="utf-8") as file:
        json.dump(_history, file, indent=2)

def get_history() -> list[dict[str,str]]:
    return _history