import secrets
import string

def generate_secure_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

generate_password = input("do you want to use generated password?: ").lower().strip()
if generate_password == "yes":
    length = int(input("enter your desired password length: "))
    password = generate_secure_password(length)
    print("your password is:", password)
elif generate_password == "no":
    password_own = input("enter your password: ")
    print(f"your password is: {password_own}")
