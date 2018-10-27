#Basilio Bazan III
#bb36366
import random

def main():
   print("Welcome to the Virtual Magic 15 Ball Program")
   name = input("What is your name? ")
   magicBall = ["Yes", "No", "Yes, but not now", "Um, definitely no", "That is a terrible idea",
                "Why would you even ask that?", "Only on Sundays", "Only if you don’t want lunch",
                "You really wasted a question on that but sure", "In your dreams!", "Never", "Duh, of course",
                "HA! You wish", "C'mon, you know that answer already", "I don't know"]
   input("What is your question? ")
   genNum = random.randint(0, 14)
   print(name + ", your answer is: " + magicBall[genNum])

main()
