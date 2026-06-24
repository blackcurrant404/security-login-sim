from json import load, dump, JSONDecodeError

def load_users():
    try:
        with open("data/users.json") as new_file:
            return load(new_file)
    except (FileNotFoundError, JSONDecodeError):
        return {}

def update_login_info(username: str, result: bool, timestamp):
    users = load_users()
    if result:
        users[username]["last_login"] = timestamp
        users[username]["failed_attempts"] = 0 
    else:
        users[username]["failed_attempts"] += 1

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
        "last_login": None
        }
    save_users(users)
    return

def check_username_availability(input_username: str):
    users = load_users()
    return input_username not in users
