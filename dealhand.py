from random import randint

class Card:
    def __init__(self):
        pass

    def card_value(self):
        pass

    card_face = ['Ace','2','3','4','5','6','7','8','9','10','J','Q','K']
    card_suit = ['Hearts','Spades','Clubs','Diamonds']

class Deck(Card):
    new_deck = []
    length = len(new_deck) #testing purposes

    for i in Card.card_suit:
        for j in Card.card_face:
            new_deck.append(j + ' of ' + i)

    def new_card(self):
        #instead of return, use yield?
        return (self.new_deck[randint(0,len(self.new_deck)-1)])
    
    def remove_card(self,card):
        self.new_deck.remove(card)

class Game:
    def zonedesk():
        d = Deck()
        #d.deck()
        #d.loop()
        c1 = d.new_card()
        d.remove_card(c1)
        c2 = d.new_card()
        d.remove_card(c2)
        print(str(c1) + " and " + str(c2))
        print(len(d.new_deck))

g = Game
g.zonedesk()