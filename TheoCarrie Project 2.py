element = ["Fire", "Water", "Earth", "Air"]
action1 = ["Splosh", "Scorch", "Crunch", "Swoosh"]
action2 = [" Waterfall", "Firewall", "Meteor", "Slice"]
action3 = ["Tsunami", "Phoenix", "Fortress", "Cyclone"]
sel = [1, 2, 3, 4]
print("LOADING...")
print("...")


def main():
    print("Welcome to Elemenbrawl: choose your element: \n")
    element = input ("-Water \n-Fire \n-Earth \n-Air \n")
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

def water():
    sel == 1
    print(element[sel],"! Good choice, balanced and life sustaining, sure to wash away the competition! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Splosh \nDMG: 40\nWET: Target deals -20% DMG next turn")
    print("Waterfall \nDMG: 45\nCHURNING RAPIDS: Target takes +20% DMG next turn")
    print("Tsunami \nDMG: 55\nMUD: Target 55% Chance to miss next attack")
    loading()

def fire():
    a = 2
    print("Fire! Exellent choice, aggressive ""Scorch 'n burn"" playstyle, sure to incinerate the competition! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Scorch \nDMG: 40\nBURN: Target takes 10 DMG for 2 turns")
    print("Firewall \nDMG: 20\nCOVERING FIRE: Negates 80% DMG taken next turn")
    print("Phoenix \nDMG: 70\nBURN: Heal 50% DMG dealt")
    gameplay()

def earth():
    a = 3
    print("Earth! Wise choice, sturdy and immovable, sure to crush the competition to dust! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Crunch \nDMG: 50")
    print("Meteor \nDMG: 60\nEXTINCTION: 35% chance to stun target, skipping their turn")
    print("Fortress \nDMG: 0\nLAST STAND: Takes 95% reduced DMG for 1 turn and 55% reduced DMG for 1 turn after")
    gameplay()


def air():
    a = 4
    print("Air! Exciting choice, fast and agile, sure to fly above the competition! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Swoosh \nDMG: 35\nDODGE: 35% chance to evade next attack")
    print("Slice \nDMG: 55\nCRITICAL: 25% chance to do 2X DMG")
    print("Cyclone \nDMG: 40\nDIVINE WIND: 40% chance to dodge, 30% chance to do 1.5X DMG  ")
    gameplay()

def gameplay():
    cont = input("CONTINUE TO ARENA? \nY/N")
    if cont == "Y":
        print("Ready to fight OPPONENT!")
        fight()

    elif cont == "N":
        print("Returning to Element Selector")
        main()
        
    else:
        print("Please type Y(Yes) or N(NO)")
        gameplay()

def fight():
    oHP = 200
    sHP = 200
    print("YOUR TURN")
    breakpoint

def loading():
    yn = input("Do you wish to continue? Y/N")
    if yn == "Y":
        print("LOADING GAME")
        gameplay()
    elif yn == "N":
        print("MAIN MENU...")
        main()
    else:
        print("Retry")
        loading

   

main()