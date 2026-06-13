from auth.user_store import load_users

def verify(input_info):
    
    input_username = input_info["username"]
    input_password = input_info["password"]
    users = load_users()

    if input_username in users:
        return input_password == users[input_username]["password"]

    return False