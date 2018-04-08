from country_class import country
from player_class import player
from generate_countries import generateCountries
from random import shuffle
from drawer import drawMap    
from setup import init_players,split_territories
from helper_functions import attackTerritory,fortify

countries=generateCountries()

id_to_country={}
for territory in countries:
    id_to_country[territory.idnumb]=territory
players=init_players()

temp_countries=countries[:]
split_territories(players,temp_countries)
shuffle(players)


turn=0
rounds=0


while len(players)>1:
    drawMap(countries,players)
    rounds+=1
    if turn>len(players)-1:
        turn=0
    current_player=players[turn]
    current_player.gotCard=False
    print(current_player.color.title(),"player's turn")
    print("You have the following cards: ")
    print(current_player.displayCards())
    current_player.bonusTroops=0
    a=input("Would you like to play a set of cards (y/n): ")
    if a[0].lower()=="y":
        playcards=input("Cards to play (space seperated): ")
        current_player.playCards(playcards)
    current_player.placeTroops(countries)
    print("Input 'end' at any time to stop attacking")
    in2=input("Input e or the id/name of the attacking and defending country, along with the attacking troops (e.g. 13 14 5) ")
    print("Input 'showmap' to view the map")
    while in2!="e":
        if in2=='showmap':
            drawMap(countries,players)
        else:
            in2=in2.split()
            defender=id_to_country[int(in2[1])].ownedBy
            id_to_country[int(in2[0])],id_to_country[int(in2[1])],current_player,defender=attackTerritory(id_to_country[int(in2[0])],id_to_country[int(in2[1])],current_player,defender,int(in2[-1]))
        in2=input("Input e or the id/name of the attacking and defending country, along with the attacking troops (e.g. 13 14 5) ")
    last_in=input("Would you like to fortify (y/n): ")
    if last_in[0].lower()=="y":
        z=id_to_country[int(input("Origin: "))]
        x=id_to_country[int(input("Destination: "))]
        y=int(input("Number of troops: "))
        z,x=fortify(current_player,z,x,y,countries)
        id_to_country[z.idnumb]=z
        id_to_country[x.idnumb]=x
    turn+=1
    
print("Game over!")

for p in players:
    if p.alive==True:
        print("The",p.color,"has won!")
