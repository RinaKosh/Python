from math import sqrt

A = str(input('Введите значения координат x,y,t через запятую для точки A'))
[x, y, t] = A.split(',')
# тут у тебя приведение типов, после можно проверить, что обе компоненты -- число, если нет -- сообщить об ошибке
xA = float(x)
yA = float(y)
tA = float(t)
print(xA, '  ', yA, '  ', tA)
B = str(input('Введите значения координат x,y,t через запятую для точки B'))
[x, y, t] = B.split(',')
xB = float(x)
yB = float(y)
tB = float(t)
print(xB, '  ', yB, '  ', tB)
c =sqrt((xA-xB)**2+(yA-yB)**2+(tA-tB)**2)
print('Расстояние между точкой A и B равно',c) 