from element import Element 
from action import Action
water = Element(name = "Water", health = 100)
fire = Element(name = "Fire", health = 100)


print("LOADING...")
print("...")


def main():

    elselect()
    
    
def elselect():    
    print("Welcome to Elemenbrawl: choose your element: \n")
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
    water = Element(name = "Water", health = 100)
    
    print("Water! Good choice, balanced and life sustaining, sure to wash away the competition! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Splosh \nDMG: 40\nWET: Target deals -20% DMG next turn\n")
    print("Waterfall \nDMG: 45\nCHURNING RAPIDS: Target takes +20% DMG next turn\n")
    print("Tsunami \nDMG: 55\nMUD: Target 55% Chance to miss next attack\n")
    print("HP", {water.health})
    loading()

def fire():
    fire = Element(name = "Fire", health = 100)
    print("Fire! Exellent choice, aggressive ""Scorch 'n burn"" playstyle, sure to incinerate the competition! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Scorch \nDMG: 40\nBURN: Target takes 10 DMG for 2 turns \n")
    print("Firewall \nDMG: 20\nCOVERING FIRE: Negates 80% DMG taken next turn \n")
    print("Phoenix \nDMG: 70\nBURN: Heal 50% DMG dealt \n")
    print("HP", {fire.health})
    loading()

# def earth():
#     a = 3
#     print(element[a]+"! Wise choice, sturdy and immovable, sure to crush the competition to dust! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
#     print("Crunch \nDMG: 50 \n")
#     print("Meteor \nDMG: 60\nEXTINCTION: 35% chance to stun target, skipping their turn \n")
#     print("Fortress \nDMG: 0\nLAST STAND: Takes 95% reduced DMG for 1 turn and 55% reduced DMG for 1 turn after \n")
#     loading()


# def air():
#     a = 4
#     print(element[a]+"! Exciting choice, fast and agile, sure to fly above the competition! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
#     print("Swoosh \nDMG: 35\nDODGE: 35% chance to evade next attack \n")
#     print("Slice \nDMG: 55\nCRITICAL: 25% chance to do 2X DMG \n")
#     print("Cyclone \nDMG: 40\nDIVINE WIND: 40% chance to dodge, 30% chance to do 1.5X DMG \n ")
#     loading()

def gameplay():
     print("An ENEMY has appeared!")
     print("hp", {water.health})
     
     
     




    

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