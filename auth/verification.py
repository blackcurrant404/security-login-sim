from auth.user_store import load_users
from auth.password_manager import verify_password

def verify(input_info):
    
    users = load_users()
    result = verify_password(users, input_info)

    return result