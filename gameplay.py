

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
elselect()
