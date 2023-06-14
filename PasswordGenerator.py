import random
import string

class PasswordGenerator:
    def __init__(self, length):
        self.length = length

    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password

def main():
    length = 10

    generator = PasswordGenerator(length)
    password = generator.generate_password()

    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
