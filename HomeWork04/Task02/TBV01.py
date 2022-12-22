# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def parse(eq: str):
    partsMap = {}
    parts = eq.split(' + ')
    maxPow = 0
    for part in parts:
        coef = 0
        rest = ''
        pow = 0
        if ('x' not in part):
            coef = int(part)
            pow = 0
        else:
            t = part.split('*x')
            if (len(t) == 2):
                coef = int(t[0])
                rest = t[1]
            else:
                coef = 1
                rest = t[0]

            t = rest.split('**')
            if (len(t) == 2):
                pow = int(t[1])
            else:
                if (t[0] != ''):
                    pow = int(t[0])
                else:
                    pow = 1
        partsMap[pow] = coef
        if(pow > maxPow):
            maxPow = pow
    return [partsMap, maxPow]
    
def combinePartsMap(partsMapA, partsMapB):
    resultMap = partsMapB
    for pow in partsMapA:
        coef = partsMapA[pow]
        coefB = 0
        if (pow in partsMapB):
            coefB = partsMapB[pow]
        resultMap[pow] = coef + coefB
        
    return resultMap
    
def equaliation(maxPow, partsMap):
    equalation = []
    for i in range(maxPow + 1):
        pow = maxPow - i
        if (pow in partsMap):
            coef = partsMap[pow]
            if (coef == 1):
                if (pow != 0):
                    equalation.append('x**' + str(pow))
            elif(coef != 0):
                if (pow !=0):
                    equalation.append(str(coef) + '*x**' + str(pow))
                else:
                    equalation.append(str(coef))
    return ' + '.join(equalation)

def readEqualation(filename):
    data = ''
    file=open(filename,'r')
    for i in file:
        print(i)
        data = i
    file.close()
    return data
    
dataA = readEqualation('file-2.txt')
dataB = readEqualation('file.txt')

[partsMapA, maxPow] = parse(dataA)
[partsMapB, maxPowB] = parse(dataB)
resultMap = combinePartsMap(partsMapA, partsMapB)

if (maxPowB > maxPow):
    maxPow = maxPowB

result = equaliation(maxPow, resultMap)

print(result)
data = open('result.txt', 'w')
data.writelines(result)
data.close()