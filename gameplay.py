from element import FireElement, WaterElement, AirElement, EarthElement 
import random
import re
import csv




global opp
global myel

print("LOADING...")
print("...")
def get_advantage(atta, defe):
    if atta.name == "Fire" and defe.name == "Air":
        return 1.5
    if atta.name == "Water" and defe.name == "Fire":
        return 1.5
    if atta.name == "Earth" and defe.name == "Water":
        return 1.5
    if atta.name == "Air" and defe.name == "Earth":
        return 1.5
    return 1
#----------------------------------------------------------------------------------------------------------------------
# Element Selection
#----------------------------------------------------------------------------------------------------------------------

def main():

    elselect() 
    
    
def elselect():    
    print("Welcome to Elemenbrawl: choose your element: \n")
    global elsel
    
    elsel = input ("-Water \n-Fire \n-Earth \n-Air \n").strip().title()
   
    
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
    global myel
    myel = WaterElement()
    print("Water! Good choice, balanced and life sustaining, sure to wash away the competition! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Splosh \nDMG: 40\nWET: Target deals -20% DMG next turn\n")
    print("Waterfall \nDMG: 45\nCHURNING RAPIDS: Target takes +20% DMG next turn\n")
    print("Tsunami \nDMG: 55\nMUD: Target 55% Chance to miss next attack\n")
    print("HP", myel.health)
    loading()

def fire():
    global myel
    myel = FireElement()
    print("Fire! Exellent choice, aggressive ""Scorch 'n burn"" playstyle, sure to incinerate the competition! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Scorch \nDMG: 40\nBURN: Target takes 10 DMG for 2 turns \n")
    print("Firewall \nDMG: 20\nCOVERING FIRE: Negates 80% DMG taken next turn \n")
    print("Phoenix \nDMG: 70\nBURN: Heal 50% DMG dealt \n")
    print("HP", myel.health)
    loading()

def earth():
    global myel
    myel = EarthElement()
    print("Earth! Wise choice, sturdy and immovable, sure to crush the competition to dust! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Crunch \nDMG: 50 \n")
    print("Meteor \nDMG: 60\nEXTINCTION: 35% chance to stun target, skipping their turn \n")
    print("Fortress \nDMG: 0\nLAST STAND: Takes 95% reduced DMG for 1 turn and 55% reduced DMG for 1 turn after \n")
    print("HP", myel.health)
    loading()


def air():
    global myel
    myel = AirElement()
    print("Air! Exciting choice, fast and agile, sure to fly above the competition! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Swoosh \nDMG: 35\nDODGE: 35% chance to evade next attack \n")
    print("Slice \nDMG: 55\nCRITICAL: 25% chance to do 2X DMG \n")
    print("Cyclone \nDMG: 40\nDIVINE WIND: 40% chance to dodge, 30% chance to do 1.5X DMG \n ")
    print("HP", myel.health)
    loading()

#----------------------------------------------------------------------------------------------------------------------
# Gameplay
#----------------------------------------------------------------------------------------------------------------------

def gameplay():
     global opel, opp
     print("An ENEMY has appeared!")
     opel = random.choice(["Fire", "Water","Air", "Earth"])
     if opel == "Fire":
         
         print("ENEMY element is FIRE, beware")
         opp = FireElement()
     elif opel == "Water":
         
         print("ENEMY element is WATER, beware")
         opp = WaterElement()
     elif opel == "Air":
         
         print("ENEMY element is AIR, beware")
         opp = AirElement()
     elif opel == "Earth":
         
         print("ENEMY element is EARTH, beware")
         opp = EarthElement()
     print(f"ENEMY HP: {opp.health}")
     fightloop()
    
def fightloop():
    global myel, opp
    while myel.health > 0 and opp.health > 0:
        fight()

    if myel.health <= 0:
        print("\nYou have been defeated... better luck next time!")
    else:
        print("\nVICTORY! The enemy has been vanquished!")

        replay()

def fight():
     global myel, opp

     print("It's your turn to attack!") 

     myel.apply_status()
     opp.apply_status()

     if opp.health <= 0:
         return

     if myel.is_stunned():
        print("You are stunned")
     else:
        print(f"YOUR HP: {myel.health}")
        print(f"ENEMY HP: {opp.health}")

        print("\nChoose a move!")

        for key, (name, dmg, _) in myel.actions.items():
            print(f"{key} -- {name} ({dmg} dmg)")

        choice = input(">")

        if choice in myel.actions:
            name, dmg, effect = myel.actions[choice]

            advantage = get_advantage(myel, opp)
            ad_dmg = int(dmg * advantage)
            if advantage > 1:
                print(f"Elemental advantage! Damage increased to {ad_dmg}")
            
            print(f"\nYou used {name}!")

            opp.take_damage(ad_dmg)
            effect(opp)

            print(f"ENEMY HP: {opp.health}")
        else:
            print("Invalid action")

        if opp.health <= 0:
            return
        

     print("ENEMY TURN")

     if opp.is_stunned():
        print("Enemy is stunned!")
        return
        
     action = random.choice(list(opp.actions.values()))
     name, dmg, effect = action

     advantage = get_advantage(opp, myel)
     ad_dmg = int(dmg * advantage)
     if advantage > 1:
                print(f"Enemy has elemental advantage! Damage increased to {ad_dmg}")
            
     
     print(f"Enemy used {name}!")
     
     myel.take_damage(ad_dmg)
     effect(myel)
     
     
     print(f"YOUR HP: {myel.health}")
        
   
#----------------------------------------------------------------------------------------------------------------------
# Menus
#----------------------------------------------------------------------------------------------------------------------
def loading():
    yn = input("Do you wish to continue? Y/N\n").strip().title()
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
    yn = input("Do you wish to continue? Y/N\n").strip().title()
    if yn == "Y" :
        print("LOADING GAME...")
        main()
    elif yn == "N":
        print("THANKS FOR PLAYING :D")
    else:
        print("Retry")
        replay()


   

main()