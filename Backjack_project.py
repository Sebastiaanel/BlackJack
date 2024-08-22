import random

#deck of cards / player deaker hand

playerIn = True
dealerIn = True

playerhand = []
dealerhand = []
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
         "A", "B", "Q","K","A", "B", "Q","K","A", "B", "Q","K","A", "B", "Q","K"]

# deal the cards
def dealcard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# calculate the total of each
def total(turn):
    total = 0
    face = ["A", "B", "Q","K"]
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 10
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
for _ in range(2):
    dealcard(dealerhand)
    dealcard(playerhand)

while playerIn or dealerIn:
    print(f"Deaker had {dealerhand} and X")
    print(f"You have {playerhand} for a total of {total(playerhand)}")
    if playerIn:
        stayOrHit = input("1: Stay\n2:Hit\n")
        if total(dealerhand) > 16:
            dealerIn = False
        else:
            dealcard(dealerhand)
        if stayOrHit == "1":
            playerIn = False
        else:
            dealcard(playerhand)

        if total(playerhand) >= 21:
                break
        elif total(dealerhand) >= 21:
                break

if total(playerhand) == 21:
    print(f"You have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("Blackjack! You win!")
elif total(dealerhand) == 21:
    print(f"You have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("Blackjack! Dealer win!")
elif total(playerhand) > 21:
    print(f"You have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("You bust! Dealer win!")
elif total(dealerhand) > 21:
    print(f"You have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("Deaker bust! You win!")
elif 21 - total(dealerhand) < 21 - total(playerhand):
    print(f"You have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("Dealer win!")
elif 21 - total(playerhand) < 21 - total(dealerhand):
    print(f"You have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("Player win!")