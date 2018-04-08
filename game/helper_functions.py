from country_class import country
from player_class import player
from random import randint



def attackTerritory(attackingTer,defendingTer,attacker,defender,attackingTroops):
    
    def conquerTerritory(attackingTer,defendingTer,loser,winner,attackingTroops):
        loser.countries_controlled.remove(defendingTer)
        winner.countries_controlled.append(defendingTer)
        if winner.gotCard==False and len(winner.cards)!=5:
            bonus_cards=["s","h","t"]
            winner.cards.append(bonus_cards[randint(0,2)])
            winner.gotCard=True
        defendingTer.ownedBy=winner
        while True:
            try:
                minimun=attackingTroops
                if attackingTroops>3:
                    minimum=3
                a=int(input("How many troops would you like to move into "+str(defendingTer.name)+"("+str(defendingTer.idnumb)+") - maximum "+str(attackingTer.troops-1)+", minimum "+str(minimum)))
                if a>=minimum and a<attackingTer.troops:
                    defendingTer.troops=a+1
                    attackingTer.troops-=a
                    break
            except:
                print("Invalid input")
        if len(loser.countries_controlled)==0:
            loser.alive=False
            winner.cards+=loser.cards[0:5-len(winner.cards)]
        return attackingTer,defendingTer,loser,winner

    if (attackingTer.ownedBy==attacker and defendingTer.ownedBy==defender and attackingTroops>0 and attackingTer.troops>attackingTroops and attackingTer in defendingTer.connectedTo):
        aDices=[]
        dDices=[]
        for x in range(attackingTroops):
            aDices.append(randint(1,6))
            if x==2:
                break
        for y in range(defendingTer.troops):
            dDices.append(randint(1,6))
            if x==1:
                break
        aDices.sort(reverse=True)
        dDices.sort(reverse=True)
        print("Attacker rolled",aDices)
        print("Defender rolled",dDices)
        if len(aDices)>len(dDices):
            maxi=len(dDices)
        else:
            maxi=len(aDices)
        for z in range(maxi):
            if aDices[z]>dDices[z]:
                defendingTer.troops-=1
                print("Defender loses one troop")
            else:
                attackingTer.troops-=1
                print("Attacker loses one troop")
        if defendingTer.troops==0:
            print("Territory conquered!")
            attackingTer,defendingTer,defender,attacker=conquerTerritory(attackingTer,defendingTer,defender,attacker,attackingTroops)
        return attackingTer,defendingTer,attacker,defender

        
def fortify(mover,origin,destination,troops,countries):
    
    def isPath(current,destination,mover,countries):
        #Implements a breadth-first search in order to determine whether there is path between two nodes, in which all nodes of that path are owned
        #by the same player
        a=[]
        connected=current.connectedTo
        print(connected)
        while destination not in connected:
            for thing in connected:
                if thing.ownedBy==mover:
                    a+=thing.connectedTo
            if a==[]:
                break
            connected=a[:]
            print(connected)
            a=[]

        if destination in connected:
            print("there is a path")
            return True
        print("No path")
        return False
    
    if origin.ownedBy==mover and destination.ownedBy==mover:
        if isPath(origin,destination,mover,countries)==True:
            if origin.troops>troops:
                origin.troops-=troops
                destination.troops+=troops
            else:
                print("Do not have that many troops to fortify")
                return False
        else:
            print("No path between those two territories")
    else:
        print("Do not own one of those territories")
        return False
    return origin,destination


        
             
            
    
