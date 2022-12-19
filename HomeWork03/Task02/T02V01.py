# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint as rnd

my_list= []
for i in range (4):
    my_list.append(rnd(1,100))
print(*my_list, sep=' ')

last_index=len(my_list)-1
c=[]
for i in range(len(my_list)):
    if i > last_index:
        break
    p=my_list[i]*my_list[last_index]
    c.append(p)
    last_index=last_index-1
    print(p)
print(f'Произведение пар чисел списка{my_list} равно {c}')

    

