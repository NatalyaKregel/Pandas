'''Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
5
1 2 3 4 5
3
-> 1'''
list_1 = [1, 2, 3, 4, 5]
k = 3
#from random import randint
#list_1 = [randint(1, 9) for k in range(int(input('Введите размер массива: ')))]
#print(list_1)
print(list_1.count(k))