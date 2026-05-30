def print_report(ip: str, result: bool, timestamp: str):
    with open("auth.log", "a") as new_file:
        if result:
            new_file.write(timestamp + " Accepted password for root from " + ip + "\n")
            print("Authentication succesfull, correct password")
        else:
            new_file.write(timestamp + " Failed password for root from " + ip + "\n")
            print("Authentication failed, wrong password")
