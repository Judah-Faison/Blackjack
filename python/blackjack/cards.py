from random import shuffle
##### this is where i define some variables that I will use throughout the programm
facecards = ['Jack', 'Queen', 'King']                #a list of the cards that have a special atribute
suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']    #a list of the suits
deck = []                                            #an empty list that we will store all the cards in

class Card:
    def __init__(self, sute, name):
        self.sute = sute            #
        self.name = name            #  we must have a name and value because of the facecaerds
        self.value = name           #
        if self.name in facecards:  # these statements
            if self.name == 'King': # allow us to 
                self.value=13       # assigne values
                                    # to the facecards
            if self.name =='Queen': # jack, queen and
                self.value=12       # king
                                    #
            if self.name == 'Jack': #
                self.value=11       #
                
                                    # the 'printable_format variable is there so that 
                                    # you can print to the terminal a specific card instead of an object hash
        self.printable_format=f'{self.name} of {self.sute}' 
        
    
                                    # this is where we fill in the deck with cards
for _suit in range(0, 4):           # 4 times it goes thru the processs, once per suit
    suit = suits[_suit]             # the _suit is a placeholder cuz your to dumb to think of something better
    for value in range(1, 10):
        deck.append(Card(suit, value))
    for facecard in facecards:
        deck.append(Card(suit, facecard))
        shuffle(deck)