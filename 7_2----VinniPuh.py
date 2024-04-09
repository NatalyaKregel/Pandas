'''Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
Вам стоит написать программу.

Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами.

Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. 
В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, 
если с ритмом все не в порядке. Если фраза только одна, то ритм определить не получится 
и необходимо вывести: Количество фраз должно быть больше одной!.'''
'''
def rhythm(str):
    str = str.split()
    list_1 = []
    for word in str:
        sum_w = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                sum_w += 1
        list_1.append(sum_w)
    return len(list_1) == list_1.count(list_1[0])


str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
if rhythm(str_1):
    print('Парам пам-пам')
else:
    print('Пам парам')
    '''
'''    
stroka = "пара-ра-рам рам-пам-папам па-ра-па-дам"
lines = stroka.split()
 
print(lines)
 
lst = [sum(x in 'уеыаоэяию' for x in lin)
 for lin in lines]
 
if len(set(lst)) == 1 :
    res = "Парам пам-пам"  
else: res = "Пам парам"
 
print(res)

else:
    print('Количество фраз должно быть больше одной!')


'''


stroka = "пара-ра-рам рам-пам-папам па-ра-па-дам"
lines = stroka.split()
 
def count_syllables(phrase):
    """
    Функция для подсчета слогов (гласных букв) во фразе.

    Args:
    phrase: Фраза, в которой нужно посчитать слоги.

    Returns:
    Количество слогов во фразе.
    """
    vowels = "аеёиоуыэюя"
    count = 0
    for char in phrase.lower():
        if char in vowels:
            count += 1
    return count

def check_rhythm(poem):
    """
    Функция для проверки ритма в стихотворении.

    Args:
    poem: Стихотворение, в котором нужно проверить ритм.

    Returns:
    True, если в стихотворении есть ритм, False - если нет.
    """
    phrases = poem.split()
    syllables_count = count_syllables(phrases[0])
    for phrase in phrases[1:]:
        if syllables_count != count_syllables(phrase):
            return False
    return True


if stroka.contains(' '):
    if check_rhythm(stroka):
        print("Парам пам-пам")
    else:
        print("Пам парам")
else:
    print('Количество фраз должно быть больше одной!')