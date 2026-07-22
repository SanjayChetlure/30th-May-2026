print("----Program without exception handling-----")

# num1=10
# num2=0
# num3=num1/num2    #10/0
# print(num3)
# print("Hi")
# print("Hello")

print("------Ex1.1: basic example of Exception handling-----")

n1=10
n2=0
try:
    n3=n1/n2               #risky code
    print(n3)
except ZeroDivisionError:
    print("ZeroDivisionError handled")              #msg in except block
print("Hi")
print("Hello")

print("-----1.2: Alternate code in except block------")
n1=10
n2=0

try:
  print(n1/n2)          #risky code
except ZeroDivisionError:
  print(n1/1)          #only alternate solution

print("Hi Hello")


print("-----1.3: Alternate code & msg in except block------")
n1=10
n2=0

try:
  print(n1/n2)          #risky code
except ZeroDivisionError:
  print(n1/1)                            #alternate solution
  print("ZeroDivision Error Handled")    #msg

print("Hi Hello")


print("------2: Example of Multiple Except block------")
n1=10
n2=0

try:
  print(n1/n2)
except ValueError:
  print("ValueError Handled")
except ZeroDivisionError:
  print("ZeroDivisionError Handled")

print("program ended")


print("-----------3.1: Example of Generic exception-----------")
n1=10
n2=0

try:
  print(n1/n2)          #risky code
except Exception:
  print("Generic exception handled")

print("program ended")


print("-----------3.2: Example of Generic exception-----------")
n1=10
n2=0

try:
    print(n1/n2)          #risky code
except Exception as s1:
    print(s1)
    print("Generic exception handled")

print("program ended")


print("-----4: Example of Correct way of using Generic exception-------")
n1=10
n2=0

print("program started")
try:
    print(n1/n2)
except ValueError:
    print("Value Error Handled")
except ZeroDivisionError:
    print("ZeroDivisionError handled")
except Exception as e:
    print("Generic Exception handled")
    print(e)

print("program ended")


print("--------5: Alternative way of using Generic exception-------------")
n1=10
n2=0

try:
    print(n1/n2)
except:
    print("Generic Exception Handled")

print("Hi Hello")














