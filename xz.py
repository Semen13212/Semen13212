import random, time

print('как тебя завут'):
myName = imput()

def displayIntro:
    print(myName+''', вас нашол абоба и хочет cъесть вас вам нужно выйграть чтобы выжить...''')
    time.sleep(2)   
    print('''он рычит''')
    time.sleep(2)
    print('''он ждёт когда вы зделаете выбор''')

def playGemes:
    ctakan = random.randint(1,3)
    print('''выбери какой ты стакан будещ открывать 1-3''')
    vybor = input()
    if ctakan == int(vybor):
        

    if ctakan != int(vybor):