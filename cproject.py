import random 

print('Welcome to Derby! One of a kind of card game!')




cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
typeofcards = ["Clubs", "Hearts", "Diamonds","Spades"]
deck = []

    

    
for card in cards:
    for typeofcard in typeofcards:
        deck.append([ typeofcard,])
print(deck)
print({len(deck)}, 'card in the deck.')
print(input("draw? yes/no\n"))
print(input("whoever gets the most of their type of cards wins. are you ready!? yes/no\n"))

    


player1 = []
player2 = []
points = 0
points2 = 0
while len(player1) < 25:
    card = random.choice(deck)
    deck.remove(card)
    player1.append(card)
    secondcard = random.choice(deck)
    deck.remove(secondcard)
    player2.append(secondcard)
hearts = 0
clubs = 0
diamonds = 0
spades = 0

choices = print(input("what type of card player1 choose to be ? Clubs/Hearts/Diamonds/Spades\n"))
for cards in player1:
    if cards == ["Hearts"]:
         hearts = hearts + 1
print("there is this many hearts in your hand player1\n", hearts)
choices2 = print(input("what type of card player2 choose to be? Clubs/Hearts/Diamonds/Spades\n"))
for cards in player2:
    if cards == ["Clubs"]:
        clubs = clubs + 1
print('there is this many clubs in your hand player2\n', clubs)
    

print('player1 show hands', player1, )
print('player2 show hands', player2, )











    

    
   
    
    










