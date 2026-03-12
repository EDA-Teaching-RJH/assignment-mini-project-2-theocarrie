element = ["Fire", "Water", "Earth", "Air"]
action1 = ["Splosh", "Scorch", "Crunch", "Swoosh"]
action2 = [" Waterfall", "Firewall", "Meteor", "Slice"]
action3 = ["Tsunami", "Phoenix", "Fortress", "Cyclone"]

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
    print("Water! Good choice, balanced and life sustaining, sure to wash away the competition! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Splosh \nDMG: 40\nWET: Target deals -20% DMG next turn")
    print("Waterfall \nDMG: 45\nCHURNING RAPIDS: Target takes +20% DMG next turn")
    print("Tsunami \nDMG: 55\nMUD: Target 55% Chance to miss next attack")
    

def fire():
    print("Fire! Exellent choice, aggressive ""Scorch 'n burn"" playstyle, sure to incinerate the competition! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Scorch \nDMG: 40\nBURN: Target takes 10 DMG for 2 turns")
    print("Firewall \nDMG: 20\nCOVERING FIRE: Negates 80% DMG taken next turn")
    print("Phoenix \nDMG: 70\nBURN: Heal 50% DMG dealt")
    

def earth():
    print("Earth! Wise choice, sturdy and immovable, sure to crush the competition to dust! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Crunch \nDMG: 50")
    print("Meteor \nDMG: 60\nEXTINCTION: 35% chance to stun target, skipping their turn")
    print("Fortress \nDMG: 0\nLAST STAND: Takes 95% reduced DMG for 1 turn and 55% reduced DMG for 1 turn after")

def air():
    print("Air! Exciting choice, fast and agile, sure to fly above the competition! \nTHREE actions have been granted to you which will be availble to use on your turn. \n")
    print("Swoosh \nDMG: 35\nDODGE: 35% chance to evade next attack")
    print("Slice \nDMG: 55\nCRITICAL: 25% chance to do 2X DMG")
    print("Tornado \nDMG: 40\nDIVINE WIND: 40% chance to dodge, 30% chance to do 1.5X DMG  ")


main()