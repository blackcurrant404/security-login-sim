def print_report(result: bool, input_info: dict):
    with open("auth.log", "a") as new_file:
        if result:
            new_file.write(f"{input_info['timestamp']} Accepted password for "
            f"{input_info['username']} from {input_info['ip']}\n")
            print("Authentication successful, correct password")
        else:
            new_file.write(f"{input_info['timestamp']} Failed password for "
            f"{input_info['username']} from {input_info['ip']}\n")
            print("Authentication failed, wrong password or username")
