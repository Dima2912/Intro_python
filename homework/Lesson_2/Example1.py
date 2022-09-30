n = input("Введите число = ")
s = n.replace('.', '')
sum = 0
for i in s:
    sum += int(i)
print(sum)

# Второй способ решения через if
# n = input("Введите число = ") 
# sum = 0
# for i in n:
#     if i != '.':
#         sum += int(i)
# print(sum)



