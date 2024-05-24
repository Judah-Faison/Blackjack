from cards import *
from sys import exit

'''

here I will be brutily honest, I have no clue what i was thinking when I coded the
rest of the file, but I didn't comment, so... yeah.
You might need to compleatly scrap the Player and House and just restart, pleese forgive me
5/21/24


a good idea would be to name things so that they are inteligeable, like what does position mean?
take some time to hash out what happens in blackjack and how the mechanics should run
5/22/24


Still have no clue what I am doing, but I'm working on it. 
5/23/24


'''



class Game:
    def __init__(self, deck: list) -> None:
        self.deck=deck

    def fetch_players(self):
        still_fetching_players=True
        print('Welcome to the cassino\n')
        player_num = input('how many players\n')
                        

        while still_fetching_players == True:
            print("in the while loop")
            try:
                player_num == int()
                print('kinda working')
                still_fetching_players = False
                
                if player_num == 0:
                    print("ok, goodby")
                    exit()
                    
            except:
                player_num = input('that\'s not a number')
            
        print("Ok, we need some user names for ")
        player_num=int(player_num)
        for player in range(0,  player_num):
                pass
        


    def deal(self):
        for player in players:
            pass

game = Game(deck=deck)

game.fetch_players

class Player:
    def __init__(self, name:str, starting_cash = False):
        pass

    
    pass

players = {
    "Judah": Player("Judah")

} 

def main(game: Game):
    game.fetch_players()
    print('game ON!!')




if __name__ == "__main__":
    main(game=game)