

import random
import string


CHARACTER_POOL = string.ascii_uppercase + string.ascii_lowercase + string.digits


def get_valid_length():
    """
    Ask the user how long they want their password to be.
    Keep asking until a valid whole number is entered that
    is within a sensible range (4 to 32 characters).
    Returns the length as an integer.
    """
    while True:
        user_input = input("Enter desired password length (4-32): ").strip()

        # Make sure the user typed a whole number
        if not user_input.isdigit():
            print("Invalid input. Please enter a whole number (e.g. 8).")
            continue

        length = int(user_input)

        # Keep the length within a reasonable, safe range
        if length < 4 or length > 32:
            print("Please choose a length between 4 and 32 characters.")
            continue

        return length


def generate_password(length):
    
    password_characters = []

    for _ in range(length):
        random_character = random.choice(CHARACTER_POOL)
        password_characters.append(random_character)

    # Join the list of characters into one string
    password = "".join(password_characters)
    return password


def show_header():
    
    print("      RANDOM PASSWORD GENERATOR")
    print("      DecodeLabs Training - Project 3")
    


def main():
    
    show_header()

    generating = True

    while generating:
        length = get_valid_length()
        password = generate_password(length)

        print(f"\nYour generated password is: {password}\n")

        again = input("Generate another password? (y/n): ").strip().lower()
        if again != "y":
            generating = False

    print("\nThank you for using the Random Password Generator. byebye!")


if __name__ == "__main__":
    main()