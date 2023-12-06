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

    def __init__(self, name, moneyIncrement):
        self.name = name
        self.moneyIncrement = moneyIncrement

    #Prints out all stats  
    def __str__(self):
        state = self.name.upper() + "'S STATS" + '\n'
        state += "--------------------" + '\n'
        state += "Stress: " + str(self.stress) + "\n"
        state += "Affection: " + str(self.affection) + '\n'
        state += "Mental Darkness: " + str(self.mental_darkness) + '\n'
        state += "Money: $" + str(self.money) + '\n'
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
            x = int((3*self.subscribers)/rand)
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
        rand_affect = random.randint(20, 60)

        self.affection += rand_affect
        self.stress -= rand_stress
        self.mental_darkness -= rand_ment

        if self.stress < 0:
            self.stress = 0
        
        if self.mental_darkness < 0:
            self.mental_darkness = 0
    
    def reset(self):
        self.money = 100
        self.subscribers = 0
        self.stress = 0
        self.affection = 0
        self.mental_darkness = 0
    
    #add THE function here (but on your personal computer)


def clear():
 
    # for windows
    if os.name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

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
    print("(3)Go to therapy (Costs $" + str(ame.therapy_cost) + ")")
    print("(4)Do the deed")
    if current_time == "Night":
        print("(6)Stream")
    print("=================================")
clear()

def checkForLoss():
    global ame
    global day
    global lost

    if ame.money <= 0:
        print(ame.name.upper() + " can't live like this anymore..")
        sleep(1.4)
        print(ame.name.upper() + " ran out of money.")
        lost = True

def ranOutOfMoneyScreen():
    print("===========================")
    print("youLost.exe       | - | X |")


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
        elif decision == "4":
            handleTime()
            print("You decided to do the deed with " + ame.name.upper())
            sleep(2.8)
            ame.doTheDeed()
            doTheDeedScreen()

        else:
            notAValidCommand()
    
    while day == 2 and not lost:
        clear()
        displayMenu()
        decision = input(">")

        







                



    





    






