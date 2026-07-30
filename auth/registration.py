from auth.password_manager import create_password
from auth.user_store import check_username_availability, register_new_user


def register(input_info: dict):

    input_username = input_info["username"]
    input_password = input_info["password"]

    result = check_username_availability(input_username)

    if result:
        hashed_password = create_password(input_password)
        register_new_user(input_info, hashed_password)
    return result