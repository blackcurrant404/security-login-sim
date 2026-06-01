from verification import verify
from report import print_report

def login_user(input_info: dict):
    result = verify(input_info)
    input_info["result"] = result
    print_report(input_info)

    return result