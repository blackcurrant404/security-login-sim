from bcrypt import checkpw

def verify_password(stored_hash, input_password: str):
    return checkpw(input_password.encode(), stored_hash.encode())
