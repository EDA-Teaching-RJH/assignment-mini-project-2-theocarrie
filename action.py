class Action:
    def __init__(self, name: str, damage: int, effect: str):
        self.name = name 
        self.damage = damage 
        self.effect = effect 


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
