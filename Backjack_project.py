import random

#deck of cards / player deaker hand
playerhand = []
dealerhand = []
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
         "A", "B", "Q","K","A", "B", "Q","K","A", "B", "Q","K","A", "B", "Q","K"]

# deal the cards
def dealcard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(deck)

# calculate the total of each
def total(turn):
    total = 0
    face = ["A", "B", "Q","K"]
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 1
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total
# check for winner
def revealDealerHand():
    if len(dealerhand) == 2:
        return dealerhand[0]
    elif len(dealerhand) > 2:
        return dealerhand[0], dealerhand[1] 

# game loop 
