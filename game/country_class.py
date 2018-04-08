class country:
    def __init__(self,idnumb,connectedTo,name):
        self.name=name
        self.idnumb=idnumb
        self.ownedBy=None
        self.troops=0
        self.connectedTo=connectedTo

    def addTroops(self,troopsToAdd):
        self.troops+=troopsToAdd

    def delTroops(self,troopsToDel):
        self.troops-=troopsToDel

    def changeOwner(self,newOwner):
        self.ownedBy=newOwner

    def adjacentTo(self,country):
        if country in self.connectedTo:
            return True
        return False
    
