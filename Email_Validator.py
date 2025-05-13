import re

def email_validator():
    email = input("Enter your email address: ")
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]$'

    if re.match(pattern, email):
        print(f"{email} is a Valid email address")
    else:
        print(f"{email} is an Invalid email address")
    
email_validator()