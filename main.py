"""
LEVEL : B E G I N N E R.
-----------------------------------------------------------
Project - Treasure Island game using conditional statemnet.
-----------------------------------------------------------
Functions Used:
* Print - Prints a string into the console. || ex: print("Hello World").
* Input - Prints a string into the console, and asks the user for a string input. || ex: name = input("What's your name").

Conditional Statement:
* if-else
"""


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
print("Your mission is to find the treasure.\n") 

print("(HINT : By which hand you can hold your right elbo)")
turn = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")
if turn == "left":
    print("(HINT : What do you do when the traffic light turns red)")
    dec1= input("You come to a lake. there is an island in the middle of the lake. Type 'wait' to wait for a boat. Type'swim' to swim across.\n")
    if dec1 == "wait":
        print("HINT : What color is a ripe banana")
        dec2= input("You arrive at the island unharmed. There is a house with 3 doors. one red, one yellow and one blue. Which colour do you choose?\n")
        if dec2 == "yellow":
            print("You Won, Well, look who we have here, the human Wikipedia mixed with a pinch of Einstein! Don't mind me; I'm just busy trying to keep up with my one brain cell. XD")
        elif dec2 == "red":
            print("Game Over, you went to hell XD")
        else:
            print("Game Over, you went with smurf's XD")
    else:
        print("Game Over, Crocodile had a good lunch XD")
else:
    print("Game Over, your dad caught you playing game XD")
