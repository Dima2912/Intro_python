def product_of_numbers(list, number1,number2):
    p = list[number1 - 1]*list[number2 - 1]
    return p

n = int(input("Number of elements= "))
s = []
for i in range(-n, n+1):
    s.append(i)

n1 = int(input("Positoin one: "))
n2 = int(input("Positoin two: "))

print(s)
print(product_of_numbers(s, n1, n2))