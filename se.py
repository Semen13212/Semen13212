import random
def sozdanieV():
    HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''','''
  +---+
  0   |
      |
      |
     ===''','''
  +---+
  0   |
  |   |
      |
     ===''','''
  +---+
  0   |
 /|   |
      |
     ===''','''
  +---+
  0   |
 /|\  |
      |
     ===''','''
  +---+
  0   |
 /|\  |
 /    |
     ===''','''
  +---+
  0   |
 /|\  |
 / \  |
     ===''','''
  +---+
 [0   |
 /|\  |
 / \  |
     ===''','''
  +---+
 [0]  |
 /|\  |
 / \  |
     ===''','''
  +---+
 [0]  |
[/|\  |
 / \  |
     ===''','''
  +---+
 [0]  |
[/|\] |
 / \  |
     ===''']
    return HANGMAN_PICS 

words = {'цвета':'красный оранжевый желтый зеленый голубой синий фиолетовый белый черный коричневый'.split(),
'фигуры':'треугольник квадрат прямоугольник круг овал пятиугольник трапеция ромб шестиугольник звезда'.split(),
'фрукты':'апельсин ананас абрикос банан виноград груша грейпфрукт яблоко лимон лайм мандарин персик манго нектарин'.split(),
'животные':'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'.split()}

def getRandomWord(wordList):
    # Эта функция возвращает случайную строку из переданного списка.
    wordKey = random.choice(list(wordList.keys()))

    wordIndex = random.randint(0, len(wordList[wordKey])-1)
    return [wordList[wordKey][wordIndex],wordKey]

def displayBoard(missedLetters, correctLetters, secretWord,hang):
    print(hang[len(missedLetters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # заменяет пропуски отгаданными буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # показывает секретное слово с пробелами между буквами
        print(letter, end=' ' )
    print()

def getGuess(alreadyGuessed):
    # возвращает букву, введенную игроком. Эта функция проверяет, что игрок вве только одну букву и ничего больше
    while True:
        print('Введите букву.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйста, введите одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже называли эту букву. Назовите другую.')
        elif guess not in 'абвгдежзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ')
        else:
            return guess

def playAgain():
    # Эта функция возвращает True, если игрок хочет сыграть заново, в противном False
    print('Хотите сыграть еще? (да или нет).')
    while True:
        otvet = input().lower()
        if (otvet == 'да') or (otvet == 'д') or (otvet == 'yes') or (otvet == 'y'):
            # ответ да, запускаем игру по новой
            return True
        elif (otvet == 'нет') or (otvet == 'н') or (otvet == 'no') or (otvet == 'n'):
            # игрок отказался от игры, завершаем
            return False
        else:
            print('''Я вас не понял! 
Введите ответ еще раз.
Введите "да" для продолжения и "нет" для завершения игры''')

def vyborSl():
    print('Выберите уровень сложности.')
    print('Введите "Л" для легкого,')
    print('"С" для среднего и')
    print('"Т" для тяжелого уровня сложности"".')
    while True:
        otv = input().upper()
        if len(otv) != 1:
            print('Ведите одну букву')
        elif otv not in 'ЛСТ':
            print('Введите Л, С или Т')
        else:
            return otv

def delVis(vybS,hangP):
    if vybS == 'С':
        del hangP[10]
        del hangP[9]
    elif vybS == 'Т':
        del hangP[10]
        del hangP[9]
        del hangP[8]
        del hangP[7]

#hm = HANGMAN_PICS

#bS = vyborSl()
#delVis(bS,hm)
delV = True
errorB = ''
yesB = ''
gameOver = False
sicretS,keyWords = getRandomWord(words)

while True:
    if delV:
        hm = sozdanieV()
        
        bS = vyborSl()
        delVis(bS,hm)
        delV = False

    if bS == 'Л':
        print('Категория слова: '+keyWords)
    displayBoard(errorB,yesB,sicretS,hm)

    bukva = getGuess(errorB+yesB)

    if bukva in sicretS:
        yesB = yesB + bukva
 
        # Проверяет, выиграл ли игрок
        ssYes = True
        for i in range(len(sicretS)):
            if sicretS[i] not in yesB:
                ssYes = False
                break
        if ssYes:
            print('ДА! Секретное слово - "'+sicretS+'"! Вы угадали!')
            gameOver = True
    else:
        errorB = errorB + bukva
        if len(errorB) == len(hm) - 1:
            displayBoard(errorB,yesB,sicretS,hm)
            print('Вы исчерпали все попытки!\nНеугадано букв:'+str(len(errorB))+'\nугадано букв:'+str(len(yesB))+'.\nБыло загадано слово "'+sicretS+'".')
            gameOver = True

    # Запрашивает, хочет ли игрок сыграть заново (только если игра завершена).
    if gameOver:
        if playAgain():
            errorB = ''
            yesB = ''
            gameOver = False
            sicretS,keyWords = getRandomWord(words)
            delV = True
        else:
            break
