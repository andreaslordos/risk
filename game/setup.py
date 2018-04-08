from country_class import country
from player_class import player
from random import shuffle

def init_players():
    players=[]
    colors=["red","blue","yellow","orange","green"]
    while True:
        try:
            qPlayers=int(input("How many real people will be playing? "))
            if qPlayers<0 and qPlayers>5:
                print("There can only be between 1 and 5 real players")
            else:
                break
        except:
            print("Invalid. Enter an integer.")
    for x in range(qPlayers):
        c=None
        while c not in colors:
            c=input("Player "+str(x+1)+": pick a color between "+str(','.join(colors))+": ")
        colors.remove(c)
        players.append(player(x,c))
    #players.append(player(99,"black"))
    return players

def split_territories(players,countries):
    shuffle(countries)
    i=0
    while i<len(countries):
        for some_guy in players:
            some_guy.countries_controlled.append(countries[i])
            countries[i].ownedBy=some_guy
            countries[i].troops=1
            i+=1
            if i==len(countries):
                break
    
        
    
