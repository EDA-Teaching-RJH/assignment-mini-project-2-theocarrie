from element import Element 
from action import Action
import random
from random import choice 
myelwater = Element(name = "Water", health = 100)
myelfire = Element(name = "Fire", health = 100)
myelair = Element(name = "Air", health = 90)
myelearth = Element(name = "Earth", health = 120)
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
global opp
global myel

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
    elif elsel == "Earth":


        earth()
    elif elsel == "Air":


        air()

    
    else:
        print("Please choose a valid element:\n-Water \n-Fire \n-Earth \n-Air \n")
        elselect()

def water():
    myelwater = Element(name = "Water", health = 100)
    print("Water! Good choice, balanced and life sustaining, sure to wash away the competition! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Splosh \nDMG: 40\nWET: Target deals -20% DMG next turn\n")
    print("Waterfall \nDMG: 45\nCHURNING RAPIDS: Target takes +20% DMG next turn\n")
    print("Tsunami \nDMG: 55\nMUD: Target 55% Chance to miss next attack\n")
    print("HP", {myelwater.health})
    loading()

def fire():
    myelfire = Element(name = "Fire", health = 100)
    print("Fire! Exellent choice, aggressive ""Scorch 'n burn"" playstyle, sure to incinerate the competition! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Scorch \nDMG: 40\nBURN: Target takes 10 DMG for 2 turns \n")
    print("Firewall \nDMG: 20\nCOVERING FIRE: Negates 80% DMG taken next turn \n")
    print("Phoenix \nDMG: 70\nBURN: Heal 50% DMG dealt \n")
    print("HP", {myelfire.health})
    loading()

def earth():
    myelearth = Element(name = "Earth", health = 120)
    print("Earth! Wise choice, sturdy and immovable, sure to crush the competition to dust! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Crunch \nDMG: 50 \n")
    print("Meteor \nDMG: 60\nEXTINCTION: 35% chance to stun target, skipping their turn \n")
    print("Fortress \nDMG: 0\nLAST STAND: Takes 95% reduced DMG for 1 turn and 55% reduced DMG for 1 turn after \n")
    print("HP", {myelearth.health})
    loading()


def air():
    myelair = Element(name = "Air", health = 90)
    print("Air! Exciting choice, fast and agile, sure to fly above the competition! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Swoosh \nDMG: 35\nDODGE: 35% chance to evade next attack \n")
    print("Slice \nDMG: 55\nCRITICAL: 25% chance to do 2X DMG \n")
    print("Cyclone \nDMG: 40\nDIVINE WIND: 40% chance to dodge, 30% chance to do 1.5X DMG \n ")
    print("HP", {myelair.health})
    loading()


def gameplay():
     print("An ENEMY has appeared!")
     global opel
     opel = random.choice(["Fire", "Water","Air", "Earth"])
     if opel == "Fire":
         
         print("ENEMY element is FIRE, beware")
         opp = oppfire
         print(f"ENEMY HP: {opp.health_max}")
         fight()
     elif opel == "Water":
         
         print("ENEMY element is WATER, beware")
         opp = oppwater
         print(f"ENEMY HP: {opp.health_max}")
         fight()
     elif opel == "Air":
         
         print("ENEMY element is AIR, beware")
         opp = oppair
         print(f"ENEMY HP: {opp.health_max}")
         fight()
     elif opel == "Earth":
         
         print("ENEMY element is EARTH, beware")
         opp = oppearth
         print(f"ENEMY HP: {opp.health_max}")
         fightloop()
    
def fightloop():
    global myel
    global opp
    while myel.health > 0 and opp.health > 0:
        fight()

    if myel.health <= 0:
        print("\nYou have been defeated... better luck next time!")
    else:
        print("\nVICTORY! The enemy has been vanquished!")

        replay

def fight():
     print("It's your turn to attack! Choose a move!")
     global elsel
     elsel = elsel.title()
     if elsel == "Fire":
         
         
      
         myel = myelfire
         print(f"HP:", {myel.health_max})
        
     elif elsel == "Water":
         
         
      
         myel = myelwater
         print(f"HP:", {myel.health_max})
       
     elif elsel == "Air":
         
     
         myel = myelair
         print(f"HP:", {myel.health_max})
        
         
     elif elsel == "Earth":
         
         myel = myelearth
         print(f"HP:", {myel.health_max})
        
         
    
     
     
     
    
     
     
     if opel == "Fire":
         
         
         splosh.damage *= 1.5
         waterfall.damage *= 1.5
         tsunami.damage *= 1.5
         opp = oppfire
        
     elif opel == "Water":
         
         
         crunch.damage *= 1.5
         meteor.damage *= 1.5
         fortress.damage *= 1.5
         opp = oppwater
       
     elif opel == "Air":
         
         
         scorch.damage *= 1.5
         firewall.damage *= 1.5
         phoenix.damage *= 1.5
         opp = oppair
        
         
     elif opel == "Earth":
         
        
         swoosh.damage *= 1.5
         aslice.damage *= 1.5
         cyclone.damage *= 1.5 
         opp = oppearth
        
         
    
     
     print(f"ENEMY HP:", {opp.health})
     
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

      
     elif elsel == "Air":
         
         movesel = input(f"1 -- {swoosh.name} \n2 -- {aslice.name} \n3 -- {cyclone.name} \n")
         if movesel == "1":
             opp.health -= swoosh.damage
             print(f"ENEMY HP",{opp.health})
         elif movesel == "2":
            opp.health -= aslice.damage
            print(f"ENEMY HP",{opp.health})
         elif movesel == "3":
            opp.health -= cyclone.damage
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
         if movesel == "1":
             opp.health -= crunch.damage
             print(f"ENEMY HP",{opp.health})
         elif movesel == "2":
            opp.health -= meteor.damage
            print(f"ENEMY HP",{opp.health})
         elif movesel == "3":
            opp.health -= fortress.damage
            print(f"ENEMY HP",{opp.health})

     print(f"YOUR HP:", {myel.health})
#----------------------------------------------------------------------------------------------------------------------
# Menus
#----------------------------------------------------------------------------------------------------------------------
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

def replay():
    yn = input("Do you wish to continue? Y/N\n")
    yn = yn.title()
    if yn == "Y" :
        print("LOADING GAME...")
        main()
    elif yn == "N":
        print("THANKS FOR PLAYING :D")
        main()
    else:
        print("Retry")
        replay()


   

main()