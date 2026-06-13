from json import load

def load_users():
    with open("data/users.json") as new_file:
        return load(new_file)