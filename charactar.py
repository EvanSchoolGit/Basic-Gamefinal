from items import fists
class Character():
  species = "Intern"
  def __init__(self, name: str, health: int):
    self.name = name
    self.health = health
    
    self.Items = fists
    self.itemsdesc = fists
    
  def attack(self, target):
    target.health -= self.Items.damage
    target.health = max(target.health, 0)
    print(f"{self.name} dealt {self.Items.damage} damage towards {target.name} with "
          f"{self.Items.name}")
  def descrbing(self):
    print(f"NAME: {self.Items.name}")
    print(f"DAMAGE: {self.Items.damage}")
    print(f"DESCRIPTION: {self.Items.description}")
    input("COUNTINUE: ")

class Protag(Character):
  def __init__(self, name: str, health: int, weapon, weapondesc: str):
    super().__init__(name=name, health=health)
    self.Items = weapon
    self.itemsdesc = weapondesc

class Enemyone(Character):
  def __init__(self, name: str, health: int):
    super().__init__(name=name, health=health)

class Enemytwo(Character):
  def __init__(self, name: str, health: int, weapon):
    super().__init__(name=name, health=health)
    self.Items = weapon

class Enemythree(Character):
  def __init__(self, name: str, health: int, weapon):
    super().__init__(name=name, health=health)
    self.Items = weapon
    
class Hrboss(Character):
  def __init__(self, name: str, health: int, weapon):
    super().__init__(name=name, health=health)
    self.Items = weapon