from bcrypt import checkpw, gensalt, hashpw


def verify_password(stored_hash, input_password: str):
    return checkpw(input_password.encode(), stored_hash.encode())

def create_password(input_password):
    hashed = hashpw(input_password.encode(), gensalt())
    return hashed.decode()