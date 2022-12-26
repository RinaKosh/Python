# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res


def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

a=input('Введите текст для кодировки ')
c=coding(a)
s=open('ForCoding.txt','w')
s.write(c)
s.close()

data=''
s=open('ForCoding.txt','r')
for i in s:
    data=i
print(data)
b=decoding(data)
print(f'Текст после дешифровки: {b}')
s=open('ForDecoding.txt','w')
s.write(b)
s.close()
