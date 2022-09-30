import math
number = int(input("Введите число N ="))
spisok =[]
for i in range(number):
    spisok.append(math.factorial(i+1)) 
print(spisok)