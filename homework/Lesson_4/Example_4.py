import random 
data = open('temp1.txt', 'w')
k = int(input("Задайте натуральную степень к: "))

while k > 0:
    num = random.randint(0,10)
    if num == 0:
        continue
    poly = str(num) + '*x^' + str(k) + ' ' + str(random.choice("+-"))
    k -=1
    print(poly, end = " ")
    data.write(poly)
else:
    poly = str(num) + " = 0"
    print(poly)

data.write(poly)
data.close()

import random

# Второй способ чере функцию
# num = int(input("Введите натуральную степень k: "))

# def magit_to_file(num: int):
#     if num != 0 and num > 0:
#         with open('temp1.txt', "a", encoding="utf-8") as file:
#             for i in reversed(range(1, num+1)):
#                 num1 = random.choice(range(5))
#                 if num1 == 0:
#                     continue
#                 print(f"{num1}*x^{i} {random.choice(['+', '-'])}", file=file, end=" ")

#             else:

#                 print(f"{num1} = 0", file=file)


# magit_to_file(num)





