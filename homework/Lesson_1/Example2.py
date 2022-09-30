# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
for x in range(2):
    for y in range(2):
        for z in range(2):
            res1 = (not(x or y or z))
            res2 = ((not x) and (not y) and (not z))
            res = (res1 is res2)
            print(x ,y, z, res1, res2, res)