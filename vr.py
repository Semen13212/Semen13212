from inspect import Attribute
import numbers
import random

Attribute = 0

print("Привет! КАК тебя завут")
v = random.randint(1,20)
print("Что ж,"+"myName"+",я загадываю число от 1 до 20")
for attNumber in range(6):
    print("попрбуй угадать.")
    guess = input()
    guess = int(guess)
    if guess < numbers.Number:
        print("meniwe lox")
    if guess > numbers.Number:
        print("boliwe lox")
    if guess == numbers.Number:
        break
if guess == numbers:
    attNumber = str(attNumber + 1)
    print("Malodec,"+"myName+"'!')