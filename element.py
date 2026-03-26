import random
class Element:
    def __init__(self, name: str, health: int):
        self.name = name 
        self.health = health
        self.health_max = health
        self.status = []

    def take_damage(self, dmg):

        for effect in self.status:
            if effect["type"] == "shield":
                print(f"{self.name}'s shield blocks some damage!")
                dmg *= 0.5

        for effect in self.status:
            if effect["type"] == "dodge":
                print(f"{self.name} dodged!")
                self.status.remove(effect)
                return

        self.health -= int(dmg)
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += int(amount)
        if self.health > self.health_max:
            self.health = self.health_max

    def apply_status(self):
        for effect in self.status[:]:
            if effect["type"] == "burn":
                print(f"{self.name} takes 10 burn damage!")
                self.take_damage(10)
                effect["turns"] -= 1

            if effect["type"] == "stun":
                effect["turns"] -= 1

            if effect["turns"] <= 0:
                self.status.remove(effect)

    def is_stunned(self):
        return any(effect["type"] == "stun" for effect in self.status)

    def is_alive(self):
        return self.health > 0
    

class WaterElement(Element):
    def __init__(self):
        super().__init__("Water", 100)
        self.actions = {
            "1": ("Splosh", 40, self.splosh),
            "2": ("Waterfall", 45, self.waterfall),
            "3": ("Tsunami", 55, self.tsunami)
            
        }
    def splosh(self, enemy):
        print("WET- Enemy weakened!")

    def waterfall(self, enemy):
        print("CHURNING RAPIDS- Enemy takes increased damage next turn!")

    def tsunami(self, enemy):
        if random.random() < 0.5:
            print("MUD- Enemy stunned!")
            enemy.status.append({"type": "stun", "turns":1})


class AirElement(Element):
    def __init__(self):
        super().__init__("Air", 90)
        self.actions = {
            "1": ("Swoosh", 35, self.swoosh),
            "2": ("Slice", 55, self.slice),
            "3": ("Cyclone", 40, self.cyclone)

        }

    def swoosh(self, enemy):
        if random.random() < 0.35:
            print("DODGE- You will dodge the next attack")
            self.status.append({"type": "dodge", "turns": 1})

    def slice(self, enemy):
        if random.random() < 0.25:
            print("CRITICAL!")
            enemy.take_damage(55)

    def cyclone(self, enemy):
        if random.random() < 0.4:
            print("DIVINE WIND- Dodge ready!")
            self.status.append({"type": "dodge","turns": 1})

class EarthElement(Element):
    def __init__(self):
        super().__init__("Earth", 120)
        self.actions = {
            "1": ("Crunch", 50, self.crunch),
            "2": ("Meteor", 60, self.meteor),
            "3": ("Fortress", 0, self.fortress)

        }

    def crunch(self, enemy):
        pass

    def meteor(self, enemy):
        if random.random() < 0.35:
            print("EXTINCTION landed!")
            enemy.status.append({"type": "stun","turns": 1})

    def fortress(self, enemy):
        print("LAST STAND!")
        self.status.append({"type": "shield","turns": 2})
                           

class FireElement(Element):
    def __init__(self): 
        super().__init__("Fire", 100)
        self.actions = {
            "1": ("Scorch", 40, self.scorch),
            "2": ("Firewall", 20, self.firewall),
            "3": ("Phoenix", 70, self.phoenix)

        }

    def scorch(self, enemy):
        print("BURN- Burn applied!")
        enemy.status.append({"type": "burn","turns": 2})

    def firewall(self, enemy):
        print("COVER FIRE- Damage reduction in effect next turn!")
        self.status.append({"type": "shield","turns": 1})

    def phoenix(self, enemy):
        heal_amount = 35
        print(f"PHOENIX- Phoenix heals {heal_amount}!")
        self.heal(heal_amount)

                           




    




