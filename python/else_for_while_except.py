# for
# Блок else выполняется, только если цикл for дощел до конца
# т.е. не было преждевременного выхода с помощью break
def else_for(letters: list):
    for letter in letters:
        if letter == 'e':
            break
        print(letter)
    else:
        print('Done')
    print('-'*50)


else_for(['a', 'b', 'c', 'd'])
else_for(['a', 'b', 'c', 'd', 'e', 'f'])


# while
# Блок else выполняется, только если цикл while завершился вследствие того,
# что условие приняло ложное значение (не в результате выхода с помощью break)
def else_while(letters: list):
    index = 0
    while index != len(letters):
        letter = letters[index]
        print(letter)
        if letter == 'e':
            break
        index += 1
    else:
        print('Done')
    print('-'*50)


else_while(['a', 'b', 'c', 'd'])
else_while(['a', 'b', 'c', 'd', 'e', 'f'])


# try
# Блок else выполняется только, если в блоке try не возникло исключение
def else_try(letters: list):
    try:
        if 'e' in letters:
            raise ValueError
    except ValueError:
        print('letter `e` in letters')
    else:
        print('Done')
    print('-'*50)


else_try(['a', 'b', 'c', 'd'])
else_try(['a', 'b', 'c', 'd', 'e', 'f'])
