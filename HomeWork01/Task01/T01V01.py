# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

x = int(input('Введите день недели цифрой'))
if 0 < x < 6: 
    print('рабочий день')
elif x == 6 or x ==7:
    print('выходной день')
else:
    print('некорректный формат данных, введите число от 1 до 7')
    
    