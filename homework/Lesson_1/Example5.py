# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
x1 = int(input('Введите координаты точки A х1:= '))
y1 = int(input('Введите координаты точки A y1:= '))
x2 = int(input('Введите координаты точки B х2:= '))
y2 = int(input('Введите координаты точки B y2:= '))
d = ((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))**0.5
print(round(d, 2))