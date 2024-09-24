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


8/16/24
I apologize for having shelved this project


10:55, 9/24/24
I'm going to make the game less recursive, and more iterative
'''

PLAYER_ORDER = [[1, 'first'], [2, 'second'], [3, 'third'], [4, 'fourth'], [5, 'fith']]
deck = []

class Player:
    def __init__(self, name:str, starting_cash = False):
        self.name = name
        self.cash = starting_cash
        self.hand = []
        self.busted = False
        self.stay = False

    def calc_hand_val(self):
            
        self.hand_val = 0
        for _card in self.hand:
            self.hand_val += _card.value
        print(self.hand_val)

        return self.hand_val


class House(Player):

    def __init__(self, deck:list):
        super().__init__(name='house', starting_cash=10000000000000)
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
            players[name] = Player(name=name)
            pass
        
    def hit(self, player:Player):
        card = self.deck.pop()
        players[player].hand.append(card)
        
    def deal(self, player=Player):
        for _ in range(2):
            for player in players:
                self.hit(player)

    def turn(self, player: Player):
        options  = ['1','2','3']
        print(f"ok, {player.name}, it's your turn")
        choice = input(f"""what would you like to do? you have some options. 
              1: check hand value
              2: hit
              3: stay""")
        while choice not in options:
            print("that's not an option")
            choice = input(f"""
              1: check hand value
              2: hit
              3: stay""")
        if choice == "1":
            print(f"your hand is {[card.printable_format for card in player.hand]} and your hand value is {player.calc_hand_val()}")
            if player.calc_hand_val()==21:
                print(f"you got a blackjack, you win")
                player.stay = True
                return player.stay
        elif choice == "2":
            self.hit(player)
            print(f"you got a {player.hand[-1].printable_format}")
        elif choice == "3":
            print(f"ok, thats the end of your turn, your hand is {[card.printable_format for card in player.hand]}")
            player.stay = True
            return player.stay
        



        #you busted
players = {
    "house": House(deck=deck),

} 


mk_deck(deck)
def main():
    players['house'].fetch_players()    #house gets all the players
    players['house'].deal()             #house deals the cards
    for _player in players:             #iterates through the players
        if players[_player] != players['house']:#skips the house because the house goes last
            while players[_player].busted == False:#player only takes a turn if they haven't busted
                print(players[_player].busted)
                players['house'].turn(players[_player]) #player takes a turn
                if players[_player].stay == True:
                    break
                
    players['house'].turn(players['house'])#lets the house take its turn
    #print(players['house'].busted)
        
    print('game ON!!')


print(players)

if __name__ == "__main__":
    main()
    pass
