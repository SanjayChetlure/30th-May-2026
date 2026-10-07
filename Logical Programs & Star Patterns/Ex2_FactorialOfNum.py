print("------Ex2: Factorial of a number------")


num=4              #5*4*3*2*1=120
fact=1  #120
#              6<6
for i in range(1,num+1):
   fact=fact*i      # 1*1=1*2=2*3=6*4=24*5=120

print(fact)

print("-------------")

fact=1
for i in range(2,num+1):
   fact=fact*i

print(fact)
