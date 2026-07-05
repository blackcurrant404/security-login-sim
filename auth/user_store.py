from json import load, dump, JSONDecodeError
from datetime import datetime, timedelta

def load_users():
    try:
        with open("data/users.json") as new_file:
            return load(new_file)
    except (FileNotFoundError, JSONDecodeError):
        return {}

def update_login_info(username: str, result: bool, timestamp):
    users = load_users()
    user = users[username]
    if result:
        user["last_login"] = timestamp      
        user["failed_attempts"] = 0 
        user["locked_until"] = None
    else:
        user["failed_attempts"] += 1
        if user["failed_attempts"] >= 3:
            user["locked_until"] = calculate_cooldown()

    users[username] = user
    save_users(users)
    return

def save_users(users: dict):
    with open("data/users.json", "w") as new_file:
        dump(users, new_file, indent=4)
        return

def register_new_user(input_info: dict, hashed_password: str):
    users = load_users()
    users[input_info["username"]] = {
        "password_hash": hashed_password,
        "failed_attempts": 0,
        "last_login": None,
        "locked_until": None
        }
    save_users(users)
    return

def check_username_availability(input_username: str):
    users = load_users()
    return input_username not in users

def calculate_cooldown():
    return (datetime.now() + timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")


# for testing 
if __name__ == "__main__":
    update_login_info("root", False, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))