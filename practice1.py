import random
x=int(input("please enter count of your list: "))
num=[random.randint(0,1000)]

for i in range(x):
   y=(random.randint(0,1000))
   if y!=num[i-1]:
    num.append(y)
   
    
print (num)