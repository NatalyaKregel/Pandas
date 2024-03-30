'''Задача 26: Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8'''

a = 3
b = 5
'''
def f(a, b):
    if b == 0:
        return 1
    return a * f(a, b - 1)

#a = int(input('Введите число: '))
#b = int(input('Введите степень: '))
print(f(a, b))

def power(a, b):
    if (b == 1):
        return (a)
    elif (b != 1):
        return (a * power(a, b - 1))
    elif (b == 0):
        return
print(power(a, b))


def power(a, b):
    if b == 0:
        return 1
    elif b % 2 == 1:
        return power(a, b - 1) * a
    else:
        return power(a, b // 2) ** 2
print(power(a, b))'''


def power(a, b):
    res = 1
    for i in range(b):
        res *= a
    return res
        
print(power(a, b))    