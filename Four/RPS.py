# Rock, Paper, Scissors Game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock, paper, scissors]
print('Welcome to the "Best" Rock, Paper, Scissors game!')
choice = int(input('What is your choice? Type 0 for Rock, 1 for Paper, or 2 for Scissors: '))

print('\nYour choice was:\n')
if choice >= 3 or choice < 0:
    print('YOU DID NOT MAKE A VALID CHOICE!\n')
else:
    print(images[choice])

print('Computer chose:\n')
computer = random.randint(0, 2)
print(images[computer])

if choice == computer:
    print('It\'s a TIE!')
elif choice == 0 and computer == 1:
    print('Paper beats rock. You Lose!')
elif choice == 0 and computer == 2:
    print('Rock beats Scissors. You Win!')
elif choice == 1 and computer == 0:
    print('Paper beats rock. You Win!')
elif choice == 1 and computer == 2:
    print('Scissors beats paper. You Lose!')
elif choice == 2 and computer == 0:
    print('Rock beats Scissors. You Lose!')
elif choice == 2 and computer == 1:
    print('Scissors beats paper. You Win!')
else:
    print('YOU LOSE')


