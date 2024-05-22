from items import fists
class Character():
  species = "Intern"
  def __init__(self, name: str, health: int):
    self.name = name
    self.health = health

    self.Items = fists
    
  def attack(self, target):
    target.health -= self.Items.damage
    target.health = max(target.health, 0)
    print(f"{self.name} dealt {self.Items.damage} damage towards {target.name} with "
          f"{self.Items.name}")

class Protag(Character):
  def __init__(self, name: str, health: int):
    super().__init__(name=name, health=health)

class Enemyone(Character):
  def __init__(self, name: str, health: int):
    super().__init__(name=name, health=health)
    
