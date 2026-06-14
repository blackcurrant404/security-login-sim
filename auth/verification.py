from auth.user_store import load_users
from auth.password_manager import verify_password
from auth.user_store import update_login_info

def verify(input_info):

    users = load_users()   
    input_username = input_info["username"]
    input_password = input_info["password"]   

    if input_username in users: 
        stored_hash = users[input_username]["password_hash"]
        result = verify_password(stored_hash, input_password)
        update_login_info(input_username, result)
        return result
    else:
        return False