def fetch_players():
    still_fetching_players=True
    print('Welcome to the cassino\n')
    player_num = input('how many players\n')
                    

    while still_fetching_players == True:
        print("in the while loop")
        try:
            player_num = int(player_num)
            print('kinda working')
            still_fetching_players = False
            
                
        except:
            player_num = input('that\'s not a number')
        
    print("Ok, we need some user names for ")
    player_num=int(player_num)
    for player in range(0,  player_num):
            pass
        
fetch_players()