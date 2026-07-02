

print("---Print num from 1 to 5 without 3rd parameter---")

#start num: 1
#end num: 5
#incr/decr: incr num by 1


#Syntax of for loop
# for variableName in range(startNum,endNum+1, incr/decr(Optional) ):
#     print(variableName)

# by default 3rd parameter : incr by 1

            #  6<6
for i in range(1,6):
    print(i)           #1 2 3 4 5

print("---Print num from 1 to 5 using 3rd parameter(incr/decr)---")

#                2<6
for num in range(1,6,1):
    print(num)

print("----print num from 20 to 50------")
for i in range(20,51):
    print(i)

print("----print num from 101 to 200------")
for i in range(101,201):
    print(i)

print("----print Even numbers from 2 to 8----")
#              10<9
for i in range(2,9,2):
    print(i)           #2 4 6 8


print("----print Even numbers from 20 to 60----")
for i in range(20,61,2):
    print(i)

print("----print table of 5----")
for i in range(5,51,5):
    print(i)

print("----print table of 5----")
for i in range(1,11):
    print(i*5)

print("----print square of num from 5 to 10-----")
for i in range(5,11):
    print(i*i)

print("------print any msg 5 times-------")
#              6<6
for i in range(1,21):
    print("hi")       #hi hi hi hi hi


print("-----print num from 5 to 1-----")
# 2nd parameter=endNum-1

#             startNum>endNum
#             0>0     5-1=4-1=3-1=2-1=1-1=0
for i in range(5,0,-1):
    print(i)           #5 4 3 2 1



print("-----print num from 100 to 20-----")
for i in range(100,19,-1):
    print(i)


print("-----print Even number from 8 to 2-----")
#             0s>1    8-2=6-2=4-2=2-2=0
for i in range(8,1,-2):
    print(i)           #8 6 4 2

print("-----print Even number from 100 to 40-----")
for i in range(100,39,-2):
    print(i)




