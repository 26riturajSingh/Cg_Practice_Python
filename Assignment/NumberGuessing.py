'''
Number Guessing Game Objectives:
Allow the player to submit a guess for a number between 1 and 100.
Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
If they got the answer correct, show the actual answer to the player.
Track the number of turns remaining.
If they run out of turns, provide feedback to the player.
Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

Points to consider.
•	#1: Appropriate error messages if user tries to enter a non number
•	#2: Number can be positive or Negative
•	#3: User allowed to choose easy or Hard mode of the game.
Expected Learning:
Participants will learn following concepts from this assignment.
•	Basic programing building blocks like functions, scope of variables, importing modules like  random.

Duration of the project:  2Hrs
Sample Output:
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': hard
You have 5 attempts remaining to guess the number.
Make a guess: 20
Too low.
Guess again.
You have 4 attempts remaining to guess the number.
Make a guess: 40
You got it! The answer was 40.
'''
import random as r
import math as m
num = r.randint(1,100)
print(num)
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
print("Choose a difficulty. Type 'easy' or 'hard'")
mode = input()


b = 5

if mode == "easy" or mode == "hard":
    while b>0:
        print(f"You have {b} attempts remaining to guess the number.")
        print("Make a guess:")
        guess = int(input())
        match guess:
            case n if n == num:
                print(f"You got it! The answer was {n}.")
                b = 0
            case _ if (mode == "easy"):
                b -= 1
                diff = num - guess
                if(m.fabs(diff) >= 10 and diff > 0):
                    print("Too low.")
                elif (m.fabs(diff) >= 10 and diff < 0):
                    print("Too high.")
                elif (m.fabs(diff) <= 10 and diff > 0):
                    print("Low.")
                elif (m.fabs(diff) <= 10 and diff < 0):
                    print("High.")
            case _ if (mode == "hard"):
                b -= 1
                diff = num - guess
                if (m.fabs(diff) >= 5 and diff > 0):
                    print("Too low.")
                elif (m.fabs(diff) >= 5 and diff < 0):
                    print("Too high.")
                elif (m.fabs(diff) <=5 and diff > 0):
                    print("Low.")
                elif (m.fabs(diff) <=5 and diff < 0):
                    print("High.")
            case _ :
                print("Type 'easy' or 'hard'")
else:
    print("Invalid mode. Please enter either 'easy' or 'hard'.")