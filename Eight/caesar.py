from art import alphabet, logo

def caesar(start_text, shift_amount, shift_direction): # combined function to encrypt / decrypt coded text
    end_text = ''
    if shift_direction == 'decode':
        shift_amount *= -1 # this gives our negative shift value
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f'Your {direction}d text is: {end_text}')

print(logo) # grab ascii art from imported file

again = True
while again: # to see if user wants to keep going
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26 # keeps shift amount in number of letters in alphabet

    caesar(text, shift, direction)
    # user decides if they want to go again which will keep running loop if True
    go_again = input('Do you want to go again? Type yes or no: ')
    if go_again == 'no':
       again = False
       print('Thanks for using our Caesar Cipher - Goodbye')