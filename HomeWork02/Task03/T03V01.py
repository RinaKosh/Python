# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

from random import randint as rnd

size = int(input('Введите размер списка: '))
rnd_list = []
for i in range (size):
    rnd_list.append(rnd(0,100))
print (rnd_list)
for i in range (len(rnd_list)): 
    temp = rnd_list[i]
    target_index = rnd(0, size-1)
    target_value = rnd_list[target_index]
    rnd_list[target_index] = temp
    rnd_list[i] = target_value
print (rnd_list)
