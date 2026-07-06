def print_report(input_info: dict):
    with open("logs/auth.log", "a") as new_file:

        if input_info["result"]["locked"]:
            new_file.write(f"{input_info['timestamp']} Failed attempt, reason: locked user for "
            f"{input_info['username']} from {input_info['ip']}\n")
            print("Failed attempt, reason: locked user")
        else:
            if input_info["result"]["verification"]:
                new_file.write(f"{input_info['timestamp']} Accepted password for "
                f"{input_info['username']} from {input_info['ip']}\n")
                print("Authentication successful, correct password")
            else:
                new_file.write(f"{input_info['timestamp']} Failed password for "
                f"{input_info['username']} from {input_info['ip']}\n")
                print("Authentication failed, wrong password or username")
