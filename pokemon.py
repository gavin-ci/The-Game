print("Welcome to the Pokemon World ")
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
else:
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






#ik maak een pokemon game voor school feelsgood