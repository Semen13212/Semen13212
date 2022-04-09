# Это игра орел и решка
import random

print('Привет! Как тебя зовут?')

myName = input()

number = random.randint(1,2)

print('Что ж, '+myName+', я подбрасываю монетку.')
print('Попробуй угадать.')
print('Введи 1, если выбрал "орел" и 2, если выбрал "решка".')

guess = input()
guess = int(guess)

if guess == number:
    print('Отлично, '+myName+'! Ты выйграл!')

if guess != number:
    print('Увы, '+myName+'. Ты ЛОХ.')