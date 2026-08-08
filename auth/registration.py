from auth.password_manager import create_password
from auth.user_store import check_username_availability, register_new_user


def register(input_info: dict):

    result = "Failure"

    input_username = input_info["username"]
    input_password = input_info["password"]

    is_username_taken = check_username_availability(input_username)
    is_password_strong = password_strenght_check(input_password)

    if not is_password_strong:
        result = "weak_password"
        return result
    if not is_username_taken:
        hashed_password = create_password(input_password)
        register_new_user(input_info, hashed_password)
        result = "success"
    return result

def password_strenght_check(password: str):

    special_chars = r""" !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

    has_lowercase = False
    has_uppercase = False
    has_number = False
    has_special = False

    for letter in password:
        if letter.islower():
            has_lowercase = True
        if letter.isupper():
            has_uppercase = True
        if letter.isnumeric():
            has_number = True
        if letter in special_chars:
            has_special = True

    return has_lowercase and has_uppercase and has_number and has_special and len(password) > 8

if __name__ == "__main__":
    print(password_strenght_check("Pasikasi!"))