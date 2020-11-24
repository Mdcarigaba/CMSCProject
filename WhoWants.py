import time
import INTRO
import ASSETS

#Main Menu
print("\t----------------------------------")
print("\t| Who Wants to be a Millionaire? |")
print("\t----------------------------------")
print("\n\t\t (1) Play")
print("\t\t (2) Show Leaderboards")
print("\t\t (3) Quit")

n = 1
while n == 1:
    c1 = int(input("\t\tPlease enter your choice: "))
    if c1 == 1:
        print("Hello! What's your name?")
        name = str(input("Enter name: "))
        INTRO.rules(name)
        break

    elif c1 == 2:
        with open("Leaderboards.txt", "a+") as f:
            if f.tell() == 0:
                f.write("\t----------------------")
                f.write("\t|    Leaderboards    |")
                f.write("\t----------------------")
            else:
                #header = 
                txt = f.read()
                print(txt)
        f.close()
        break

    elif c1 == 3:
        exit()
    else:
        print("Incorrect value. Try again.")
