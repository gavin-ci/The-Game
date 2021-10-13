print("Welcome to the Pokemon World ")
name = input("What is your name? ")
print("Hello " + name)
starter = input("Which starter would you like to have by your side? You can choose from Chimchar the fire type, Turtwig the grass type and Prinplup the water type. Just type the name of the starter you want. ")
print("Good choice! " + starter + " seems to like you! ")
nameCheck = input("Would you like to name your Pokemon? y/n ")
if nameCheck != "n":
    nameStarter = input("Enter the desired name for your " + starter + " .")
else: print(starter + " has joined your team!")
