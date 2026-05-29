from verification import verify
from report import print_report

def main():
    ip, attempt_pass = user_input()
    result = verify(attempt_pass) 
    print_report(ip, result)

def user_input():
    ip = input("Enter yuor ip (if empty, using default)")
    attempt_pass = input ("Enter the password:")

    return ip, attempt_pass

if __name__ == "__main__":
    main()