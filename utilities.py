import json,os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_FILE = os.path.join(BASE_DIR, "tasks.json")


def load_file(file_path):
    if not os.path.exists(file_path):
        return []

    if os.path.getsize(file_path) == 0:
        return []

    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
    
def load_tasks():
    return load_file(TASKS_FILE)

def save_file(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def save_tasks(tasks):
    save_file(TASKS_FILE, tasks)