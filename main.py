#WEEKEND'S CHECKLIST - INVENTORY SYSTEM

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
###########################-IMPORTS-############################################
from charactar import Enemytwo, Hrboss, Protag, Enemyone, Enemythree
from items import zippy, gakle, astra_revolver, fists
############################-SETUP-#############################################
x_loc=0
y_loc=4

guy = Protag(name = "You", health=20, weapon=fists, weapondesc="fists")
enemyone = Enemyone(name="Unpaid Specialist", health=10)
enemytwo = Enemytwo(name = "Custodial Enigneer", health=18, weapon=zippy)
enemythree = Enemythree(name = "Executive Administator", health=30, weapon=zippy)
hrboss = Hrboss(name = "Human Resources", health=45, weapon=astra_revolver)

mapfile = 'map.txt'
uifile = 'ui.txt'
fightfile = 'fight.txt'
gameoverfile = 'gameover.txt'
promotedfile = 'promoted.txt'

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
##############################-MAIN####################################################

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

def end():
  input("'You did it'")
  input("'Im so proud of you'")
  input("'You truly are a Go-Getter'")
  input("'Enjoy your promotion!'")
  with open(promotedfile) as file:
    print(file.read())
    quit()

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
    elif x_loc == 0 and y_loc == 3:
      input("'HELLO FELLOW EMPLOYEE': ")
      print("")
      print("'PLEASE EXTERMINATE ALL OF THOSE UGGOS IN THEIR OFFICES'")
      input("[Pressing q within Strange Rooms]: ")
      print("")
      input("'SOME ARE STRONGER THAN OTHERS SO I RECCOMEND USING COMPANY RESOURCES': ")
      print("")
      print("'THESE CAN BE FOUND WITHIN THE BUILDING'")
      input("[Press q in some rooms can give you items or bonuses")
      print("")
      input("'ONCE YOU'VE FINISHED YOUR TASK REPORT TO HR IMMEDIATELY': ")
      print("")
      input("'THANK YOU FOR COOPERATING'")
    
    elif x_loc == 0 and y_loc == 0 and guy.Items == fists:
      input("'You begin rummaging throughout the cubicles':  ")
      input("'You found a Zippy!'")
      guy.Items = zippy

    elif x_loc == 0 and y_loc == 2 or x_loc == 1 and y_loc == 3:
      input("'PSST': ")
      input("'Yo... could you help me real quick...': ")
      input("'I lost my weapon in the Cubicles again...': ")
      input("'Could you get it for me?': ")
      input("'It's at (0,0)': ")
      input("'WHAT ARE YOU STANDING FOR! GO GET IT': ")

    elif x_loc == 2 and y_loc == 1 or x_loc == 1 and y_loc == 1:
      input("A Green and Stout individual waddles up to you: ")
      input("He is wearing fake glasses with fake a nose...: ")
      input("'HELLO WEALTHY MAN': ")
      input("'I've heard you were going through the QUEST and ADVENTURE': ")
      input("'As a fellow employee, I shall give RUMORS and GOSSIP': ")
      input("'I heard that if you have a Zippy with you, you can make millions': ")
      input("'THEYRE GIVING OUT GOLD, EMPLOYEE': ")
      input("'All you need to do is proceed to THE DUNGEON': ")
      input("'GOOD LUCK EMPLOYEE': ")
      input("He waddles away...: ")

    elif x_loc == 3 and y_loc == 0 and guy.Items == zippy:
      input("A Green and Stout individual waddles up to you: ")
      input("'HELLO WEALTHY MAN': ")
      input("He punches you in the gut")
      input("'GOODBYE EMPLOYEE': ")
      input("'He ran away...': ")
      input("*YOU LOST ZIPPY")
      input("You notice something on the ground...: ")
      input("*YOU GAIN AN ASTRA REVOLVER: ")
      guy.Items = astra_revolver
    elif x_loc == 3 and y_loc == 1:
      input("I should only go past here if I have done everything here...: ")
    else:
      input("Theres nothing here of interest... ")
  elif direction == ("X"):
    print("Now quiting...")
    quit()
  elif direction == ("e"):
    guy.descrbing()

def restrictions():
  global x_loc, y_loc
  if x_loc==-1:
    x_loc+=1
  elif x_loc==4 and y_loc==0 or x_loc==4 and y_loc==2 or x_loc==1 and y_loc==4:
    x_loc-=1
  elif x_loc==4 and y_loc==3 or x_loc==0 and y_loc==5 or x_loc==2 and y_loc==3:
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
  if x_loc == 1 and y_loc == 0:
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
        if guy.health == 0:
          with open(gameoverfile) as file:
            print(file.read())
            quit()
        if enemyone.health == 0:
          guy.health = 20
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
        if enemytwo.health == 0:
          guy.health = 20
          break
        if guy.health == 0:
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
          input("'It seems that something has dropped after the battle...': ")
          input("'You've obtained a Gakle!")
          guy.Items = gakle
          guy.health = 20
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
          end()
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

###########################################################################################