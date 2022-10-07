from decimal import Decimal

n = input("Введите число: ")
while not n.isdigit():
    n = input("Введите число: ")

print(Decimal(n).quantize(Decimal(input('Введите точность вычисления числа: '))))






