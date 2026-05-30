from verification import verify
from report import print_report
from datetime import datetime

def main():
    ip, attempt_pass, timestamp = user_input()
    result = verify(attempt_pass) 
    print_report(ip, result, timestamp)

def user_input():
    ip = input("Enter yuor ip (if empty, using default)")
    if ip == "":
        ip = "10.0.0.100"
    attempt_pass = input ("Enter the password:")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return ip, attempt_pass, timestamp

if __name__ == "__main__":
    main()