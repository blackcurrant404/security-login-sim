def print_report(ip, result):
    with open("auth.log", "a") as new_file:
        if result:
            new_file.write("Accepted password for root from " + ip + "\n")
            print("Authentication succesfull, correct password")
        else:
            new_file.write("Failed password for root from " + ip + "\n")
            print("Authentication failed, wrong password")
