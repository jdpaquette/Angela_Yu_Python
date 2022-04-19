alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # Add a second total list of alphabet allows for end of index (out of index) error.

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# encoding the text
def encrypt(plain_text, shift_amount): # create new function
    cipher_text = '' # create string to store new letters
    for letter in plain_text: # loop for length of chosen text
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f'The encoded text is: {cipher_text}')

# decoding the text
def decrypt(cipher_text, shift_amount):
    plain_text = ''
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f'The decoded text is: {plain_text}')

# user wants to encode or decode text
if direction == 'encode':
    encrypt(text, shift)
else:
    decrypt(text, shift)
