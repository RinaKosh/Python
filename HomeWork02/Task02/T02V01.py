# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывести в консоль сам список и сумму его элементов.

n = int(input('Введите число '))
my_list = []
for i in range (n):
    my_list.append((1 + 1/n)**n)
print (*my_list, sep=', ')
c = 0
for i in my_list:
    c = float(i)+c
print ('Сумма элементов равна', c)