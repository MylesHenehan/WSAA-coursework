import requests 
deck_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
deck_response = requests.get(deck_url)
deck_data = deck_response.json()
#print(data) - used to check the above code was working as it should

deckid = deck_data["deck_id"]
print(deckid) # now we print the deck ID

draw_url = f"https://deckofcardsapi.com/api/deck/{deckid}/draw/?count=5" # formatting the url as an f-string with the deck id retrieved above in the url, and the count set to 5
draw_response = requests.get(draw_url)
draw_data = draw_response.json()
# print(draw_data) - used to check the above code was working as it should

cards = draw_data["cards"]
for card in cards:
    print(f"{card['value']} of {card['suit']}") # this prints out the 5 cards with both value and suit.

# More advanced part of the assignment - check if the user has drawn a pair, triple, straight, or all of the same suit and congratulate the user.

# 1. Separate values and suits into 2 separate lists, since one is not dependent on the other for what we're trying to achieve
drawnsuits = []
for card in cards:
    suit = card["suit"]
    drawnsuits.append(suit)

# print(drawnsuits) - used to test

drawnvalues = []
for card in cards:
    value = card["value"]
    drawnvalues.append(value)

# print(drawnvalues) - used to test

# 2. Congrats message for flush (all same suit)
for suit in set(drawnsuits):
    count = drawnsuits.count(suit)
    if count == 5:
        print("Congratulations, you have a flush.")

# 3. Congrats message for pair or triple
for value in set(drawnvalues):
    count = drawnvalues.count(value)
    if count == 2:
        print("Congratulations, you have a pair.")
    elif count == 3:
        print("Congratulations, you have a triple.")

# 4. Congrats message for a straight
for value in set(drawnvalues):
    