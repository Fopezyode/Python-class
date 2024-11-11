print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
direction = input("You are at a Crossroad, Which direction do you want to go? left Or right?\n")
if direction == "left":
    print("You are walking down the Road then " + "You have Encountered a River")
    boat = input("Will You swim or wait for a boat? swim or wait?\n" )
    if boat == "wait":
        print("Welcome to the Last Trial, Player!")
        door = input("Up Ahead is Three Doors, red, blue and Yellow. Pick red, blue Or yellow\n")
        if door == "red":
            print('''   ,.   (   .      )        .      "
   ("     )  )'     ,'        )  . (`     '`
 .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
 _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..jb

''')
            print("Burned By Fire..... GAME OVER!!!")
        elif door == "blue":
            print("Eaten By Beasts...... GAME OVER!!!")
        elif door == "yellow":
            print("Congratulations Player,You have reached the End")
            print("YOU WINNNNN!!!!!!!")
        else:
            print("GAME OVER SUCKERRRR!!!")
    else:
        print('''          ,---,
  _    _,-'    `--,
 ( `-,'            `\
  \           ,    o \
  /   ,       ;       \
 (_,-' \       `, _  ""/
     pb `-,___ =='__,-'
              ````
''')
        print("Attacked By Trout.....  GAME OVER!!!")
else:
    print("You Fell Into A Hole. GAME OVER!!")


