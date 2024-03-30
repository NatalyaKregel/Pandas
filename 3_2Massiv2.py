'''Требуется найти в массиве list_1 самый близкий по значению элемент 
к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. 
Если значение k совпадает с этим элементом - выведите его.'''

list_1 = [1, 2, 3, 4, 5]
k = 6

'''from random import randint
list_1 = [randint(1, 99) for i in range(int(input('Введите размер массива: ')))]
print(list_1)
k = int(input('Введите искомое число: '))
input_set = set(list_1)'''
dif = 0
if k > max(list_1):
    print(max(list_1))
elif k < min(list_1):
    print(min(list_1))
else:
    while True:
        if k - dif in list_1 and k + dif in list_1 and k - dif != k + dif:
            print(k - dif, k + dif)
            break
        elif k - dif in list_1:
            print(k - dif)
            break
        elif k + dif in list_1:
            print(k + dif)
            break
        else:
            dif += 1