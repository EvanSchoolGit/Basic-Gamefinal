class Items():
  def __init__(self, name: str, description: str, damage: int) -> None:
    self.name = name
    self.description = description
    self.damage = damage
  pass

astra_revolver = Items(name="Astra 680 Magnum Revolver",
                       damage=5,
                       description="a decent, but slightly inaccurate handgun.")
zippy = Items(name="Zippy HE55",
              damage=2,
              description="a weak pellet shooter, that has a chance of jamming easily")
gakle = Items(name = "g-AKle 5959",
              damage=10,
              description="a long hunting rifle with no apparent faults")
fists = Items(name= "Fists",
              damage=1,
              description="a gross pair of spotted knuckles, fitted with your hands")