import string
from src.pkg.caeser_cipher_ascii_art import caeser_cipher_logo

print(caeser_cipher_logo)

lowercase_alphabet = list(string.ascii_lowercase)


def find_encrypt_letter_index(letter_index, shift_amount):
    new_index = (letter_index + shift_amount) % 26
    return new_index


def find_decrypt_letter_index(letter_index, shift_amount):
    new_index = letter_index - (shift_amount % 26)
    return new_index


def caeser(operation, input_text, alphabet, shift_amount):
    output_text = ""
    for character in input_text:
        if character in alphabet:
            index = alphabet.index(character)

            if operation == "encode":
                new_index = find_encrypt_letter_index(index, shift_amount)
            if operation == "decode":
                new_index = find_decrypt_letter_index(index, shift_amount)

            new_letter = alphabet[new_index]
            output_text += new_letter
        else:
            output_text += character

    return output_text


def get_user_input(prompt):
    return input(prompt)


def main():
    encrypt_decrypt_prompt = "Type 'encode' to encrypt, \
    \nType 'decode' to decrypt:\n"

    is_rerunning = True
    while is_rerunning:
        direction = get_user_input(encrypt_decrypt_prompt)
        text = get_user_input("Type your message:\n").lower()
        shift = int(get_user_input("Type the shift number:\n"))

        shift = shift % 26
        print(caeser(direction, text, lowercase_alphabet, shift))

        rerun = get_user_input(
            "Type 'yes' if you want to go again. Otherwise 'no'.\n"
        ).lower()
        if rerun == "no":
            is_rerunning = False
            print("Good Bye!")


if __name__ == "__main__":
    main()
