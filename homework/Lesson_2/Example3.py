n = int(input("Введите число:"))
list = [ ]
s = 0
for i in range(1, n+1):
    list.append(round((1 + 1/i)**i))
    s = s + list[i-1]
print(f'Для n = {n}: {list} -> {s}')
