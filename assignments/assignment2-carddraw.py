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

    