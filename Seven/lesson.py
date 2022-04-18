import random


end_of_game = False
word_list = ['ardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(f'Pssst, the solution is {chosen_word}.')

display = [] # creates the blank spaces based on random word
for i in range(word_length):
    display.append('_')

while not end_of_game:
    guess = input('Guess a letter:\n').lower()
    for position in range(word_length): # Check guessed letter is in word
        if chosen_word[position] == guess:
            display[position] = guess

    if guess not in chosen_word:
        print('Wrong Guess')
        lives -= 1
        if lives > 0:
            print(stages[lives])
        else:
            end_of_game = True
            print('You Lose!')

    print(f"{' '.join(display)}") # Join all elements in list to make string

    if "_" not in display: # Check if user entered all letters
        end_of_game = True
        print('You Win!')



