print("------Ex10: Armstrong Number------")

num = 111      #1+125+27=153
orgNum=num
sum = 0   #153

#     0>0
while num>0:
   rem=num%10     #get last digit  - FIND reminder     1%10=1
   sum=sum + rem*rem*rem       # 0+ 27=27+125=152+1=153
   num =num//10      #153/10=15/10=1/10=0

# print(sum)

if orgNum == sum:
   print("Given num is armstrong")
else:
   print("Given num is not armstrong")
