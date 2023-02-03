import random
def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True
print("comp turn : snake(s),gun (g),water(w)")
randomno = random.randint(1,3)
if randomno == 1:
    comp = "s"
elif randomno == 2:
    comp = "w"
elif randomno == 3:
    comp = "g"
you = input("your turn : snake(s),gun (g),water(w)")
a = gamewin(comp,you) 
print(f"computer choose {comp}")
print(f"you choose {you}")
if a == None:
    print("The game is a tiel")
elif a:
    print("Game is win")
else:
    print("game is lose")  