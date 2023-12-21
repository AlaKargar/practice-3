num=int(input("please enter yur num: "))
snake=[]
for i in range(num):
  if i%2==0:
      snake.append("*")
  else:
      snake.append("#")
print(snake)


    