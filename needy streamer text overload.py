""""
//THIS GAME IS UNDER CONSTRUCTION!//
"""

from time import sleep
import os
from os import system
import random

day = 1
current_time = "Day"
lost = False

#handles the day system in the game
def handleTime():
    global day
    global current_time

    if current_time == "Night":
        day += 1
        current_time = "Day"
    else:
        current_time = "Night"

def displayTime():
    global day
    global current_time

    print("")
    print("=============================")
    print("time.exe            | - | X |")
    print("=============================")
    print("DAY " + str(day) + " / 30")
    print("TIME: " + current_time.upper())
    print("=============================")
    print("")


#class to represent a girlfriend
class GF:
    money = 100
    affection = 0
    stress = 0
    mental_darkness = 0
    subscribers = 0
    therapy_cost = 50
    #Searching for stream ideas will give you bonus subscribers
    subscriber_bonus = 0
    

    def __init__(self, name, moneyIncrement):
        self.name = name
        self.moneyIncrement = moneyIncrement

    #Prints out all stats  
    def __str__(self):
        state = f"{self.name.upper()}'S STATS\n"
        state += "--------------------\n"
        state += f"Subscribers: {self.subscribers} / 1000000\n"
        state += f"Stress: {self.stress} / 100\n" 
        state += f"Affection: {self.affection} / 100\n"
        state += f"Mental Darkness: {self.mental_darkness} / 100\n" 
        state += f"Money: ${self.money}"
        state += "--------------------"

        return state
    
    def spendMoney(self):
        self.money -= self.moneyIncrement
    
    #calculates stat gains from streaming
    def stream(self):
        if self.subscribers == 0:
            self.subscribers += 100
            self.stress += 15
            self.mental_darkness += 5
            self.money += 50
        else:
            rand = random.randint(1, 10)
            x = int((3*(self.subscribers + self.subscriber_bonus))/rand)
            self.money += int(x * (20/9))
            self.mental_darkness += int(x * 1.3)
            self.stress += int(x * (3.5/2))
            self.subscribers += x
            self.affection -= rand

        if self.affection < 0:
            self.affection = 0
    
    def therapy(self):
        rand_ment = random.randint(10,20)
        rand_stress = random.randint(15, 25)
        rand_affect = random.randint(15, 45)

        self.mental_darkness -= rand_ment
        self.stress -= rand_stress
        self.affection += rand_affect

        if self.mental_darkness < 0:
            self.mental_darkness = 0
        
        if self.stress < 0:
            self.stress = 0
    
    def goOutside(self):
        rand_ment = random.randint(5,10)
        rand_stress = random.randint(5,10)
        rand_affect = random.randint(1,5)

        self.mental_darkness -= rand_ment
        self.stress -= rand_stress
        self.affection += rand_affect

        if self.mental_darkness < 0:
            self.mental_darkness = 0
        
        if self.stress < 0:
            self.stress = 0
    
    def doTheDeed(self):
        rand_ment = random.randint(20, 45)
        rand_stress = random.randint(35, 55)
        rand_affect = random.randint(30, 60)

        self.affection += rand_affect
        self.stress -= rand_stress
        self.mental_darkness -= rand_ment

        if self.stress < 0:
            self.stress = 0
        
        if self.mental_darkness < 0:
            self.mental_darkness = 0
    
    def browseIdeas(self):
        chance = random.randint(1,2)
        rand_bonus = random.randint(5,10)
        if chance == 1:
            print(f"{self.name.upper()} found some new ideas for a stream!")
            sleep(1.2)
            print(f"GAINED +{rand_bonus} SUBSCRIBER BONUS")
            self.subscriber_bonus += rand_bonus
        else:
            print(f"{self.name.upper()} failed to find any ideas!")


    #resets all stats
    def reset(self):
        self.money = 100
        self.subscribers = 0
        self.stress = 0
        self.affection = 0
        self.mental_darkness = 0
        self.therapy_cost = 50
        self.subscriber_bonus = 0
    
    #add THE function here (but on your personal computer)


def clear():
 
    # for windows
    if os.name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

clear()

def notAValidCommand():
    print("That's not a valid command!")
    print("")
    sleep(0.4)
    clear()

def doTheDeedScreen():
    clear()
    print("===================================================")
    print("XXX.exe                                   | - | X |")
    print("===================================================")
    print("*************************************************")
    print("*************************************************")
    print(" ____  ____  __  _   ____  ____ _____  ____  ____")
    print("/ (__`| ===||  \| | (_ (_`/ () \| () )| ===|| _) \ ")
    print("\____)|____||_|\__|.__)__)\____/|_|\_\|____||____/")
    print("*************************************************")
    print("*************************************************")
    print("===================================================")
    sleep(2.3)

def therapyScreen():
    clear()
    print("======================================================")
    print("therapy.exe                                  | - | X |")
    print("======================================================")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░░░██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░░░█░░░░░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░░░█░░░██░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░░░█░██████░█████████████████████████████░░░░░░░░░░░░")
    print("░░░░█░██████░█░░┌┐┌┬─┬──┬─┬──┬──┬──┬┐░░░░█░░░░░░░░░░░░")
    print("░░░░█░░░██░░░█░░│└┘│││──┤┼├││┴┐┌┤┌┐││░░░░█░░░░░░░░░░░░")
    print("░░░░█░░░░░░░░█░░└┘└┴─┴──┴┘└──┘└┘└┘└┴─┘░░░█░░░░░░░░░░░░")
    print("░░░░███████████████████████████████████████░░░░░░░░░░░")
    print("░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░")
    print("░░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░")
    print("░░░░█░░░░░░░░░░░░░░░███░░░███░░░███░░███░░█░░░░░░░░░░░")
    print("░░░░█░░░░░░░░░░░░░░░███░░░███░░░███░░███░░█░░░░░░░░░░░")
    print("░░░░█░░█████████░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░")
    print("░░░░█░░█░░░█░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░")
    print("░░░░█░░█░░░█░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░")
    print("░░░░█░░█░░░█░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░")
    print("░░░░█░░█░░░█░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░")
    print("░░░░███████████████████████████████████████░░░░░░░░░░░")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("======================================================")
    sleep(2.3)



def loadingScreen():
    if os.name == "nt":
        print("===================================================================")
        print("windoseLoader.exe                                        | - | X |")
        print("===================================================================")
        print("$$\      $$\ $$\                 $$\                               ")
        print("$$ | $\  $$ |\__|                $$ |                              ")
        print("$$ |$$$\ $$ |$$\ $$$$$$$\   $$$$$$$ | $$$$$$\   $$$$$$$\  $$$$$$\  ")
        print("$$ $$ $$\$$ |$$ |$$  __$$\ $$  __$$ |$$  __$$\ $$  _____|$$  __$$\ ")
        print("$$$$  _$$$$ |$$ |$$ |  $$ |$$ /  $$ |$$ /  $$ |\$$$$$$\  $$$$$$$$ |")
        print("$$$  / \$$$ |$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ | \____$$\ $$   ____|")
        print("$$  /   \$$ |$$ |$$ |  $$ |\$$$$$$$ |\$$$$$$  |$$$$$$$  |\$$$$$$$\ ")
        print("\__/     \__|\__|\__|  \__| \_______| \______/ \_______/  \_______|")
        print("")
        print("")
        print("Loading.....")
        print("===================================================================")
        sleep(3.5)
        clear()
    else:
        print("==========================================================================")
        print("macDoseLoader.exe                                                | - | X |")
        print("==========================================================================")
        print("$$\      $$\                     $$$$$$$\                                ")
        print("$$$\    $$$ |                    $$  __$$\                               ")
        print("$$$$\  $$$$ | $$$$$$\   $$$$$$$\ $$ |  $$ | $$$$$$\   $$$$$$$\  $$$$$$\  ")
        print("$$\$$\$$ $$ | \____$$\ $$  _____|$$ |  $$ |$$  __$$\ $$  _____|$$  __$$\ ")
        print("$$ \$$$  $$ | $$$$$$$ |$$ /      $$ |  $$ |$$ /  $$ |\$$$$$$\  $$$$$$$$ |")
        print("$$ |\$  /$$ |$$  __$$ |$$ |      $$ |  $$ |$$ |  $$ | \____$$\ $$   ____|")
        print("$$ | \_/ $$ |\$$$$$$$ |\$$$$$$$\ $$$$$$$  |\$$$$$$  |$$$$$$$  |\$$$$$$$\ ")
        print("\__|     \__| \_______| \_______|\_______/  \______/ \_______/  \_______|")
        print("")
        print("Loading......")
        print("==========================================================================")
        sleep(5)
        clear()


def titleScreen():
    while True:
        print("================================================")
        print("needyStreamerTextOverload.exe          | - | X |")
        print("================================================")
        print("       >>>>NEEDY TEXT OVERLOAD<<<<")
        print("A game inspired by Needy Streamer Overload")
        print("Pre-Alpha Version")
        print("")
        print(">>Press 't' to view the tutorial")
        print(">>Press 's' to start the game")
        print("================================================")
        decision = input(">")
        if decision.lower() == "t":
            print("Alan please add details")
            clear()
        elif decision.lower() == "s":
            clear()
            break
        else:
            notAValidCommand()


#losing conditons
#ran out of money
#too much mental darkness
#too much stress
#too much affection
#too little affection
#not enough subscribers by the end of day 30
#died from.. you know...

titleScreen()

name = input("Enter a name for your girlfriend: ") or 'Ame'
ame = GF(name, 15)

def displayMenu():
    global current_time
    global day

    displayTime()
    print("================================")
    print("menu.exe              | - | X |")
    print("================================")
    print("(1)Check your girlfriend's stats")
    print("(2)Go Outside")
    print(f"(3)Go to therapy (Costs ${ame.therapy_cost})")
    print("(4)Do the deed")
    if current_time == "Night":
        print("(6)Stream")
    print("=================================")
clear()

#loss by running out of money
def ranOutOfMoneyScreen():
    global ame
    global day
    global current_time
    global lost
    
    ame.reset()
    lost = False
    day = 1
    current_time = "Day"

    print("===============================")
    print("youLost.exe           | - | X |")
    print("===============================")
    print("Money, Money, Money")
    print("---------------------")
    print("Money is the equivalence point.")
    print("********************************")
    print("Type Anything to Continue")
    print("===============================")
    i = input(">")
    clear()

#loss by too much mental darkness
def mentalDarkenssLost():
    global ame
    global day
    global current_time
    global lost

    ame.reset()
    lost = False
    day = 1
    current_time = "Day"
    
    print("===============================")
    print("youLost.exe           | - | X |")
    print("===============================")
    print("Think Happy Thoughts")
    print("---------------------")
    print("988lifeline.org")
    print("********************************")
    print("Type Anything to Continue")
    print("===============================")
    i = input(">")
    clear()


def checkForLoss():
    global ame
    global day
    global lost

    if ame.money <= 0:
        print(f"{ame.name.upper()} can't live like this anymore..")
        sleep(1.4)
        print(f"{ame.name.upper()} ran out of money.")
        sleep(2.5)
        lost = True
        ranOutOfMoneyScreen()
    


#main game loop
while True:
    loadingScreen()
    while day == 1 and not lost:
        clear()
        displayMenu()
        decision = input(">")
        if decision == "1":
            print("")
            print(ame)
            sleep(2.8)
        elif decision == "3":
            if ame.money >= ame.therapy_cost:
                ame.money -= ame.therapy_cost
                print(f"You decided to send {ame.name.upper()} to therapy.")
                sleep(2.8)
                handleTime()
                ame.therapy()
                therapyScreen()
            else:
                print("You don't have enough money!")
                sleep(1.4)
        elif decision == "4":
            handleTime()
            print(f"You decided to do the deed with {ame.name.upper()}")
            sleep(2.8)
            ame.doTheDeed()
            doTheDeedScreen()
        elif decision == "6" and current_time == "Night":
            ame.stream()
            print(f"{ame.name.upper()} is now live!")
            sleep(1.3)
            handleTime()
        else:
            notAValidCommand()
    #Do not check for losses until day 6
    while day == 2 and not lost:
        clear()
        displayMenu()
        decision = input(">")

        if decision == "1":
            print("")
            print(ame)
            sleep(2.8)

        







                



    





    







