from cards import mk_deck
from sys import exit

'''
5/21/24
here I will be brutily honest, I have no clue what i was thinking when I coded the
rest of the file, but I didn't comment, so... yeah.
You might need to compleatly scrap the Player and House and just restart, pleese forgive me


5/22/24
a good idea would be to name things so that they are inteligeable, like what does position mean?
take some time to hash out what happens in blackjack and how the mechanics should run


5/23/24
Still have no clue what I am doing, but I'm working on it. 
Added a way to get how many players will play, its fetch_players in Game


13:00, 5/25/24
Going to work on how the Player are made in the fetch_players


2:18, 5/25/24
I'm going to start to work on the casino it'self

'''

PLAYER_ORDER = [[1, 'first'], [2, 'second'], [3, 'third'], [4, 'fourth'], [5, 'fith']]
deck = []

class Player:
    def __init__(self, name:str, starting_cash = False):
        self.name = name
        self.cash = starting_cash
        self.hand = []



class Game(Player):

    def __init__(self, deck:list, starting_cash= int(10000000000000000000)):
        super().__init__(starting_cash)
        self.cash = starting_cash
        self.deck = deck
        self.hand = []


    def fetch_players(self):
        global players
        still_fetching_players=True
        print('Welcome to the cassino\n')
        player_num = input('how many players\n')
                        

        while still_fetching_players == True:
            print("in the while loop")
            try:
                player_num = int(player_num)
                print('kinda working')
                still_fetching_players = False
                
                if player_num == 0:
                    print("ok, goodby")
                    exit()
                    
            except:
                player_num = input('that\'s not a number')
            
        print("Ok, we need some user names for the players")
        player_num=int(player_num)
        for player in range(1, player_num+1):
                
            name = input(f'ok, we need a name for the {PLAYER_ORDER[player-1][1]} player\n')
            pass
        


    def deal(self):
        for card_in_hand_index in range(2):
            print(card_in_hand_index)
            for player in players:
                #for _card in deck:
                    #print(_card.printable_format)
                card = deck.pop(0)
                print(card.printable_format)
                players[player].hand.append(card)
                print(f'player {player} was delt a {players[player].hand[card_in_hand_index].printable_format}')

    def turn(self, player):
        print(f'{player.name}, do you want to take a hit? You have a:')
        for card in range(len(player.hand)):
            if card != len(player.hand)-1:
                print(f'{player.hand[card].printable_format},  ')
            else:
                print(f' and a {player.hand[card].printable_format}')
        pass
players = {
    "Judah": Player("Judah"),
    "house": Game(deck=deck),

} 


mk_deck(deck)
def main(game: Game):
    #game.fetch_players()
    game.deal()
    game.turn(players['Judah'])
    print('game ON!!')

players['house'].fetch_players



if __name__ == "__main__":
    main(game=players['house'])