def encode_message():
    print("Write message to encrypt")
    clear_user_message = input()
    print("Write how much letters to shift")
    cipher_shift = int(input())
    print(encrypt_message(clear_user_message, cipher_shift))


def decode_message():
    print("Write message to decrypt")
    encrypted_user_message = input()
    print("Write how much letters to shift")
    cipher_shift = int(input())
    print(decrypt_message(encrypted_user_message, cipher_shift))


def encrypt_message(message: str, shift: int) -> str:
    output = ""
    for char in message:
        position = letters.index(char) # Searches for index in letters list assigned to character same as char
        shifted_position = (position + shift) % 26 # Applies shift to index and prevents going beyond the list of 26 letters
        shifted_letter = letters[shifted_position]
        output += shifted_letter
    return output


def decrypt_message(message: str, shift: int) -> str:
    output = ""
    for char in message:
        position = letters.index(char) # Searches for index in letters list assigned to character same as char
        shifted_position = (position - shift) % 26 # Applies shift to index and prevents going beyond the list of 26 letters
        shifted_letter = letters[shifted_position]
        output += shifted_letter
    return output


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Main program loop
while True:
    print("Write decode or encode")
    task = input().lower()
    if task == "decode":
        decode_message()
    elif task == "encode":
        encode_message()
    else:
        print("Please repeat command")
