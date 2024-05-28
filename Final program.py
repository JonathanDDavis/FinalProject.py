#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jd0919889
#
# Created:     03/10/2019
# Copyright:   (c) jd0919889 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time
import random
import sys
import finalProgramRacesAndClasses
import finalProgramDiceRoller

## delclare all varibles
prompt = "\n>> "
inventory = {
}

stats = {
    "strength" : 10,
    "dexterity" : 10,
    "constitution" : 10,
    "intelligence" : 10,
    "wisdom" : 10,
    "charisma" : 10,
    }

def invalidInput():
    delayPrint("\nInvalid Input")

def delayPrint(x):
    for i in x:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.1)

## Need to work on this. Makes it were it will roll mulitply dice.
def statRolls():
    print(int(round(((random.random() * 6 + 6 + 6)))))

#credited to Iskuss on python forum

print("Welcome to Dungeon Crawler")
print("What is your name")
finalProgramRacesAndClasses.Player.name = input(prompt)
print("It is nice to meet you " + finalProgramRacesAndClasses.Player.name)
ready = False
while ready == False:
    print("Are you ready to play " + finalProgramRacesAndClasses.Player.name + "?")
    choice = input(prompt).lower()
    if choice == "yes":
        print("Great we will start.")
        ready = True
    elif choice == "no":
        print("Just tell when you are ready then.")
    else:
        invalidInput()

##Getting the class of the character
print("Now what do you want your class to be? (mage, warrior, rouge, ranger, or cleric")
pickedClass = False
while pickedClass == False:
    choice = input(prompt).lower()
    if choice == "mage":
        print("You are a mage")
        player.position = "mage"
        pickedClass = True
    elif choice == "warrior":
        print("You are a warrior")
        player.position = "warrior"
        pickedClass = True
    elif choice == "rouge":
        print("You are a rouge")
        player.position = "rouge"
        pickedClass = True
    elif choice == "ranger":
        print("You are a ranger")
        player.position = "ranger"
        pickedClass = True
    elif choice == "cleric":
        print("You are a cleric")
        player.position = "cleric"
        pickedClass = True
    else:
        invalidInput()

## Getting the race of the character
print("Okay time to create your character.")
print("What race would you want to be? (Human or Dwarf")
pickedRace = False
while pickedRace == False:
    choice = input(prompt).lower()
    if choice == "human":
        print("You are a human")
        player.race = "human"
        pickedRace = True
    elif choice == "dwarf":
        print("You are a dwarf")
        player.race = "dwarf"
        pickedRace = True
    else:
        invalidInput()


##Getting the stats for the character NEEDS LOT OF WORK
statsDone = False
while statsDone == False:
    stats["strength"] = statRolls()
    print("Which one of these do you want to be your dexterity")
    choice = input(prompt)
    stats["dexterity"] = statRolls()
    print("Which one of these do you want to be your constitution")
    choice = input(prompt)
    stats["constitution"] = statRolls()
    print("Which one of these do you want to be your intelligence")
    choice = input(prompt)
    stats["intelligence"] = statRolls()
    print("Which one of these do you want to be your wisdom")
    choice = input(prompt)
    stats["wisdom"] = statRolls()
    print("Which one of these do you want to be your charisma")
    choice = input(prompt)
    stats["charisma"] = statRolls()
    newStats = True
    while newStats == True:
        choice = input(prompt).lower()
        print("Do you want new stats?")
        if choice == "yes":
            print("Okay")
        if choice =="no":
            print("Okay")
            newStats = False



## The start of the game

print("You walk up and the first thing you see is that you are in a dark room. You try to move your arms but you find out that they are tied. You can tell that who ever tied you up used rope.")
print("Do you want to try and break the rope?")
free = False
while free == False:
    choice = input(prompt).lower()
    if choice == "yes":
        if player.stats["strength"] >= 12:
            print("You use all of your strenth to try and rip the rope apart and the you hear a 'rip'. You broke the rope.")
        elif player.stats["strength"] < 12:
            print("You tried to break the rope but you can't. You strugled to get out of them but no matter what you do you couldn't get out.")
        else:
            invalidInput()
    elif choice == "no":
        print("You don't try to break out. You sit there waiting to see who captured you")
    else:
        invalidInput()































