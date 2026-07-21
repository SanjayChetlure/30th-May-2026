print("----Program without exception handling-----")

# num1=10
# num2=0
# num3=num1/num2    #10/0
# print(num3)
# print("Hi")
# print("Hello")

print("------Ex1: basic example of Exception handling-----")

n1=10
n2=0
try:
    n3=n1/n2               #risky code
    print(n3)
except ZeroDivisionError as e:
    print("ZeroDivisionError handled")
print("Hi")
print("Hello")

