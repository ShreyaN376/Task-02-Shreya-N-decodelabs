import random
import string


def generate_password(length):
    # Characters used to create the password
    characters = string.ascii_letters + string.digits

    # Generate the random password
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


def main():
    print("=" * 40)
    print("       RANDOM PASSWORD GENERATOR")
    print("=" * 40)

    # Ask the user for password length
    while True:
        try:
            length = int(input("\nEnter password length: "))

            if length <= 0:
                print("Please enter a positive number.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a number.")

    # Generate password
    password = generate_password(length)

    # Display password
    print("\nYour generated password is:")
    print(password)

    print("\n" + "=" * 40)


# Run the program
if __name__ == "__main__":
    main()
    