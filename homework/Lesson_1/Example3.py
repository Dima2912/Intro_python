# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите координаты точки х:= '))
y = int(input('Введите координаты точки y:= '))
if x > 0 and y > 0 :
    print(f'x={x} y={y} Первая четверть')
elif x < 0 and y > 0 :
    print(f'x={x} y={y} Вторая четверть')
elif x < 0 and y < 0 :
    print(f'x={x} y={y} Третья четверть')
elif x > 0 and y < 0 :
    print(f'x={x} y={y} Четвертая четверть')
elif x == 0 and y == 0 :
    print('Введите координаты не равные 0')

