#Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
#не превосходящие числаN.


n = int(input('Введите число N: '))
k = 0
res = 1
while res < n+1:
    print(res)
    k += 1
    res = 2 ** k