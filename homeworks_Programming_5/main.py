# Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

'''
def factr(n):
    if n == 1:
        return n
    else:
        return n*factr(n-1)
print(factr(int(input())))
'''
'''
def trin(n):
    if n == 1:
        return 1
    else:
        return n + trin(n-1)
print(trin(int(input())))
'''

# Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

'''
def summ (a, b):
    if b == 0:
        return a
    return summ(a,b-1)+1
num1 = int(input("Введи число А: "))
num2 = int(input("Введи число Б: "))
print(summ(num1, num2))
'''