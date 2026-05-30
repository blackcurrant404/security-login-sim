def print_report(result: bool, input_info: dict):
    with open("auth.log", "a") as new_file:
        if result:
            new_file.write(input_info["timestamp"] + " Accepted password for root from " 
            + input_info["ip"] + "\n")
            print("Authentication succesfull, correct password")
        else:
            new_file.write(input_info["timestamp"] + " Failed password for root from " 
            + input_info["ip"] + "\n")
            print("Authentication failed, wrong password or username")
