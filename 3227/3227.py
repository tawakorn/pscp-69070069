"""CARD 44"""
card = input().upper()

if len(card) == 3:
    RANK = "10"
    suit = card[2]
else:
    RANK = card[0]
    suit = card[1]

if RANK == "A":
    RANK_NAME = "ace"
elif RANK == "J":
    RANK_NAME = "jack"
elif RANK == "Q":
    RANK_NAME = "queen"
elif RANK == "K":
    RANK_NAME = "king"
else:
    RANK_NAME = RANK

if suit == "D":
    SUIT_NAME = "diamonds"
elif suit == "H":
    SUIT_NAME = "hearts"
elif suit == "S":
    SUIT_NAME = "spades"
elif suit == "C":
    SUIT_NAME = "clubs"
else:
    SUIT_NAME = ""

print(RANK_NAME + " of " + SUIT_NAME)
