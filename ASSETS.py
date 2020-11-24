import time
import random

#Life Lines

#Phone a Friend
f=(random.choice(list(open("trial-questionbank.txt"))))
line = f.split("|")
question = line[0]
answer = line[1].strip("\n").split(",")
def wiseFriend(friend_name,name):
    choice = random.randint(1, 10)
    print(">>> Hello,", friend_name, "Your friend,",name,"needs your help on this question.")
    time.sleep(2)
    print("\tI see. What is the question? <<<")
    time.sleep(2)
    print(question)
    time.sleep(2)
    print("A.) ", answer[0])
    time.sleep(2)
    print("B.) ", answer[1])
    time.sleep(2)
    print("C.) ", answer[2])
    time.sleep(2)
    print("D.) ", answer[3])
    time.sleep(4)
    print("\tThat's a hard question but I will help you! <<<")
    time.sleep(2)
    print("\tHmmm. I think the answer is... <<<")
    time.sleep(4)
    if choice <= 10:
        print(answer[4])
    else:
        n = random.randint(0,3)
        if answer[n] == answer[4]:
            print(answer[n-1])
        else:
            print(answer[n])

def unsureFriend(friend_name,name):
    choice = random.randint(1, 10)
    print(">>> Hello,", friend_name, "Your friend,", name, "needs your help on this question.")
    time.sleep(2)
    print("\tUhh. I don't think I can answer correctly but I'll try. What is the question? <<<")
    time.sleep(3)
    print(question)
    time.sleep(2)
    print("A.) ", answer[0])
    time.sleep(2)
    print("B.) ", answer[1])
    time.sleep(2)
    print("C.) ", answer[2])
    time.sleep(2)
    print("D.) ", answer[3])
    time.sleep(4)
    print("\tI don't think I know this. <<<")
    time.sleep(2)
    print("\tMaybe the answer is... <<<")
    time.sleep(2)
    if choice <= 5:
        print(answer[4])
    else:
        n = random.randint(0, 3)
        if answer[n] == answer[4]:
            print(answer[n - 1])
        else:
            print(answer[n])

def arrogantFriend(friend_name, name):
    choice = random.randint(1, 10)
    print(">>> Hello,", friend_name, "Your friend,", name, "needs your help on this question.")
    time.sleep(2)
    print("\tI see someone is crawling back to me for help. Shoot. <<<")
    time.sleep(2)
    print(question)
    time.sleep(2)
    print("A.) ", answer[0])
    time.sleep(2)
    print("B.) ", answer[1])
    time.sleep(2)
    print("C.) ", answer[2])
    time.sleep(2)
    print("D.) ", answer[3])
    time.sleep(4)
    print("\tThis is so easy! You called me for a simple question? Pathetic. <<<")
    time.sleep(2)
    print("\tThe answer is obviously... <<<")
    time.sleep(2)
    if choice <= 3:
        print(answer[4])
    else:
        n = random.randint(0, 3)
        if answer[n] == answer[4]:
            print(answer[n - 1])
        else:
            print(answer[n])

#arrogantFriend("<input friend name here>", "Kobe") #for trial purposes just remove first '#' then run

#50/50
def fifty_fifty(name):
    n = random.randint(1,3)
    if n == 1:
        print("Here are your new set of choices.")
        if answer[random.randint(0,3)] == answer[4]:
            print("Your remaining choices are:",) #append file here
        else:
            print("Your remaining choices are")