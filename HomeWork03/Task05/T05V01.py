# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).

a = int(input('Введите целое число = '))

my_list = [1, 0, 1]
prev_value = 0
current = 1
current_neg = 1
prev_neg_value = 0

for i in range(a - 1):
    new = prev_value + current
    new_neg = prev_neg_value - current_neg
    my_list.append(new)
    my_list.insert(0, new_neg)
    prev_value = current
    current = new
    prev_neg_value = current_neg
    current_neg = new_neg
    
print('список чисел Фибоначчи: ', my_list)