from element import Element 
from action import Action

water = Element(name = "Water", health = 100)
fire = Element(name = "Fire", health = 100)
air = Element(name = "Air", health = 90)
earth = Element(name = "Earth", health = 120)
oppwater = Element(name = "Water", health = 90)
oppfire = Element(name = "Fire", health = 90)
oppair = Element(name = "Air", health = 80)
oppearth = Element(name = "Earth", health = 110)
splosh = Action("Splosh", 40, "Wet")
waterfall = Action("Waterfall", 45, "Churning Rapids")
tsunami = Action("Tsunami", 55, "Mud")
scorch = Action("Scorch", 40, "Burn")
firewall = Action("Firewall", 20, "Cover Fire")
phoenix = Action("Phoenix", 70, "Burn")
crunch = Action("Crunch", 50, "")
meteor = Action("Meteor", 60, "Extinction")
fortress = Action("Fortress", 0, "Last Stand")
swoosh = Action("Swoosh", 35, "Dodge")
aslice = Action("Slice", 55, "Critical")
cyclone = Action("Cyclone", 40, "Divine Wind")
global theotest
def main():
    theotest = fire 
    print("HP:", {theotest.health})


main()