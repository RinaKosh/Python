from random import randint as rnd

my_list= []
for i in range (9):
    my_list.append(rnd(1,100))
print(*my_list, sep=' ')
i = 1
step = 2
sum = 0 

while i <= len(my_list)-1:
    print(i)
    sum = my_list[i] + sum
    i = i+step
print(sum)
    

    


    