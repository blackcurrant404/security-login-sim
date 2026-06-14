from bcrypt import checkpw

def verify_password(users: dict, input_info: dict):
    input_username = input_info["username"]
    input_password = input_info["password"]   
    
    if input_username in users.keys():
        stored_hash = users[input_username]["hash_password"]
        return checkpw(input_password.encode(), stored_hash.encode())

    return False

