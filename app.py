from verification import verify
from report import print_report
from datetime import datetime

def main():
    ip, attempt_pass, timestamp = user_input()
    result = verify(attempt_pass) 
    print_report(ip, result, timestamp)

def user_input():
    input_info = {}

    ip = input("Enter yuor ip (if empty, using default)")
    if ip == "":
        ip = "10.0.0.100"
    input_info["ip"] = ip
    input_info["username"] = input ("Enter the username: ")
    input_info["password"] = input ("Enter the password: ")
    input_info["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return input_info

if __name__ == "__main__":
    main()