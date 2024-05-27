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
from charactar import Enemytwo, Hrboss, Protag, Enemyone, Enemythree
from items import zippy

x_loc=0
y_loc=4

guy = Protag(name = "You", health=20)
enemyone = Enemyone(name="Unpaid Specialist", health=10)
enemytwo = Enemytwo(name = "Custodial Enigneer", health=20, weapon=zippy)
enemythree = Enemythree(name = "Executive Administator", health=30)
hrboss = Hrboss(name = "Human Resources", health=50)

mapfile = 'map.txt'
uifile = 'ui.txt'
fightfile = 'fight.txt'
gameoverfile = 'gameover.txt'

rooms = {
    "First": {
      "name" : "ROOM: Strange Room",
      "description" : """'There is a scent of blood. Proceed with caution'"""},

    "Second": {
      "name" : "ROOM: Strange Room",
      "description" : """'There is a scent of sweat. Proceed with caution'"""},

    "Last": {
      "name" : "ROOM: Strange Room",
      "description" : """'There is a scent of tears. Proceed with caution'"""},

    "Gag": {
      "name" : "ROOM: The Dungeon",
      "description" : "'The Cobblestone flooring does not match with the office'"},

    "FINAL": {
      "name" : "ROOM: Final Stage",
      "description" : "'If I go past this area, I should be prepared...'"},

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
      "description" : "'No darts, no pool cues... the pinnacle of relaxation'"},

    "IT Room": {
      "name" : "ROOM: IT Room",
      "description" : "[PRESS Q FOR TUTORIAL] 'Is there anything I need to know?'"},
  
    "Copy Room": {
      "name" : "ROOM: Copy Room",
      "description" : "'The printers here always smelled cold'"}
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

def roomdesc():
  if x_loc == 1 and y_loc == 0:
    print(rooms["First"]["name"])
    print("")
    print(rooms["First"]["description"])
  elif x_loc == 0 and y_loc == 1:
    print(rooms["Second"]["name"])
    print("")
    print(rooms["Second"]["description"])
  elif x_loc == 2 and y_loc == 2:
    print(rooms["Last"]["name"])
    print("")
    print(rooms["Last"]["description"])
  elif x_loc == 3 and y_loc == 0:
    print(rooms["Gag"]["name"])
    print("")
    print(rooms["Gag"]["description"])
  elif x_loc == 3 and y_loc == 1:
    print(rooms["FINAL"]["name"])
    print("")
    print(rooms["FINAL"]["description"])
  elif x_loc == 0 and y_loc == 0 or x_loc == 0 and y_loc == 4:
    print(rooms["Cubicles"]["name"])
    print("")
    print(rooms["Cubicles"]["description"]) 
  elif x_loc == 0 and y_loc == 2 or x_loc == 2 and y_loc == 1:
    print(rooms["Meeting Room"]["name"])
    print("")
    print(rooms["Meeting Room"]["description"])
  elif x_loc == 1 and y_loc == 2 or x_loc == 2 and y_loc == 0:
    print(rooms["Bathrooms"]["name"])
    print("")
    print(rooms["Bathrooms"]["description"])
  elif x_loc == 1 and y_loc == 1 or x_loc == 3 and y_loc == 2:
    print(rooms["Rec Room"]["name"])
    print("")
    print(rooms["Rec Room"]["description"])
  elif x_loc == 0 and y_loc == 3:
    print(rooms["IT Room"]["name"])
    print("")
    print(rooms["IT Room"]["description"])
  elif x_loc == 1 and y_loc == 3:
    print(rooms["Copy Room"]["name"])
    print("")
    print(rooms["Copy Room"]["description"])


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
  elif direction =="q":
    if x_loc == 1 and y_loc == 0: #First
      input("'You stumble across a man with a gaunt appearance': ")
      input("'He looks very easy to kill':  ")
      while True:
        fightchoice = input("[1] FIGHT      [2] LEAVE : ")
        if fightchoice == "1":
          printfight()
          break
        elif fightchoice == "2":
          break
        else:
          pass
        print("")
    elif x_loc == 0 and y_loc == 1:
      input("'You stumble across a man with a repulsive appearance': ")
      input("'He looks difficult to kill': ")
      while True:
        fightchoice = input("[1] FIGHT      [2] LEAVE : ")
        if fightchoice == "1":
          printfight()
          break
        elif fightchoice == "2":
          break
        else:
          pass
    elif x_loc == 2 and y_loc == 2:
      input("'You stumble across a man with a brutish appearance': ")
      input("'He looks very difficult to kill': ")
      while True:
        fightchoice = input("[1] FIGHT      [2] LEAVE : ")
        if fightchoice == "1":
          printfight()
          break
        elif fightchoice == "2":
          break
        else:
          pass
    elif x_loc == 3 and y_loc == 0: #Gag
      print("'I hate you and never come back'")
    else:
      input("Theres nothing here of interest... ")
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

def printfight():
  global x_loc, y_loc
  if guy.health <= 0:
    with open(gameoverfile) as file:
      print(file.read())
      quit()
  if x_loc == 1 and y_loc == 2:
    while True:
      with open(fightfile) as file:
        print(file.read())
        guy.attack(enemyone)
        enemyone.attack(guy)
        print(f"Health of {guy.name}: {guy.health}")
        print(f"Health of {enemyone.name}: {enemyone.health}")
        fightchoice = input("[1] ATTACK     [2] LEAVE: ")
        if fightchoice == '1':
          pass
        elif fightchoice == '2':
          break
        else:
          pass
        if guy.health <= 0:
          with open(gameoverfile) as file:
            print(file.read())
            quit()
        if enemyone.health <= 0:
          break

  if x_loc == 0 and y_loc == 1:
    while True:
      with open(fightfile) as file:
        print(file.read())
        guy.attack(enemytwo)
        enemytwo.attack(guy)
        print(f"Health of {guy.name}: {guy.health}")
        print(f"Health of {enemytwo.name}: {enemytwo.health}")
        fightchoice = input("[1] ATTACK     [2] LEAVE: ")
        if fightchoice == '1':
          pass
        elif fightchoice == '2':
          break
        else:
          pass
        if enemytwo.health <= 0:
          break
        if guy.health <= 0:
          with open(gameoverfile) as file:
            print(file.read())
            quit()

  if x_loc == 2 and y_loc == 2:
    while True:
      with open(fightfile) as file:
        print(file.read())
        guy.attack(enemythree)
        enemythree.attack(guy)
        print(f"Health of {guy.name}: {guy.health}")
        print(f"Health of {enemythree.name}: {enemythree.health}")
        fightchoice = input("[1] ATTACK     [2] LEAVE: ")
        if fightchoice == '1':
          pass
        elif fightchoice == '2':
          break
        else:
          pass
        if enemythree.health <= 0:
          break
        if guy.health <= 0:
          with open(gameoverfile) as file:
            print(file.read())
            quit()
  if x_loc == 4 and y_loc == 1:
   while True:
      with open(fightfile) as file:
        print(file.read())
        guy.attack(hrboss)
        hrboss.attack(guy)
        print(f"Health of {guy.name}: {guy.health}")
        print(f"Health of {hrboss.name}: {hrboss.health}")
        fightchoice = input("[1] ATTACK     [2] LEAVE: ")
        if fightchoice == '1':
          pass
        elif fightchoice == '2':
          break
        else:
          pass
        if hrboss.health <= 0:
          break
        if guy.health <= 0:
          with open(gameoverfile) as file:
            print(file.read())
            quit()

def printmap():
  while True:
    with open(mapfile) as file:
      print(file.read())
    print("COORDINATES: ",f"{x_loc}, {y_loc}")
    print("")
    roomdesc()
    with open(uifile) as file:
      print(file.read())

      choice = input("Choice: ")

    movement(choice)
    restrictions()
    if x_loc == 4 and y_loc == 1:
      printfight()
      print("BOSS FIGHT")
      break
printmap()