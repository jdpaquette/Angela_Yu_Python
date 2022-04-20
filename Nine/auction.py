from art import logo
print(logo)

all_bids = {}
users = True

def winner(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}')

while users:
    name = input('What is your name?: ')
    bid = int(input('What is your bid amount?: $'))
    all_bids[name] = bid
    more_users = input('Are the any more users? Type yes or no: \n').lower()
    if more_users == 'no':
        users = False
        winner(all_bids)