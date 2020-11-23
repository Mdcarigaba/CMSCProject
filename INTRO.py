import time
import random
import sys

#Rules and info about the Lifelines
def rules(name):
    print(name, ", Would like the game to be in English or in Filipino?")
    n = 1
    while n == 1:
        ch = str(input("Enter language: "))
        if ch.lower() == "english":
            print("Ok", name, "listen closely.\n")
            time.sleep(2)
            print("There are 5 questions each for the Easy, Average, and Difficult rounds, resulting to a total of 15 questions.\n")
            time.sleep(2)
            print("Each correctly answered question will reward you a cash price.\n")
            time.sleep(2)
            print("The cash prices rise from 1,000 pesos to 1,000,000 pesos.\n")
            time.sleep(2)
            print("You can choose to walk away with your price before a question is given to you.\n")
            time.sleep(2)
            print("If you answer incorrectly, you walk away with 1/4 of your earnings.\n")
            time.sleep(4)
            print("\nYou have 2 lifelines.\n")
            time.sleep(2)
            print("PHONE A FRIEND: \n")
            time.sleep(2)
            print("You can choose from 1 of your 3 friends to help you on the question.\n")
            time.sleep(2)
            print("It is your choice to take their advice or not.\n")
            time.sleep(3)
            print("50/50: \n")
            time.sleep(2)
            print("Two incorrect choices will be removed from the set of choices.\n")
            time.sleep(4)
            print("Are you ready?, ",name)
            ch1 = str(input("y/n: "))
            if ch1.lower() == "y":
                print("Then let's play Who Wants to be a Millionaire!")
                break
            else:
                print("What do you mean no? Let's play Who Wants to be a Millionaire!")
                break
        elif ch.lower() == "filipino":
            print("Ok,", name, "makinig nang mabuti.\n")
            time.sleep(2)
            print("Mayroong 5 na tanong bawat lebel ng Easy, Average, at Difficult na bumubuo sa 15 na katanungan.\n")
            time.sleep(2)
            print("Ang bawat tamang sagot ay gagantimpalaan ka ng cash price.\n")
            time.sleep(2)
            print("Magsisimula ang halaga nito mula 1,000 pesos paakayat ng 1,000,000 pesos\n")
            time.sleep(2)
            print("Bago magsimula ang isang tanong, maaari kang umuwi na lamang kasama ang lahat ng napanalunan mo.\n")
            time.sleep(2)
            print("Kapag mali ang iyong sagot, iuuwi mo ang 1/4 ng napanalunan mo.\n")
            time.sleep(4)
            print("\nMayroon kang 2 na lifeline.\n")
            time.sleep(2)
            print("PHONE A FRIEND: \n")
            time.sleep(2)
            print("Maaari kang pumili ng 1 sa 3 na kaibigan mo upang tulungan ka sa katanungan.\n")
            time.sleep(2)
            print("Ikaw parin ang may huling desisyon kung paniniwalaan mo ang sagot nila o hindi.\n")
            time.sleep(3)
            print("50/50: \n")
            time.sleep(2)
            print("Ang dalawang maling sagot ay tatanggalin mula sa mga pagpipilian.\n")
            time.sleep(4)
            print("Handa ka na ba?, ", name)
            ch2 = str(input("oo/hindi: "))
            if ch2.lower() == "oo":
                print("Maglaro na tayo ng Who Wants to be a Millionaire!")
                break
            else:
                print("Anong hindi? Kaya mo to! Maglaro na tayo ng Who Wants to be a Millionaire!")
                break
        else:
            print("Unsupported language. Please try again.")