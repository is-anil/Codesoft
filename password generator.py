import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!@#$%^&*?(){}[]/<>"

def generate_password(length, characters):
    return "".join(random.sample(characters, length))

def main():
    complexity_levels = {
        'weak': lowercase_letters,
        'medium': lowercase_letters + digits,
        'strong': uppercase_letters + lowercase_letters + digits + symbols
    }

    complexity = input("Choose complexity level (weak, medium, strong): ").lower()
    if complexity not in complexity_levels:
        print("Invalid complexity level. Please choose from 'weak', 'medium', or 'strong'.")
        return

    length = int(input("Enter the desired length of the password: "))
    

    amount = int(input("Enter the number of passwords you want to generate: "))

    characters = complexity_levels[complexity]

    print("\nGenerated Passwords:")
    for _ in range(amount):
        password = generate_password(length, characters)
        print(password)

if __name__ == "__main__":
    main()
