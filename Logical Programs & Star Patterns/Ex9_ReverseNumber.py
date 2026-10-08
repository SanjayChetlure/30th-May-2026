print("---9: Reverse Number----")

# Apr1:
num = 12345
rev = int(str(num)[::-1])
print(rev)


 # str(num) converts the number to a string.
 # [::-1] reverses the string.
 # int(...) converts it back to an integer.

print("---------")

# Apr2:
num = 123
rev = 0    #321

    #0>0
while num>0:
   rem=num%10         #get last digit  - FIND reminder     1%10=1
   rev=rev*10+rem     #Append last digit to rev num       0*10+3=3*10+2=32*10+1=321
   num =num//10       #remove last digit                 123/10=12/10=1/10=
print(rev)
