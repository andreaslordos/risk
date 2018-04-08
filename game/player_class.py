class player:
    def __init__(self,playerID,color):
        self.playerID=playerID
        self.cards=[]
        self.countries_controlled=[]
        self.color=color
        self.attacked=False
        self.alive=True
        self.gotCard=False
        self.bonusTroops=0

    def playCards(self,cardsToPlay):
        def validCombo(cardsToCheck):
            if cardsToCheck.count('s')==3 or cardsToCheck.count('h')==3 or cardsToCheck.count('t')==3 or (cardsToCheck.count('t')==1 and cardsToCheck.count('h')==1 and cardsToCheck.count('s')==1):
                return True
            return False
        
        cardsToPlay=cardsToPlay.split()
        if cardsToPlay in self.cards:
            if len(cardsToPlay)==3:
                if validCombo(cardsToPlay)==True:
                    for card in cardsToPlay:
                        self.cards.remove(card)
                    if cardsToPlay.count('s')==3:
                        self.bonusTroops+=4
                    elif cardsToPlay.count('h')==3:
                        self.bonusTroops+=6
                    elif cardsToPlay.count('t')==3:
                        self.bonusTroops+=8
                    else:
                        self.bonusTroops+=10
                else:
                    print("Invalid combo")
                    return False
            return True
        else:
            print("fake news, you don't have those cards")
            return False

    def displayCards(self):
        print(' '.join(self.cards))
        return

    def placeTroops(self,countries):
        id_to_country={}
        for territory in countries:
            id_to_country[territory.idnumb]=territory
        continents={"na":([1,2,3,4,5,6,7,8,9],5),"sa":([10,11,12,13],2),"afr":([14,15,16,17,18,19],3),"eur":([20,21,22,23,24,25,26],5),"asia":([27,28,29,30,31,32,33,34,35,36,37,38],7),"ocea":([39,40,41,42],2)}
        for key in continents:
            if continents[key][0] in self.countries_controlled:
                self.bonusTroops+=continents[key][1]
        if int(len(self.countries_controlled)/3)==0:
            self.bonusTroops+=1
        else:
            self.bonusTroops+=int(len(self.countries_controlled)/3)
        while self.bonusTroops>0:
            in1=input("Troops left: "+str(self.bonusTroops)+"\nInput number of troops and country id/name: ")
            in1=in1.split()
            if in1[0].isnumeric() and in1[1].isnumeric()==True:
                if int(in1[0])<=self.bonusTroops:
                    if id_to_country[int(in1[1])] in self.countries_controlled:
                        print("Confirmed.")
                        id_to_country[int(in1[1])].troops+=int(in1[0])
                        self.bonusTroops-=int(in1[0])
                    else:
                        print("You do not own that territory")
                else:
                    print("Invalid, too many troops")

    
    
