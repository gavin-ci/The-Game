print("Welcome to the Pokemon World")
name = input("What is your name? ")
print("Hello " + name)
starter = input("Which starter would you like to have by your side? You can choose from Chimchar the fire type, Turtwig the grass type and Prinplup the water type. Just type the name of the starter you want. ")
print("Good choice! " + starter + " seems to like you! ")
nameCheck = input("Would you like to name your Pokemon? y/n ")
if nameCheck != "n":
    nameStarter = input("Enter the desired name for your " + starter + ". ")
    print(nameStarter + " has joined your team!")
else: 
    print(starter + " has joined your team!")

print("You walk through a patch of grass.")
if starter == "chimchar":
    encounter = "Budew"
    print("You got attacked by Budew, a grass type pokemon! ") 
elif starter == "turtwig": 
    encounter = "Starly" 
    print("You got attacked by Starly, a normal type pokemon!")
elif starter == "prinplup":
    encounter = "Bidoof" 
    print("You got attacked by Bidoof, a normal type pokemon!")

battle = input("Would you like to attack or catch the " + encounter + "? ")
if battle == "attack" and nameCheck != "n":
    print(nameStarter + " attacked!")
    print(nameStarter + " has defeated " + encounter + "!")
elif battle == "attack" and nameCheck == "n":
    print(starter + " attacked!")
    print(starter + " has defeated " + encounter + "!")

if battle == "catch":
    print("You throw a pokeball at the opposing " + encounter + "!")
    print("You caught the " + encounter + "!")
    encounterCheck = input("Would you like to name your " + encounter + "? ")
    if encounterCheck == "y":
        encounterName = input("Enter the desired name for your " + encounter + ". ")
        print(encounterName + " has joined the team!")
    else:
        print(encounter + " has joined the team!")

print("You see a boy standing in front of you, he approaches you. Ben: Hello, you're " + name + " right? We heard someone new had just moved into town. Gymleader Brock is just around the corner. What do you think? Wanna fight me or do you feel confident enough to take on the Gym already?")
path = input("Trainer or Gym? ")

if path == "trainer" and battle == "catch" and starter == "chimchar":
    print("You challenged trainer Ben! Trainer Ben sends out Goldeen!")
    if encounterCheck == "y":
        tactic = input("Would you like to attack or switch out to " + encounterName + " ? ")
    else: tactic = input("Would you like to attack or switch out to " + encounter + " ? ")

    if tactic == "switch":
        if encounterCheck == "y":
            print("You switched out to " + encounterName + "! " + encounterName + " used Pound!")
        else:print("You switched out to " + encounter + "! " + encounter + " used Pound!")
    elif tactic == "attack":
        if nameCheck != "n":
            print(nameStarter + " used Scratch! You defeated the opposing Goldeen!")
        else: print(starter + " used Scratch! You defeated the opposing Goldeen!")
else:print("You challenged trainer Ben! Trainer Ben sends out Goldeen!")
if nameCheck != "n":
    print(nameStarter + " used Scratch! You defeated the opposing Goldeen!")
else: print(starter + " used Scratch! You defeated the opposing Goldeen!")

if path == "trainer" and battle == "catch" and starter == "turtwig":
    print("You challenged trainer Ben! Trainer Ben sends out Starly!")
    tactic = input("Would you like to attack or switch out to " + encounterName + " ? ")
    if tactic == "switch":
        if encounterCheck == "y":
            print("You switched out to " + encounterName + "! " + encounterName + "used Scratch!")
        else:print("You switched out to " + encounter + "! " + encounter + " used Scratch!")
    elif tactic == "attack":
        if nameCheck != "n":
            print(nameStarter + " used Pound! You defeated the opposing Goldeen!")
        else: print(starter + " used Pound! You defeated the opposing Goldeen!")    
else:print("You challenged trainer Ben! Trainer Ben sends out Goldeen! You send out ")
if nameCheck != "n":
    print(nameStarter + " used Pound! You defeated the opposing Goldeen!")
else: print(starter + " used Pound! You defeated the opposing Goldeen!")

if path == "trainer" and battle == "catch" and starter == "prinplup":
    print("You challenged trainer Ben! Trainer Ben sends out Cherubi!")
    tactic = input("Would you like to attack or switch out to " + encounterName + " ? ")
    if tactic == "switch":
        if encounterCheck == "y":
            print("You switched out to " + encounterName + "! " + encounterName + " used Pound!")
        else:print("You switched out to " + encounter + "! " + encounter + " used Pound!")
    elif tactic == "attack":
        if nameCheck != "n":
            print(nameStarter + " used Pound! You defeated the opposing Goldeen!")
        else: print(starter + " used Pound! You defeated the opposing Goldeen!")
else:print("You challenged trainer Ben! Trainer Ben sends out Goldeen!")
if nameCheck != "n":
    print(nameStarter + " used Pound! You defeated the opposing Goldeen!")
else: print(starter + " used Pound! You defeated the opposing Goldeen!")

#if path == "Gym":
#print("You challenged Gym Leader Roark! Roark sent out Geodude!")
#tactic = input("Would you like to attack or switch out to")






#log naar console vragen
#kan de code korter?
#win en faal eindes nog