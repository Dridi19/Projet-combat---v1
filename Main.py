from casino import casino
from combat import combat
from Current import current_position
from Hospital import hospital
from Infos import info
from Market import market
from mountain_choise import mountain_choise


class player :
    def __init__(self):
        self.coins = 20
        self.hp = "100"
        self.position = "Spawn"
        self.items = []
        self.weapons = ["battlestaff"]
        self.potions  = []
        self.monster = ""
info()
p1 = player()
while int(p1.coins) < 200 and int(p1.hp) != 0 and exit!= 1:
    p1.position,exit = current_position(p1.position)
    if p1.position == "market":
        (p1) = market(p1)
    if p1.position == "casino":
        p1.coins = casino(p1.coins)
    if p1.position == "hospital":
        p1 = hospital(p1)
    if p1.position == "combat":
        p1.monster = mountain_choise()
        p1 = combat(p1)
if int(p1.hp) ==0:
    print("You lost")
elif exit != 1:
    print("You WIN")
else:
    print("See you soon")
