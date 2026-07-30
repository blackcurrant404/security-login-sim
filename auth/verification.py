from datetime import datetime, timedelta, timezone

from auth.password_manager import verify_password
from auth.user_store import load_users, update_login_info


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
        user = users[input_username]

        if is_user_locked(user, timestamp):
            result["locked"] = True
        else:
            
            stored_hash = user["password_hash"]           
            result["verification"] = verify_password(stored_hash, input_password)

            if not result["verification"]:
                user["failed_attempts"] += 1
                if user["failed_attempts"] >= 3:
                    user["locked_until"] = datetime_to_string(calculate_cooldown(timestamp))

            update_login_info(input_username, user, result["verification"], datetime_to_string(timestamp))

    return result


def is_user_locked(user: dict, timestamp: datetime):
    if user["locked_until"] is None:
        return False
    return string_to_datetime(user["locked_until"]) > timestamp

def calculate_cooldown(timestamp: datetime):
    return (timestamp + timedelta(minutes=1))

def datetime_to_string(x: datetime):
    return x.strftime("%Y-%m-%d %H:%M:%S")

def string_to_datetime(x: str):
    return datetime.strptime(x, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)