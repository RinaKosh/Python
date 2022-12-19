from random import uniform as rnd

my_list= [9, 0.66, 1, 2.3, 4.76, 98.098]

min=1
max=0
for i in my_list:
    x= i%1
    if x<min and x !=0:
        min=x
    if x>max:
        max=x
d=max-min
print(min)
print(max)
print(d)
    