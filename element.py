class Element:
    def __init__(self, name: str, health: int):
        self.name = name 
        self.health = health
        self.health_max = health
        
    
    def action(self, target):
        target.hp -= self.damage
        target.hp = max(target.hp, 0)

water = Element(name = "Water", health = 100)
air = Element(name = "Air", health = 90)
fire = Element(name = "Fire", health = 100)
earth = Element(name = "Earth", health = 120)


