# Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера. Первый ход определяется жеребьёвкой.За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Подумайте как наделить бота ""интеллектом""

from random import randint


def input_dat(name):
   
    x = int(input(f'{name}, Введите количество конфет, которое Вы возьмёте от 1 до 28: '))
    while x < 1 or x > 28:
        x = int(input(f'{name}, Введите корректное количество конфет: '))
    return x


def p_print(name, k, counter, value):
    print(f'Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.')


p1 = input('Введите имя первого игрока: ')
p2 = 'Компьютер'
value = int(input('Введите количество конфет на столе: '))
flag = randint(0, 2) 
if flag:
    print(f'Первый ходит {p1}')
else:
    print(f'Первый ходит {p2}')

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(p1)
        counter1 += k
        value -= k
        flag = False
        p_print(p1, k, counter1, value)
    else:
        k = randint(1,29)
        counter2 += k
        value -= k
        flag = True
        p_print(p2, k, counter2, value)
        
if flag:
    print(f'Выиграл {p1}')
else:
    print(f'Выиграл {p2}')