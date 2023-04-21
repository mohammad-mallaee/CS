import re


def validate_email(email):
    return re.match(r"\w+@(\w.)+\w{2,7}", email) is not None


def validate_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[+-\/*()\[\]\&%@$#!~?-^])[A-Za-z\d+-\/*()\[\]\&%@$#!~?-^]{8,}"
    return re.match(pattern, password) is not None


n = int(input())
result = []
for _ in range(n):
    email, password = input().split()
    is_email_valid = validate_email(email)
    is_password_valid = validate_password(password)
    result_str = "invalid"
    if is_email_valid and is_password_valid:
        result.append("true")
        continue
    if not is_email_valid:
        result_str += "_email"
    if not is_password_valid:
        result_str += "_password"
    result.append(result_str)

print("\n".join(result))
