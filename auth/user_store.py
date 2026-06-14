from json import load, dump
from datetime import datetime

def load_users():
    with open("data/users.json") as new_file:
        return load(new_file)

def update_login_info(username: str, result: bool):
    users = load_users()
    if result:
        users[username]["last_login"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        users[username]["failed_attempts"] = 0 
    else:
        users[username]["failed_attempts"] += 1

    save_users(users)
    return

def save_users(users: dict):
    with open("data/users.json", "w") as new_file:
        dump(users, new_file, indent=4)
        return


        
