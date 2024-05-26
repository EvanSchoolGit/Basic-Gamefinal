#WEEKEND'S CHECKLIST - INVENTORY SYSTEM, PATCH MAP, ENEMY SYSTEM, BOSS.


########################################################################
# Title : RPG game
# Class : Computer Science 30
# Assighnment : make a game
# Coder : Evan Urban
# Version : 1
########################################################################
""" 
Fill me out!!!!!
"""
########################################################################
from charactar import Protag, Enemyone 

x_loc=0
y_loc=4

guy = Protag(name = "You", health=10)
enemyone = Enemyone(name="Unpaid Specialist", health=10)
mapfile = 'map.txt'
uifile = 'ui.txt'

rooms = {
    "First": {
      "name" : "ROOM: first",
      "description" : """Ooooooo mama mia, I am the first riddel master"""},

    "Second": {
      "name" : "ROOM: Second",
      "description" : """Ooooooo mama mia, I am the second riddel master"""},

    "Last": {
      "name" : "ROOM: Last",
      "description" : """Ooooooo mama mia, I am the Last riddel master"""},

    "Gag": {
      "name" : "ROOM: gag",
      "description" : "Get GAGGED idiot!"},

    "FINAL": {
      "name" : "ROOM: Final",
      "description" : "Get FINALED idiot!"},

    "Cubicles": {
      "name" : "ROOM: Cubicles",
      "description" : "'This place was always so boring'"},

    "Bathrooms": {
      "name" : "ROOM: Bathrooms",
      "description" : "'I don't think this place has any importance to me'"},

    "Meeting Room": {
      "name" : "ROOM: Meeting Room",
      "description" : "'Theres still cobwebs here...'"},

    "Rec Room": {
      "name" : "ROOM: Rec Room",
      "description" : "'No darts, no pool cues... the perfect rec room'"}
}

def intro():
  input("'Yeah': ")
  print("")
  input("'Ohhhhhhhh yeah': ")
  print("")
  input("'You got the mindset, baby': ")
  print("")
  input("'-And the mindset make you a real go-getter': ")
  print("")
  input("'Hustle, Currency, Stocks, Digitization, Cryptistical, Corpotocracy': ")
  print("")
  input("'Thats called mindset, baby': ")
  print("")
  input("'-and mindset make you a real go-getter': ")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("a real go-getter")
  print("")
  input("You wake up to your office: ")
  input("a real go-getter?: ")


def movement(direction): 
  global x_loc, y_loc
  if direction == "a": #GOOD
    x_loc-= 1
  elif direction == "d": #PROBLEM
    x_loc+= 1
  elif direction == "w": #KINDA GOOD
    y_loc-= 1
  elif direction == "s": #PROBLEM
    y_loc+= 1
  elif direction == ("X"):
    print("Now quiting...")
    quit()

def restrictions():
  global x_loc, y_loc
  if x_loc == -1:
    x_loc += 1
  elif x_loc == 4 and y_loc == 0 or x_loc ==4 and y_loc == 2:
    x_loc -= 1
  elif x_loc == 4 and y_loc == 3 or x_loc == 0 and y_loc == 5:
    y_loc -= 1
  elif y_loc == -1:
    y_loc += 1
intro()
def printmap():
  while True:
    try:
      with open(mapfile) as file:
        print(file.read())
      print("COORDINATES: ",f"{x_loc}, {y_loc}")
      print("")
      with open(uifile) as file:
        print(file.read())
        choice = input("Choice: ")
    except Exception as e:
      printWAH
  try:
    movement(choice)
    restrictions()
  finally:
    pass
    
  #while True:
    #guy.attack(enemyone)
    #enemyone.attack(guy)
    
    #print(f"Health of {guy.name}: {guy.health}")
    #print(f"Health of {enemyone.name}: {enemyone.health}")
    #input("CLICK: ")
    #pass