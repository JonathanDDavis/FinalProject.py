#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      jd0919889
#
# Created:     21/11/2019
# Copyright:   (c) jd0919889 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
import sys


def statRolls():
    print(int(round(((random.random() * 6 + 6 + 6)))))

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
            print("Okay these are your new stats")
        elif choice == "no":
            print("")