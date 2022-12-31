print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a cross road.Where do you want to go? Type \"Left\" or \"Right\"")
a=input("->")
if a=="Left":
    pass
if a=="Right":
    print("Game Over")
print("You come to a lake. There is an island in the middle of the lake. Type \"Wait\" to wait for a boat. Type \"Swim\" to swim across.")
b=input("->")
if b=="Wait":
    pass
if b=="Swim":
    print("Game Over")
print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour door did you choose:")
c=input("->")
if c=="Red":
    print("You have entered in the jungle and died!")
    print("Game Over")
if c=="Blue":
    print("You have entered in to the room full of beasts and you died!")
    print("Game Over")
if c=="Yellow":
    print("Hooray! You win the game.")