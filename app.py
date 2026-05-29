from verification import verify

def main()
    ip, attempt_pass = user_input()
    resukt = verify(attempt_pass) 
    result(ip, verification)

def user_input()
    ip = input("Enter yuor ip (if empty, using default)")
    attempt_pass = input ("Enter the password:")

    return ip, attempt_pass

if __name__ == "__main__":
    main()