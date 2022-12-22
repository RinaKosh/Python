# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint as rnd

k = int(input('Введите число k: '))

K=[]
for i in range(k + 1):
    K.append(rnd(0,100))
 
equalation = []
for i in (range(len(K))):
    coef = K[i]
    pow = k - i
    if (coef == 1):
        if (pow != 0):
            equalation.append('x**' + str(pow))
    elif(coef != 0):
        if (pow !=0):
            equalation.append(str(coef) + '*x**' + str(pow))
        else:
            equalation.append(str(coef))

R= ' + '.join(equalation)
print(K)
print('Результат', R)

data=open('file.txt','a')
data.writelines(R)
data.close()

