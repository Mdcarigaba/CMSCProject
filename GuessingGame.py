import random

n = random.randint(1, 50)

i = 1
print("GUESSING GAME. Guess the number from 1 to 50. Five tries only")
while i < 6:
    ans = int(input("Enter guess: "))
    if ans < n:
        if (5-i) == 0:
            print("You lose. The number was:", n)
        elif (5-i) > 1:
            print("Higher!", 5 - i, "Guesses left.")
        else:
            print("Higher!", 5 - i , "Guess left.")
    elif ans > n:
        if (5-i) == 0:
            print("You lose. The number was:", n)
        elif (5-i) > 1:
            print("Lower!", 5 - i, "Guesses left.")
        else:
            print("Lower!", 5 - i , "Guess left.")
    else:
        print("Congrats! You got it correct!")
    i += 1