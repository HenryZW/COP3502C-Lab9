# Contributor: Ziwen Zhu
# Editor: Zachary Allarey

def encoder(password):
    password = str(password)
    encoded_password = ''

    for digit in password:
        new_digit = (int(digit) + 3) % 10
        encoded_password += str(new_digit)

    return encoded_password


def decoder(encoded_password):
    encoded_password = str(encoded_password)
    decoded_password = ''

    for digit in encoded_password:
        original_digit = (int(digit) - 3) % 10
        decoded_password += str(original_digit)

    return decoded_password


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = int(input("Please enter an option: "))

        match option:
            case 1:
                password = input("Please enter your password to encode: ")
                encoded_password = encoder(password)
                print("Your password has been encoded and stored!")

            case 2:
                decoded_password = decoder(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")

            case 3:
                break


if __name__ == "__main__":
    main()
