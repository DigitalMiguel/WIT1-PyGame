class TestingObject:
    var = "Hello"

    def function(self):
        print("Hello I'm just a function")

class Vehicle:
    type = "None"
    cupholders = False
    numSeats = 1
    engine = True

    def getType(self):
        return self.type

    def setType(self, name):
        self.type = name

    def getSeats(self):
        return self.numSeats

    def setSeats(self, num):
        self.numSeats = num

class Pokemon:
    name = ""
    type = ""
    rarity = ""
    defence = 0
    attack = 0
    health = 10

    def setName(self, name):
        self.name = name

    def setType(self, type):
        self.type = type

    def setRarity(self, type):
        self.rarity = type

    def powerUp(self):
        self.attack = self.attack + 10

    def takeDamage(self, dmg):
        self.health = self.health - dmg

    def getStatus(self):
        print("***** " + self.name + " *****")
        print("Type :" + self.type)
        print("Rarity :" + self.rarity)
        print("Defence :" + str(self.defence))
        print("Attack :" + str(self.attack))





# myObject = TestingObject()
#
# myObject.function()

poke1 = Pokemon()
poke1.setName(input())
poke1.setRarity("Mythical")
poke1.setType("Fire")
poke1.getStatus()
