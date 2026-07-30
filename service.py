from auth.audit import print_report
from auth.registration import register
from auth.verification import verify


def login_user(input_info: dict):
    result = verify(input_info)
    input_info["result"] = result
    print_report(input_info)

    return result

def register_user(input_info: dict):
    result = register(input_info)
    return result