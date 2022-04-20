from art import logo
print(logo)

all_bids = {}

users = True
while users:
    name = input('What is your name? \n')
    bid = int(input('What is your bid amount? \n'))
    new_user = {}
    new_user.update({name: bid})
    all_bids.update(new_user)

    more_users = input('Are the any more users? Type yes or no: \n').lower()
    if more_users == 'no':
        users = False
