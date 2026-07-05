from auth.user_store import load_users, update_login_info
from auth.password_manager import verify_password
from datetime import datetime

def verify(input_info):

    result = {
        "locked": False,
        "verification": False
    }
    
    users = load_users()   
    input_username = input_info["username"]
    input_password = input_info["password"]   
    timestamp = input_info["timestamp"]

    if input_username in users:

        if is_user_locked(users, input_username, timestamp):
            result["locked"] = True
        else:
            stored_hash = users[input_username]["password_hash"]
            result["verification"] = verify_password(stored_hash, input_password)
            update_login_info(input_username, result["verification"], timestamp)

    return result


def is_user_locked(users: dict, input_username: str, timestamp: str):
    if users[input_username]["locked_until"] == None:
        return False
    return datetime.strptime(
        users[input_username]["locked_until"], "%Y-%m-%d %H:%M:%S") > datetime.strptime(
            timestamp, "%Y-%m-%d %H:%M:%S")
