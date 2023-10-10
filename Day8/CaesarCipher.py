
def encode_message():
    print("Write message to encrypt")
    clear_user_message = input()
    print("Write how much letters to shift")
    cipher_shift = int(input())
    encrypt_message(clear_user_message,cipher_shift)

def decode_message():
    print("Write message to decrypt")
    clear_user_message = input()
    print("Write how much letters to shift")
    cipher_shift = int(input())
    decrypt_message(clear_user_message, cipher_shift)

def encrypt_message(message : str, shift : int) -> list:




def decrypt_message(message : str, shift : int) -> list:
    a




letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']


#Main program loop
while True:
    print("Write decode or encode")
    task = input().lower()
    if task == "decode":
        decode_message()
    elif task == "encode":
        encode_message()
    else:
        print("Please repeat command")