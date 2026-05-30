users = {"root": "bluewhale", "anna": "1234", "mike": "secret5"}

def verify(input_info):
    
    input_username = input_info["username"]
    input_password = input_info["password"]

    if input_username in users:
        return input_password == users[input_username]

    return False