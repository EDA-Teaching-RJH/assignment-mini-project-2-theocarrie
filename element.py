import random
class Element:
    """
    Base class for all playable elements.
    Holds shared attributes.
    All elements inherit from this class.
    """
    def __init__(self, name: str, health: int):
        """
        Initialises name and health at the beginning of the game 
        health_max ensures the player cannot overheal above max (starting) healthpool.
        Status includes all applied effects.
        """
        self.name = name 
        self.health = health
        self.health_max = health
        self.status = []

    def take_damage(self, dmg):
        """
        Reduces health by the appropriate damage value.
        Shield blocks half of all damage (1 turn).
        Dodge evades all damage (1 turn).
        """

        for effect in self.status:
            if effect["type"] == "shield":
                print(f"{self.name}'s shield is ready!")
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
        """
        Increases health by certian amount.
        Capped at max_health to prevent overheal
        """
        self.health += int(amount)
        if self.health > self.health_max:
            self.health = self.health_max

    def apply_status(self):
        """
        Called at the beginning of each round to count down the turns remaining on effects.
        When turns left <= 0, removes effect
        """
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
        """
        Returns true if player/enemy has active stun effect.
        Decides whether player/enemy will get a turn or not.
        """
        return any(effect["type"] == "stun" for effect in self.status)

    def is_alive(self):
        """
        Returns true if player/enemy has health remaining (is not dead).
        """
        return self.health > 0
    

class WaterElement(Element):
    """
    Water Element 
    Inherits all base methods from Element 
    Moves: Splosh, Waterfall, Tsunami
    """
    def __init__(self):
        super().__init__("Water", 500)
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
    """
    Air Element 
    Inherits all base methods from Element 
    Moves: Swoosh, Slice, Cyclone
    """
    def __init__(self):
        super().__init__("Air", 450)
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
    """
    Earth Element 
    Inherits all base methods from Element 
    Moves: Crunch, Meteor, Fortress
    """
    def __init__(self):
        super().__init__("Earth", 600)
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
    """
    Fire Element 
    Inherits all base methods from Element 
    Moves: Scorch, Firewall, Phoenix
    """
    def __init__(self): 
        super().__init__("Fire", 450)
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

                           




    




