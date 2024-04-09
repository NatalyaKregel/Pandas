'''Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются 
в обоих наборах.
На вход подается 2 числа через пробел: n m
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем подаются элементы каждого множества через пробел в виде строки. ! 
Писать input() не надо'''

# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
'''
var1 = set(map(int, input(f'введи кол-во элементов 1го и 2го множества через пробел: ').split()))
var2 = set(map(int, input(f'введи элементов 1го множества через пробел: ').split()))
var3 = set(map(int, input(f'введи элементов 2го множества через пробел: ').split()))

var4 = var2.intersection(var3)

numbers = var4

for num in numbers:
    print(num, end=' ')




from random import randint
n_set = set(randint(1, 20) for i in range(int(input(' Введите кол-во элементов первого множества: '))))
print(n_set)
m_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов второго множества: '))))
print(m_set)
s_set = sorted(n_set.intersection(m_set))
print(*s_set)


var1 = '5 4' 
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5' 

var1 = '5 5'
var2 = '10 20 30 40 50'
var3 = '10 20 30 40 50'
#var1 = [int(x) for x in input().split()]
n = var1[0]
m = var1[1]
myset_1 = set()
myset_2 = set()
list_1 = list()
#var2 = [int(x) for x in input().split()]
k = set(var2)
for i in k:
    myset_1.add(i)
#var3 = [int(x) for x in input().split()]
k1 = set(var3)
for i in k1:
    myset_2.add(i)
lok = myset_1 & myset_2
kool = list(lok)
kool.sort()
for i in kool:
    print(i, end=' ')
____________________________________
#var1 = map(int, input().split())
#var2 = set(map(int, input().split()))
#var3 = set(map(int, input().split()))

var1 = '5 5'
var2 = '10 20 30 40 50'
var3 = '10 20 30 40 50'

var4 = map(int, var1)
var5 = set(var2)
var6 = set(var3)
print(*sorted(var5 & var6))
'''
var1 = '5 5'
var2 = '10 20 30 40 50'
var3 = '10 20 30 40 50'

s_var2 = var2.split()
s_var3 = var3.split()
s_var4 = []
for num2 in s_var2:
    for num3 in s_var3:
        if num2 == num3 and num2 not in s_var4:
            s_var4.append(num2)
print(" ".join(s_var4))