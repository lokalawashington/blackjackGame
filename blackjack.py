import random


def deal_cards():
    """return a random card from the deck. """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# hint 6 : create a function called calculate_score() that takes a list of cards as input
# and return the score
# look up the sum() function to h elp you do this
def calculate_score(cards):
    """Takes a list of cards and return the score calculated from the card. """
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


# Hint5: deal the user and computer 2 cards each using deal_card
user_cards = []
computer_cards = []

is_game_over = False

for _ in range(2):
    new_card = deal_cards()
    user_cards.append(new_card)
    computer_cards.append(new_card)
# Hint9: call calculate_score(). if the computer or user has a blackjack (0) of if the user's scores is over 21,
# then the game ends
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f"Your card : {user_cards}, current score: {user_score} ")
print(f"Computer first card : {computer_cards[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
