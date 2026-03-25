from element import Element 
from action import Action
import random
from random import choice 
water = Element(name = "Water", health = 100)
fire = Element(name = "Fire", health = 100)
air = Element(name = "Air", health = 90)
earth = Element(name = "Earth", health = 120)
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


print("LOADING...")
print("...")


def main():

    elselect() 
    
    
def elselect():    
    print("Welcome to Elemenbrawl: choose your element: \n")
    global elsel
    elsel = input ("-Water \n-Fire \n-Earth \n-Air \n")
    elsel = elsel.title()
    
    if elsel == "Water":
        water()
    elif elsel == "Fire":
        fire()
    else:
        print("Please choose a valid element:\n-Water \n-Fire \n-Earth \n-Air \n")
        elselect()

def water():
    selfel = water
    water = Element(name = "Water", health = 100)
    
    print("Water! Good choice, balanced and life sustaining, sure to wash away the competition! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Splosh \nDMG: 40\nWET: Target deals -20% DMG next turn\n")
    print("Waterfall \nDMG: 45\nCHURNING RAPIDS: Target takes +20% DMG next turn\n")
    print("Tsunami \nDMG: 55\nMUD: Target 55% Chance to miss next attack\n")
    print("HP", {water.health})
    loading()

def fire():
    selfel = fire
    fire = Element(name = "Fire", health = 100)
    print("Fire! Exellent choice, aggressive ""Scorch 'n burn"" playstyle, sure to incinerate the competition! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Scorch \nDMG: 40\nBURN: Target takes 10 DMG for 2 turns \n")
    print("Firewall \nDMG: 20\nCOVERING FIRE: Negates 80% DMG taken next turn \n")
    print("Phoenix \nDMG: 70\nBURN: Heal 50% DMG dealt \n")
    print("HP", {fire.health})
    loading()


def gameplay():
     print("An ENEMY has appeared!")
     opel = random.choice(["Fire", "Water","Air", "Earth"])
     if opel == "Fire":
         print("ENEMY element is FIRE, beware")
         splosh.damage *= 1.5
         waterfall.damage *= 1.5
         tsunami.damage *= 1.5
         opp = Element(name = "Fire Titan", health = 100)
         print(f"ENEMY HEALTH {opp.health_max}")
         fight()
     elif opel == "Water":
         print("ENEMY element is WATER, beware")
         crunch.damage *= 1.5
         meteor.damage *= 1.5
         fortress.damage *= 1.5
         opp = Element(name = "Water Guardian", health = 100)
         print(f"ENEMY HEALTH {opp.health_max}")
         fight()
     elif opel == "Air":
         print("ENEMY element is AIR, beware")
         scorch.damage *= 1.5
         firewall.damage *= 1.5
         phoenix.damage *= 1.5
         opp = Element(name = "Air Monk", health = 100)
         print(f"ENEMY HEALTH {opp.health_max}")
         fight()
     elif opel == "Earth":
         print("ENEMY element is EARTH, beware")
         swoosh.damage *= 1.5
         aslice.damage *= 1.5
         cyclone.damage *= 1.5 
         opp = Element(name = "Earth Shaker", health = 100)
         print(f"ENEMY HEALTH {opp.health_max}")
         fight()
    
    

def fight():
     print("It's your turn to attack! Choose a move!")
     print(f"ENEMY HP:", {opp.health})
     print(f"YOUR HP:", {opp.health})
     if elsel == "Water":
         movesel = input(f"1 -- {splosh.name} \n2 -- {waterfall.name} \n3 -- {tsunami.name} \n")
         if movesel == "1":
             opp.health -= splosh.damage
             print(f"ENEMY HP",{opp.health})
         elif movesel == "2":
            opp.health -= waterfall.damage
            print(f"ENEMY HP",{opp.health})
         elif movesel == "3":
            opp.health -= tsunami.damage
            print(f"ENEMY HP",{opp.health})
       
     elif elsel == "Fire":
         movesel = input(f"1 -- {scorch.name} \n2 -- {firewall.name} \n3 -- {phoenix.name} \n")
         if movesel == "1":
             opp.health -= scorch.damage
             print(f"ENEMY HP",{opp.health})
         elif movesel == "2":
            opp.health -= firewall.damage
            print(f"ENEMY HP",{opp.health})
         elif movesel == "3":
            opp.health -= phoenix.damage
            print(f"ENEMY HP",{opp.health})
     elif elsel == "Earth":
         movesel = input(f"1 -- {crunch.name} \n2 -- {meteor.name} \n3 -- {fortress.name} \n")
     elif elsel == "Air":
         movesel = input(f"1 -- {swoosh.name} \n2 -- {aslice.name} \n3 -- {cyclone.name} \n")





     

     
     
     




    

def loading():
    yn = input("Do you wish to continue? Y/N\n")
    yn = yn.title()
    if yn == "Y" :
        print("LOADING GAME...")
        gameplay()
    elif yn == "N":
        print("MAIN MENU...")
        main()
    else:
        print("Retry")
        loading()

   

main()