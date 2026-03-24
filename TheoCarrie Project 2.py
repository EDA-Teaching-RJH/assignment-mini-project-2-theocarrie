element = ["Fire", "Water", "Earth", "Air"]
water = ["Splosh", "Waterfall","Tsunami"]
fire = ["Scorch", "Firewall", "Phoenix"]
earth = ["Crunch", "Meteor", "Fortress"]
air = ["Swoosh", "Slice", "Cyclone"]

print("LOADING...")
print("...")


def main():

    elselect()
    
    
def elselect():    
    print("Welcome to Elemenbrawl: choose your element: \n")
    element = input ("-Water \n-Fire \n-Earth \n-Air \n")
    element = element.title()
    if element == "Water":
        water()
    elif element == "Fire":
        fire()
    elif element == "Earth":
        earth()
    elif element == "Air":
        air()
    else:
        print("Please choose a valid element:\n-Water \n-Fire \n-Earth \n-Air \n")
        elselect()

def water():
    a = 1
    print(element[a]+"! Good choice, balanced and life sustaining, sure to wash away the competition! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Splosh \nDMG: 40\nWET: Target deals -20% DMG next turn\n")
    print("Waterfall \nDMG: 45\nCHURNING RAPIDS: Target takes +20% DMG next turn\n")
    print("Tsunami \nDMG: 55\nMUD: Target 55% Chance to miss next attack\n")
    loading()

def fire():
    a = 2
    print(element[a]+"! Exellent choice, aggressive ""Scorch 'n burn"" playstyle, sure to incinerate the competition! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Scorch \nDMG: 40\nBURN: Target takes 10 DMG for 2 turns \n")
    print("Firewall \nDMG: 20\nCOVERING FIRE: Negates 80% DMG taken next turn \n")
    print("Phoenix \nDMG: 70\nBURN: Heal 50% DMG dealt \n")
    loading()

def earth():
    a = 3
    print(element[a]+"! Wise choice, sturdy and immovable, sure to crush the competition to dust! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Crunch \nDMG: 50 \n")
    print("Meteor \nDMG: 60\nEXTINCTION: 35% chance to stun target, skipping their turn \n")
    print("Fortress \nDMG: 0\nLAST STAND: Takes 95% reduced DMG for 1 turn and 55% reduced DMG for 1 turn after \n")
    loading()


def air():
    a = 4
    print(element[a]+"! Exciting choice, fast and agile, sure to fly above the competition! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Swoosh \nDMG: 35\nDODGE: 35% chance to evade next attack \n")
    print("Slice \nDMG: 55\nCRITICAL: 25% chance to do 2X DMG \n")
    print("Cyclone \nDMG: 40\nDIVINE WIND: 40% chance to dodge, 30% chance to do 1.5X DMG \n ")
    loading()

#def gameplay():
     #print("An ENEMY has appeared!")
     #a = n
     #oHP = 150
     #mHP = 200
     #attack = input("Its your turn to attack!\n", action1[n]"\n", action2[n]"\n", action3[]"\n")

     #turn = 1
     #turn = turn + 1 



    

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