import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

if __name__ == "__main__":
    plen = int(input("Enter password length\n"))  # Todo1: Handle Gibberish
    password = generate_password(plen)
    print("Your password is:", password)
