# Password Generator (Terminal-based)
# Author: Nitin Gupta
import random, string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    print("===== PASSWORD GENERATOR =====")
    length = input("Enter password length (default 12): ").strip()
    length = int(length) if length.isdigit() else 12
    password = generate_password(length)
    print(f"🎯 Generated Password: {password}")

if __name__ == "__main__":
    main()
