from urllib3 import proxy_from_url

print("-----Function With Return Type------")

def add(num1, num2):
    num3=num1+num2
    return num3

#Apr1
num4=add(2,3)
print(num4*num4)

print("--")

#Apr2
print(add(4,5))

print("----------------------")

def sub(num1, num2):
    subValue=num1-num2
    return subValue

#Apr1
num3=sub(9,6)
print(num3*num3*num3)

print("--")

print(sub(9,6))

print("--------------------------------")

def getRollNum():
    rollNum=101
    return rollNum

#Apr1
n1=getRollNum()
print(n1)

#Apr2
print(getRollNum())

print("----------Function with multiple return type------------")

def mult(num1, num2):
    return num1*num2

def AddMult(num1, num2):
    add=num1+num2
    mult=num1*num2
    return add,mult

n1,n2=AddMult(7,8)
print(n1)
print(n2)


n3=mult(n1,n2)
print(n3)





