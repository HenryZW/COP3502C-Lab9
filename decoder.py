def decoder(encoded_password):
    decoded_password = ''

    for digit in encoded_password:
        original_digit = (int(digit) - 3) % 10
        decoded_password += str(original_digit)

    return decoded_password