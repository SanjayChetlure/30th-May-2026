print("------Ex11: Fibonacci Series------")


num1 = 0   #1
num2 = 1   #2


for i in range(10):
   print(num1, end=" ")    #0  1 1
   num3 = num1 + num2       #2
   num1 = num2              #1
   num2 = num3
