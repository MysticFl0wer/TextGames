from time import sleep

main_game = True
side_quest = False

deaths = 0
latest_death = "None"
#Achievements
crunchu_crunchy = False
liver_stolen = False
xxx_noscopethreesixty = False
sanctuary_beaten = False
undies_acquired = False
oneeighty_noscope = False
anime_ending = False
bffs = False
dark_lord_beaten = False
peasant = False
crunchy_dark_lord = False

total = 11


#Title
print(" _________                     __               _                          ")
print("|  _   _  |                   [  |             / |_                        ")
print("|_/ | | \_|.--.   _ .--..--.   | |.--.   .--. `| |-' .--.   _ .--.  .---.  ")
print("    | |  / .'`\ \[ `.-. .-. |  | '/'`\ \( (`\] | | / .'`\ \[ `.-. |/ /__\\")
print("   _| |_ | \__. | | | | | | |  |  \__/ | `'.'. | |,| \__. | | | | || \__., ")
print("  |_____| '.__.' [___||__||__][__;.__.' [\__) )\__/ '.__.' [___||__]'.__.' ")

print("")
print("A Simple Text-RPG Played With Inputting Numbers")
print("Ver. 1.0.6")
print("Written in Python 3")
print("")

#time.sleep(1)

def notAValidCommand():
    print("That's not a valid command!")
    print("")
    sleep(0.4)


#will default to 'flipper flopper' if the user doesn't input anything
name = input("Type your name: ") or "Flipper Flopper"

def displayTomb():
    print("")
    print("----------" + name.upper() + "'S TOMBSTONE----------")
    print("Number of deaths: " + str(deaths))
    print("Reason for latest death: " + latest_death)
    print("------------------------------------")
    print("")

while main_game:
    #stats
    attack = 0
    magic = 0
    inventory = []
    #in-game event
    journal_read = False
    #Counts the number of achivements
    num_of_achievements = 0

#Function to print all the player's stats
    def printAllInfo():
        print("")
        print("==========")
        print( "[" + name.upper() + "'S STATS]")
        print("Attack: " + str(attack))
        print("Magic: " + str(magic))
        print("Inventory:")
        for i in inventory:
            print(">" + i)
        print("==========")
        print("")
    #Function to print the inventory only
    def printInventory():
        print("")
        print("==========")
        print("[" + name.upper() + "'S INVENTORY]")
        for i in inventory:
            print(">" + i)
        print("==========")
        print("")

#Prints the number of deaths and the reason for the latest death
    print("")
    print("----------" + name.upper() + "'S TOMBSTONE----------")
    print("Number of deaths: " + str(deaths))
    print("Reason for latest death: " + latest_death)
    print("------------------------------------")
    print("")

    sleep(2)
#ACT 1
    print("--ACT 1--")
    print("TIP: type in numbers to make your decision")
    print("")
    sleep(0.5)
    print("You wake up.")
    sleep(0.5)
#Prints out all the actions on separate lines
    while True:
        print(">>Actions:\n(1)Go back to sleep\n(2)Get up from bed")
        decision = input(">")

        if decision in ["1", "2"]:
            break
        #If the user inputs an invalid command it will repeat the loop
        #until the user inputs a valid command
        else:
            notAValidCommand()
            
   #Events
    if decision == "1":

        print("You decided to go back to sleep.")
        sleep(1)
        print("ZZZZZzzzz....")
        sleep(3)
        print(">>YOU DIED!<<")
        sleep(0.5)

        deaths += 1
        latest_death = "Too much of a sleepyhead"
        continue
    else:
        print("You decided to get out of bed.")
        sleep(1)
    
    print("What will you do now?")
    print("")
    sleep(0.5)
    
    while True:
        print(">>Actions:\n(1)Go Downstairs\n(2)Stare into the abyss\n(3)Eat Cruchy Crunchy cereal, the cereal that's crunchy AND melts in your mouth at the same time")
        decision = input(">")
        if decision in ["1", "2", "3"]:
            break
        #If the user inputs an invalid command
        else:
            notAValidCommand()
    
    #Events
    if decision == "1":
        print("You decided to go downstairs")
        sleep(0.5)
    elif decision == "2":
        print("You decided to stare into the the abyss...")
        sleep(1.3)
        print("Great, you wasted your time.")
        print("")
        sleep(0.5)
        print("You went downstairs.")
        print("")
        sleep(0.5)
    else:
        print("You decided to eat your Crunchy Crunchy cereal that was for some reason near your bed")
        sleep(0.5)
        print(">>YOU DIED!<<")
        deaths += 1
        latest_death = "CHOLESTEROL LEVELS OVER 90000!!!!"
        crunchu_crunchy = True
        sleep(0.5)
        continue

    print("Outside you see fire and people running in panic")
    print("")
    sleep(1)

    while True:
        print(">>Actions:\n(1)Eat breakfast\n(2)Go Outside\n(3)Read a book about necromancy")
        decision = input(">")
        if decision in ["1", "2", "3"]:
            break
        else:
            notAValidCommand()
    #Events
    if decision == "1":
        print("You decided to eat breakfast")
        sleep(0.5)
        print("GAINED 10 HEALTH")
        sleep(0.5)
        print("Wait......")
        print("Why was my food all moldy?")
        print("....")
        sleep(1)
        print(">>YOU DIED!<<")
        deaths += 1
        latest_death = "Ate moldy food"
        continue
    elif decision == "2":
        print("You went outside")
        print("")
        sleep(0.5)
    else:
        print("You decided to read a book about necromancy")
        sleep(1)
        print("GAINED +10 MAGIC")
        sleep(1)
        magic += 10
        print("Still curious about the commotion, you went outside")
        print("")
    
    print("Outside, you see the DARK LORD destroying your village")
    sleep(1)
    print("[DARK LORD]: MUAHAHAHAH!!! I will destroy this insignificant village for NO good reason!!")
    print("")
    sleep(0.5)
    print("What will you do?")

    while True:
        print(">>Actions:\n(1)Fight the DARK LORD\n(2)Try to talk to the DARK LORD")
        decision = input(">")
        if decision in ["1", "2"]:
            break
        else:
            notAValidCommand()
    #Events
    if decision == "1":
        print("You decided to run in and fight the DARK LORD")
        print("")
        sleep(1)
        print("[DARK LORD]: What are you trying to do peasant? Tickle me?")
        sleep(1)
        print("You realize that maybe trying to fight a evil dark lord by yourself wasn't a good idea.")
        sleep(1)
        print("The DARK LORD picks you up and throws you.")
        sleep(1)
    else:
        print("You decided to try to talk to the DARK LORD")
        print("")
        sleep(1)
        print("[DARK LORD]: Who are you, peasant?")
        sleep(1)
        print("You explain who you are")
        sleep(1)
        print("The DARK LORD is looking at you funny")
        sleep(2)
        print(">>YOU DIED!<<")
        deaths += 1
        latest_death = "The DARK LORD does not have time for chit chat"
        continue

    print("--ACT 2--")
    sleep(1)
    print("You wake up in a village you don't recognize")
    print("")
    sleep(0.5)

    while True:
        print(">>Actions:\n(1)Talk to the villagers\n(2)Walk around aimlessly")
        decision = input(">")
        if decision in ["1", "2"]:
            break
        else:
            notAValidCommand()
    #Events
    if decision == "1":
        print("You decided to talk to the villagers")
        print("")
        print("From the villagers, you learn about a sacred sanctuary that will grant people immense power")
        sleep(0.5)
        print("However, the DARK LORD is going there!")
        sleep(0.5)
        print("Fortunately (or unfortunately) there is a powerful monster guarding that place")
        sleep(0.7)
    else:
        print("You decided to walk around aimlessly.")
        print("")
        sleep(0.5)
        print("In the village, you see three buildings.")
        sleep(0.5)
        print("Which one will you go to?")
        print("")
        while True:
            print(">>Actions:\n(1)Magical Pharmacy\n(2)24 HR Medieval Gym\n(3)Definitely not a sketchy house")
            decision = input(">")
            if decision in ["1", "2", "3"]:
                break
            else:
                notAValidCommand()

        if decision == "1":
            print("You decided to go the Magical Pharmacy.")
            sleep(0.5)
            print("YOU GAINED AN ITEM: MAGICAL ANTIBIOTICS")
            inventory.append("magical antibiotics")
            sleep(0.5)
            print("After visiting the pharmacy, you hear the villagers talking about something")
            print("")
            print("You learn about a sacred sanctuary that will grant people immense power")
            sleep(0.5)
            print("However, the DARK LORD is going there!")
            sleep(0.5)
            print("Fortunately (or unfortunately) there is a powerful monster guarding that place")
            sleep(0.7)    
        elif decision == "2":
            print("You decided to go to the 24HR Medieval Gym.")
            sleep(0.3)
            print("GAINED +50 ATTACK")
            attack += 50
            sleep(0.5)
            print("After visiting the gym, you hear the villagers talking about something")
            print("")
            print("You learn about a sacred sanctuary that will grant people immense power")
            sleep(1)
            print("However, the DARK LORD is going there!")
            sleep(2)
            print("Fortunately (or unfortunately) there is a powerful monster guarding that place")
            sleep(1)
        else:
            print("You decided to visit the sketchy house.")
            sleep(0.5)
            print("Inside the house, you find the Phantom Thieves from Persona 5")
            sleep(1)
            print("(Dont even ask me about this I don't even know what is going on either)")
            sleep(2)
            print("The Phantom Thieves steal your liver :(")
            sleep(1)
            print(">>YOU DIED<<")
            deaths += 1
            liver_stolen = True
            latest_death = "The Phantom Thieves stole your liver :(. Also, Morgana likes to play with kidney stones."
            continue
    print("")
    print("You decide to go to the sacred sanctuary")
    sleep(1)
    print("You realize that you have no idea what the sacred sanctuary looks like.")
    sleep(1)
    print("At a fork, you see two signs:")
    print("")
    print("<---Definitely not the DARK LORD's palace")
    print(" Sacred Sanctuary with big scary monster this way ---->")
    print("----Signs sponsored by Obama's very convinient sign emporium----")
    print("")
    sleep(2)

    while True:
        print(">>Actions:\n(1)Go to DARK LORD's palace\n(2)Go to Sacred Sanctuary")
        decision = input(">")   
        if decision in ["1","2"]:
            break
        else:
            notAValidCommand()
    
    if decision == "1":
        print("You decided to go straight to the DARK LORD's palace.")
    else:
        print("You decided to go to the sacred sanctuary.")
        sleep(1)
        print("After walking up a enormous montain, you find the sacred sanctuary.")
        sleep(0.5)
        print("As expected, an enormous monster guards the entrance.")
        sleep(0.5)
        print("================")
        print("a PLAGUE RAT OF DOOM stands in your way")
        print("================")
        sleep(0.9)
        print("")

        while True:
            printAllInfo()
            sleep(1)
            print(">>Actions:\n(1)Throw the magical antibiotics - REQUIREMENTS => Have the magical antibiotic in your inventory" +
                  '\n' + "(2)Do a 360 mlg dorito mountain dew no-scope - REQUIREMENTS => Have at least 50 attack" +
                  '\n' + "(3)Cast an epic dorito illuminati spell - REQUIREMENTS => Have at least 10 magic" +
                    '\n' + "(4)Cry")
            decision = input(">")
            if decision in ["1","2","3","4"]:
                break
            else:
                notAValidCommand()

#cleaned up some code here
        if decision == "2":
            print("You decided to 360 mlg dorito mountain dew no-scope the PLAGUE RAT OF DOOM")
            sleep(1)
            if attack >= 50:
                print("Your no-scope was so epic the rat died!")
                sanctuary_beaten = True
                xxx_noscopethreesixty = True
            else:   
               print("You try to 360 mlg dorito mountain dew no-scope the PLAGUE RAT OF DOOM")
               sleep(0.9)
               print("However, you don't have enough ATTACK to no-scope the PLAGUE RAT OF DOOM.")
               sleep(1)
               print(">>YOU DIED<<")
               deaths += 1
               latest_death = "360 mlg no-scope was not epic enough"
               continue
        elif decision == "3":
            print("You decided to cast an epic dorito illuminati spell")
            sleep(1)
            if magic >= 10:
                print("Your spell turned the turned the PLAGUE RAT OF DOOM into a pile of doritos!")
                sanctuary_beaten = True
            else:    
                print("You tried to cast an epic dorito illuminati spell")
                sleep(1)
                print("However, your spell just made the PLAGUE RAT OF DOOM stronger!")
                sleep(1)
                print(">>YOU DIED<<")
                deaths += 1
                latest_death = "Uno reverse spell"
                continue
        elif decision == "4":
            print("You decided to cry.")
            sleep(2)
            print(">>YOU DIED<<")
            deaths += 1
            latest_death = "What did you think was going to happen?"
            continue
        else:
            print("You decided to use the magical antibiotics.")
            sleep(1)
            if "magical antibiotics" in inventory:
                print("You threw the antibiotics at the PLAGUE RAT OF DOOM")
                sleep(0.5)
                print("the PLAGUE RAT OF DOOM died instanlty!")
                inventory.remove("magical antibiotics")
                sanctuary_beaten = True
            else:
                print("You realize that you don't have antibiotics.")
                sleep(1)
                print(">>YOU DIED<<")
                deaths += 1
                latest_death = "Contracted the Black Death"
                continue
        print("After beating the PLAGUE RAT OF DOOM, you gained immense power")
        sleep(1)
        print("")
        print("GAINED +50 ATTACK")
        print("GAINED +50 MAGIC")
        attack += 50
        magic += 50
        print("YOU GAINED AN ITEM: BOTTLE OF BLACK DEATH")
        print("")
        inventory.append("bottle of black death")
        sleep(1)
        print("After gaining immense power, you decide to go to the DARK LORD's palace.")

    sleep(1) 
    print("---ACT 3---")
    sleep(2)
    print("")
    print("You arrive at the DARK LORD's palace")
    print("However, you need to figure out how to enter his palace.")
    print("")

    while True:
        printInventory()
        print(">>Actions:" + '\n' + "(1)Try to jump over the lava moat" + '\n' +
              "(2)Try to go past the guards at the entrance - REQUIREMENTS => Have the bottle of black death in your inventory" + '\n' +
              "(3)Walk around the castle")
        decision = input(">")
        if decision in ["1","2","3"]:
            break
        else:
            notAValidCommand()
    
    if decision == "1":
        print("You decided to try to jump over the lava moat.")
        sleep(1)
        print("You fell in the lava.")
        sleep(1)
        print(">>YOU DIED<<")
        deaths += 1
        latest_death = "Fell into lava"
        continue
    elif decision == "2":
        print("You decided to try to go past the guards")
        sleep(1)
        if "bottle of black death" in inventory:
            print("Using the bottle of black death to infect the guards, you enter the DARK LORD's palace")
            sleep(1)
            inventory.remove("bottle of black death")
        else:
            print("The guards spot you immediatly and shred you to pieces.")
            sleep(1)
            print(">>YOU DIED<<")
            deaths += 1
            latest_death = "Evil guards are viscious, man :("
            continue
    else:
        print("You decided to walk around the palace in search of an entrance")
        sleep(1)
        print("")
        print("After walking around the palace, you find a manhole.")
        print("You decide to enter the manhole.")
        sleep(1)
        print("Down in the sewers, three different monsters are blocking different paths.")
        print("Which path will you take?")
        print("")
        sleep(0.5)
        while True:
            print(">>Actions:" + '\n' + "(1)The path with an evil-looking wizard" + '\n' +
                   "(2)The path with a ferocious monster" + '\n' + "(3)The path with the tank (which is somehow in a sewer)" )
            decision = input(">")
            if decision in ["1","2","3"]:
                break
            else:
                notAValidCommand()
        
        if decision == "1":
            print("You decided to approach the evil-looking wizard.")
            sleep(1)
            print("")
            print("===========")
            print("wizard MOE LESTER stands in your way")
            print("===========")
            print("")

            while True:
                printAllInfo()
                print(">>Actions:" + '\n' + "(1)Call the police" + '\n' +
                       "(2)Engage in a magic duel - REQUIREMENTS => Have at least 50 magic" + '\n' +
                       "(3)Use the bottle of black death - REQUIREMENTS => Have the bottle of black death in your inventory.")
                decision = input(">")
                if decision in ["1", "2", "3"]:
                    break
                else:
                    notAValidCommand()

            if decision == "1":
                print("You decided to call the police.")
                sleep(1)
                print("You realize that things such as cell service or wi-fi don't exist in a fantasy world.")
                sleep(1)
                print(">>YOU DIED<<")
                deaths += 1
                latest_death = "Cell Service Not Found :("
                continue
            elif decision == "2":
                print("You decided to engage in a magic duel with MOE LESTER")
                sleep(1)
                if magic >= 50:
                    print("You turned MOE LESTER into a dorito chip!")
                    sleep(1)
                    print("After defeating MOE LESTER, you notice something on the floor.")
                    sleep(1)
                    print("YOU GAINED AN ITEM: EVIL SPELLBOOK")
                    inventory.append("evil spellbook")
                else:
                    print("MOE LESTER turned you into a pile of sand")
                    sleep(0.5)
                    print(">>YOU DIED<<")
                    deaths += 1
                    latest_death = "Got MOE LESTER'D"
                    continue
            else:
                print("You decided to use the bottle of black death")
                sleep(1)
                if "bottle of black death" in inventory:
                    print("MOE LESTER got infected and died!")
                    inventory.remove("bottle of black death")
                    sleep(1)
                    print("After defeating MOE LESTER, you notice something on the floor.")
                    sleep(1)
                    print("YOU GAINED AN ITEM: EVIL SPELLBOOK")
                    inventory.append("evil spellbook")
                else:
                    print("You realize you don't have the bottle of black death")
                    print("......")
                    sleep(1)
                    print(">>YOU DIED<<")
                    deaths += 1
                    latest_death = "Epic Fail"
                    continue
        elif decision == "2":
            print("You decided to approach the ferocious monster.")
            sleep(1)
            print("")
            print("===========")
            print("a SOUL CONSUMING FLAME stands in your way")
            print("===========")
            while True:
                printAllInfo()
                print(">>Actions:" + '\n' + "(1)Try to extinguish the flame" +
                      '\n' + "(2)1080 mlg dorito illuminati no-scope the flame - REQUIREMENTS => have at least 100 attack" +
                      '\n' + "(3)Offer your soul as sacrifice")
                decision = input(">")
                if decision in ["1","2","3"]:
                    break
                else:
                    notAValidCommand()

            if decision == "1":
                print("You decided to try to extinguish the SOUL CONSUMING FLAME.")
                sleep(1)
                print("The SOUL CONSUMING FLAME didn't like that.")
                sleep(1)
                print(">>YOU DIED<<")
                latest_death = "Evil sentient soul consuming flames are vicious, man :("
                deaths += 1
                continue
            elif decision == "2":
                print("You decided to 1080 mlg dorito illuminati no-scope the flame.")
                sleep(1)
                if attack >= 100:
                    print("Your 1080 mlg dorito illuminati no-scope was so epic the SOUL CONSUMING FLAME died!")
                    sleep(1)
                    print("YOU GAINED AN ITEM: REALLY HOT CHARCOAL")
                    inventory.append("really hot charcoal")
                    oneeighty_noscope = True
                else:
                    print("However, since you don't have enough ATTACK, you ended up tripping and falling into the flames")
                    sleep(1)
                    print(">>YOU DIED<<")
                    deaths += 1
                    latest_death = "Grandma Moment"
                    continue
            else:
                print("You decided to offer your soul to the SOUL CONSUMING FLAME")
                sleep(1)
                print("the SOUL CONSUMING FLAME is devouring your soul.")
                sleep(1)
                print(">>YOU DIED<<")
                deaths += 1
                latest_death = "You kind of need your soul to live :/"
                continue

        else:
            print("You decided to approach the tank")
            sleep(1)
            print("")
            print("===========")
            print("a M1 ABRAMS TANK blocks your way!")
            print("===========")
            while True:
                printAllInfo()
                print(">>Actions:" + '\n' + "(1) Use the bottle of black death - REQUIREMENTS => Have the bottle of black death" +
                      '\n' + "(2)Do a 720 mlg illuminati dorito epic no-scope - REQUIREMENTS => Have at least 50 attack" +
                      '\n' + "(3)Cast a magical barrier - REQUIREMENTS => Have at least 10 magic" + '\n' + 
                      "(4)Not give the tank your legal consent")
                decision = input(">")
                if decision in ["1","2","3","4"]:
                    break
                else:
                    notAValidCommand()
            
            if decision == "1":
                print("You decided to use the bottle of black death")
                print("")
                sleep(1)
                if "bottle of black death" in inventory:
                    print("You realize that tanks are not affected by bacteria.")
                    sleep(0.5)
                    print(">>YOU DIED<<")
                    deaths += 1
                    latest_death = "Did you seriously try to infect a tank?"
                    continue
                else:
                    print("You realize that you don't have the bottle of black death.")
                    sleep(0.5)
                    print(">>YOU DIED<<")
                    deaths += 1
                    latest_death = "TANK POWER 3000!!!"
                    continue
            elif decision == "2":
                print("You decided to 720 mlg illuminati dorito no-scope the tank.")
                print("")
                sleep(1)
                if attack >= 50:
                    print("However, your wombo combo mlg dorito bullets don't seem to have an effect on the tank.")
                    sleep(0.5)
                    print(">>YOU DIED<<")
                    deaths += 1
                    latest_death = "720 NO-SCOPE ON TANK **GONE WRONG** **AT 3AM** **WE KISSED**"
                    continue
                else:
                    print("However, since you don't have enough ATTACK, you ended up tripping and falling.")
                    sleep(1)
                    print(">>YOU DIED<<")
                    deaths += 1
                    latest_death = "Epic Fail"
                    continue
            elif decision == "3":
                print("You decided to cast a magical barrier")
                print("")
                sleep(1)
                if magic >= 10:
                    print("The barrier you cast reflects all tank projectiles!")
                    sleep(1)
                    print("You defeated the tank.")
                    sleep(1)
                    print("YOU GAINED AN ITEM: ANTI-AIRCRAFT GUN")
                    inventory.append("anti-aircraft gun")
                else:
                    print("However, since you don't have enough MAGIC, you accidentally summoned an explosion!")
                    sleep(1)
                    print("You killed the tank and yourself!")
                    sleep(0.5)
                    print(">>YOU DIED<<")
                    deaths += 1
                    latest_death = "Task Failed Successfully"
                    continue
            else:
                print("You decided not to give the tank your legal consent.")
                print("")
                sleep(1)
                print("The tank cannot shoot you without your legal consent!")
                sleep(1)
                print("You defeated the tank (somehow).")
                sleep(1)
                print("YOU RECEIVED AN ITEM: ANTI-AIRCRAFT GUN")
                inventory.append("anti-aircraft gun")
        sleep(1)
        print("")
        print("After clearing the path, you find an exit.. which leads to a bathroom inside the palace!")
        sleep(1)
        print("You exit the batroom.")
        sleep(1)

    print("")
    print("Inside the DARK LORD's palace, you spot three paths in the hallway")
    print("Which one will you take?")
    print("")

    while True:
        print(">>Actions:" + '\n' + "(1)The secret path behind the painting" + '\n' +
              "(2)The door at the end of the hallway" + '\n' + "(3)The path in the weird-looking closet")
        decision = input(">")
        if decision in ["1","2","3"]:
            break
        else:
            notAValidCommand()

    if decision == "1":
        print("You decided to take the secret path behind the painting.")
        print("")
        sleep(1)
        print("Behind the painting, there is a large room with a treasure chest.")
        sleep(1)
        print("YOU GAINED AN ITEM: THE DARK LORD'S UNDERWEAR")
        undies_acquired = True
        inventory.append("dark lord's underwear")
        print("You also find the DARK LORD's journal.")
        sleep(1)
        print("The first page reads:")
        print("")
        sleep(0.5)
        print("-------------------")
        print("DEAR DIARY,")
        print("  Today a peasant said I smelled like shit. This was" + 
              '\n' + "so mean and hurtful that it made me decide to commit murder and genocide" + '\n' +
              "Also, my child has the black death or whatever. I think they got it from" + '\n' +
              "the stupid rat at the sacred sanctuary")
        print("-------------------")
        journal_read = True
        sleep(5)
        print("")
        print("You notice there is another door within the room.")
        sleep(1)
    elif decision == "2":
        print("You decided to open the door at the end of the hallway.")
    else:
        print("You decided to take the path in the weird-looking closet.")
        print("")
        sleep(1)
        print("Once inside the closet, you realize that there is no path.")
        sleep(1)
        print("You also discover that the 'closet' is actually an iron maiden")
        sleep(1)
        print("Before you can get out, the door closes and you are trapped inside")
        sleep(1)
        print(">>YOU DIED<<")
        deaths += 1
        latest_death = "Accidentally trapped yourself inside a toture device"
        continue

    sleep(1)
    print("When you open the door, you see the DARK LORD and his minions in a dining hall.")
    sleep(1)
    print("the DARK LORD and his minions notice you!")
    print("")
    sleep(1)
    print("What will you do?")

    while True:
        printAllInfo()
        print(">>Actions:" + '\n' + "(1)Use items" + '\n' + 
              "(2)Do the most epic no-scope - REQUIREMENTS => Have at least 100 attack" + '\n' +
              "(3)Summon an enormous explosion - REQUIREMENTS => Have at least 50 magic" +
              '\n' + "(4)Use the power of friendship")
        if journal_read:
            print("(5)Offer to help - REQUIREMENTS => Have the magical antibiotics in your antibiotics")
        decision = input(">")
        if  decision in ["2", "3", "4"]:
            break
        elif decision == "5" and journal_read:
            break
        elif decision == "1" and len(inventory) > 0:
            break
        elif decision == "1" and len(inventory) == 0:
            print("You don't have any items in your inventory!")
            print("")
            sleep(0.3)
        else:
            notAValidCommand()
    
    if decision == "1":
        print("You decided to use some items.")
        print("Which item will you use?")
        sleep(1)
        while True:
            printInventory()
            print("TIP: type in the name of the item you want to use")
            print("")
            decision = input(">")
            if decision.lower() in inventory:
                break
            else:
                print("Item not in inventory!")
                print("")
                sleep(0.3)
                        
        if decision.lower() == "dark lord's underwear":
            print("You decided to use the DARK LORD'S underwear")
            print("")
            sleep(1)
            print("[DARK LORD]: WHY DO YOU HAVE MY UNDERWEAR??!!")
            sleep(1)
            print(">>YOU DIED<<")
            deaths += 1
            latest_death = "Seriously? Out of all the things you could've chosen? Underwear?"
            continue
        elif decision.lower() == "evil spellbook":
            print("You decided to use the evil spellbook")
            print("")
            sleep(1)
            print("Using the evil spellbook, you summoned GOMORRAH, DEVOURER OF THE DIVINE.")
            sleep(1)
            print("GOMORRAH ate all of the DARK LORD's minions!")
            print("")
            sleep(1)
            print("[DARK LORD]: WAIT!! DON'T EAT ME!!! I'LL STOP BEING EVIL IF THAT MEANS NOT BEING EATEN!!")
            sleep(1)
            print("You now have two options:")
            print("")
            while True:
                print(">>Actions:" + '\n' + "(1)Let GOMORRAH eat the DARK LORD" +
                      '\n' + "(2)Spare the DARK LORD")
                decision = input(">")
                if decision in ["1","2"]:
                    break
                else:
                    notAValidCommand()
            
            if decision == "1":
                print("You decided to let GOMORRAH eat the DARK LORD")
                print("")
                sleep(1)
                print("GOMORRAH ate the DARK LORD like he was Crunchy Crunchy cereal;" + '\n' +
                      "The cereal that's crunchy AND melts in your mouth at the same time!")
                crunchy_dark_lord = True
                dark_lord_beaten = True
                sleep(1.2)
                print("YOU DEFEATED THE DARK LORD!")
                sleep(2.5)
            else:
                print("You decided to spare the DARK LORD")
                print("")
                sleep(1)
                print("the DARK LORD is VERY grateful you spared him.")
                bffs = True
                sleep(1)

        elif decision.lower() == "bottle of black death":
            print("You decided to use the bottle of black death.")
            print("")
            sleep(1)
            print("Everyone, including the DARK LORD, has been infected with the black death!")
            sleep(1)
            print("YOU DEFEATED THE DARK LORD!")
            dark_lord_beaten = True
            sleep(2.5)
        elif decision.lower() == "anti-aircraft gun":
            print("You decided to use the anti-aircraft gun.")
            print("")
            sleep(1)
            print("You destroyed all of the DARK LORD's minions!")
            sleep(1)
            print("You now have two choices: ")
            print("")
            while True:
                print(">>Actions:" + '\n' + "(1)Finish off the DARK LORD" + '\n' +
                       "(2)Spare the DARK LORD")
                decision = input(">")
                if decision in ["1", "2"]:
                    break
                else:
                    notAValidCommand()
            
            if decision == "1":
                print("You decided to finish off the DARK LORD with your anti-aircraft gun.")
                sleep(1)
                print("YOU DEFEATED THE DARK LORD!")
                dark_lord_beaten = True
                sleep(2.5)
            else:
                print("You decided to spare the DARK LORD.")
                print("")
                sleep(1)
                print("[DARK LORD]: You fool!")
                sleep(1)
                print(">>YOU DIED<<")
                deaths += 1
                latest_death = "Evil opportunistic dark lords are vicious, man :("
                continue

        elif decision.lower() == "magical antibiotics":
            print("You decided to use the magical antibiotics")
            print("")
            sleep(1)
            print("You gulped down the antibiotics.")
            sleep(1)
            print("the DARK LORD and his minions stare at you.....")
            sleep(1)
            print(">>YOU DIED<<")
            deaths += 1
            latest_death = "How are antibiotics supposed to make you fight better?"
            continue
        else:
            print("You decided to use the really hot charcoal")
            print("")
            sleep(1)
            print("The really hot charcoal made a fire ring around you!")
            print("Wait.....")
            sleep(2)
            print(".........you're stuck")
            sleep(1)
            print(">>YOU DIED<<")
            deaths += 1
            latest_death = "You weren't supposed to trap yourself :/"
            continue
    elif decision == "2":
        print("You decided to do an epic no-scope.")
        sleep(1)
        if attack >= 100:
            print("You no-scoped every minion in the dining hall!")
            sleep(1)
            print("[DARK LORD]: Did you seriously 360 illuminati no-scope every minion?")
            sleep(1)
            print("You now have two choices:")
            print("")
            while True:
                print(">>Actions: " + '\n' + "(1)Finish off the DARK LORD with a 1080 epic mlg dorito no-scope" + '\n' +
                      "(2)Spare the DARK LORD")
                decision = input(">")
                if decision in ["1", "2"]:
                    break
                else:
                    notAValidCommand()
            
            if decision == "1":
                print("You decided to 1080 epic dorito mlg no-scope the DARK LORD")
                sleep(1)
                print("YOU DEFEATED THE DARK LORD!")
                dark_lord_beaten = True
                oneeighty_noscope = True
                sleep(2.5)
            else:
                print("You decided to spare the DARK LORD.")
                print("")
                sleep(1)
                print("[DARK LORD]: You fool!")
                sleep(1)
                print(">>YOU DIED<<")
                deaths += 1
                latest_death = "Evil opportunistic dark lords are vicious, man :("
                continue
                
        else:
            print("However, you tripped in the middle of your no-scope!")
            sleep(1)
            print("the DARK LORD and his minions are laughing at you.")
            sleep(1)
            print(">>YOU DIED<<")
            deaths += 1
            latest_death = "Epic No-Scope Fail 2017 Compilation"
            continue
    elif decision == "3":
        print("You decided to summon a giant explosion.")
        sleep(1)
        if magic >= 50:
            print("The explosion you summmoned defeated all of the DARK LORD's minions!")
            sleep(1)
            print("[DARK LORD]: WHAT HAPPENED TO ALL MY MINIONS???!!!")
            sleep(1)
            print("You now have two options:")
            print("")
            while True:
                print(">>Actions:" + '\n' +"(1)Finish off the DARK LORD" + '\n' + "(2)Spare the DARK LORD")
                decision = input(">")
                if decision == "1" or decision == "2":
                    break
                else:
                    notAValidCommand()
            if decision == "1":
                print("You finished off the DARK LORD with another explosion.")
                sleep(1)
                print("YOU DEFEATED THE DARK LORD!")
                dark_lord_beaten = True
                sleep(2.5)
            else:
                print("You decided to spare the DARK LORD.")
                print("")
                sleep(1)
                print("[DARK LORD]: You fool!")
                sleep(1)
                print(">>YOU DIED<<")
                deaths += 1
                latest_death = "Evil opportunistic dark lords are vicious, man :("
                continue
        else:
            print("However, instead of an explosion, all that came out was glitter.")
            sleep(1)
            print(">>YOU DIED<<")
            deaths += 1
            latest_death = "Erm.. I don't think glitter is helpful here..."
            continue
    elif decision == "4":
        print("You decided to use the power of friendship.")
        print("")
        sleep(1)
        print("[DARK LORD]: Make it stop!!! The power of friendship burns!")
        sleep(1)
        print("The power of friendship is too strong for the DARK LORD!")
        sleep(1)
        print("YOU DEFEATED THE DARK LORD (somehow)")
        anime_ending = True
        sleep(2.4)
        print("[DARK LORD]: lol just kidding the power of friendship doesn't affect me.")
        sleep(1)
        print(">>YOU DIED<<")
        deaths += 1
        latest_death = "I thought that the power of frienship could defeat all evil >:("
        continue
    else:
        print("You decided to help the DARK LORD")
        sleep(1)
        print("")
        print("The DARK LORD's minions look confused")
        print("")
        sleep(1)
        print("[DARK LORD]: What are you going to help me with???")
        sleep(1)
        print("You explain that you read his diary (and stole his underwear)")
        print("")
        sleep(1)
        print("[DARK LORD]: YOU STOLE MY UNDERWEAR?!?!!?")
        sleep(1)
        if "magical antibiotics" in inventory:
            print("Acting quickly, you hand over the magical antibiotic to the DARK LORD.")
            sleep(1)
            print("The DARK LORD seems grateful.")
            sleep(1)
            print("[DARK LORD]: Finally, I can cure my dead child!")
            sleep(1)
            print("You become BFFs with the DARK LORD.")
            bffs = True
        else:
            print(">>YOU DIED<<")
            deaths += 1
            latest_death = "It turns out that evil dark lords don't like their underwear stolen."
            continue
    
    print("-----THE END-------")
    #Credits
    if attack == 0 and magic == 0:
        peasant = True
    sleep(1)
    print("A GAME MADE BY MYSTICFL0WER")
    print("")
    sleep(1)
    print("DIRECTOR")
    print("MysticFl0wer")
    print("")
    sleep(1)
    print("LEAD PROGRAMMER")
    print("MysticFl0wer")
    print("")
    sleep(1)
    print("YOUR MOM")
    print("MysticFl0wer")
    print("")
    sleep(1)
    print("Deaths from this run: " + str(deaths))
    print("")
    #Achievements section
    print("------ACHIEVEMENTS-----")
    print("")
    sleep(1)

    if crunchu_crunchy:
        print("Delicious! - Eat Crunchy Crunchy Cereal, the cereal that's crunchy AND melts in your mouth at the same time!")
        num_of_achievements += 1
    else:
        print("Delicious! - ???????????")
    
    print("")

    if liver_stolen:
        print("Last Surprise - Have your liver stolen by the Phatom Thieves")
        num_of_achievements += 1
    else:
        print("Last Surprise - ???????????")
    
    print("")
    
    if sanctuary_beaten:
        print("Take it from me, if you dare... - Beat the Sanctuary Guardian")
        num_of_achievements += 1
    else:
        print("Take it from me, if you dare... - ???????????")
    
    print("")

    if xxx_noscopethreesixty:
        print("xX_n00bslay3r_Xx - Do a 360 no-scope to beat the Sanctuary Guardian")
        num_of_achievements += 1
    else:
        print("xX_n00bslay3r_Xx - ???????????")
    
    print("")
    
    if oneeighty_noscope:
        print("2017 MLG BEST NO-SCOPE - Do a 1080 no-scope")
        num_of_achievements += 1
    else:
        print("2017 MLG BEST NO-SCOPE - ???????????")
    
    print("")
    
    if undies_acquired:
        print("Under Where? - Acquire the DARK LORD's underwear")
        num_of_achievements += 1
    else:
        print("Under Where? - ???????????")
    
    print("")
    
    if bffs:
        print("Best Friends Forever - Become best friends with the DARK LORD")
        num_of_achievements += 1
    else:
        print("Best Friends Forever - ???????????")
    
    print("")

    if anime_ending:
        print("The Power of Clichés - Try to use the power of friendship against the DARK LORD")
        num_of_achievements += 1
    else:
        print("The Power of Clichés - ???????????")
    
    print("")
    
    if crunchy_dark_lord:
        print("Crunchy Crunchy DARK LORD - Have GOMORRAH eat the DARK LORD")
        num_of_achievements += 1
    else:
        print("Crunchy Crunchy DARK LORD - ???????????")
    
    print("")

    if dark_lord_beaten:
        print("The End - Defeat the DARK LORD")
        num_of_achievements += 1
    else:
        print("The End - ???????????")
    
    print("")

    if peasant:
        print("Still a Peasant - Beat the game with all your stats at zero")
        num_of_achievements += 1
    else:
        print("Still a Peasant - ???????????")
    
    print("")
    #Prints out the number of achievements they got
    print("Number of achievements got: " + str(num_of_achievements) + " / " + str(total))
    sleep(5.2)
    print("")
    
    while True:
        print(">>Type 'y' to play the game again. Type 'n' to exit.")
        sleep(1)
        if num_of_achievements == total:
            print(">>Congratulations! You got all achievements. Type 's' to play the exclusive side quest.")
        decision = input(">")
        if decision.lower() == "y" or decision.lower() == "n":
            break
        elif decision.lower() == "s" and num_of_achievements == total:
            print(">>WARNING: You will not be able to go back to the main game once you start.")
            decision = input("Are you sure you want to continue? (yes/no): ")
            if decision.lower() == "yes":
                side_quest = True
                break
            elif decision.lower() == "no":
                continue
            else:
                notAValidCommand()
        else:
            notAValidCommand()
        
    #If the user wants to play again to get more achivements
    if decision.lower() == "y":
        deaths = 0
        latest_death = "None"
        name = input("Type your name: ") or 'Flipper Flopper'
        continue
    elif decision.lower() == "n":
        print("Thank You For Playing!")
        break
    else:
        break


        
        