
#Ex1: Instance/non-static method

class Demo1:

    #Without parameter method
    def m1(self):
        print("running without parameter method m1")

    #Method with parameter
    def squareOfNum(self,num):
        print("running with parameter method")
        print(num * num)

#To Call/Run Instance method
# 1: Create object/instance of class
# 2: method call

# Syntax of object creation
# objName=className()

#Syntax of method call
# objName.methodName()

d1=Demo1()           #Object Creation
d1.m1()              #Method calling
d1.squareOfNum(5)

#Para1: d1  -> object name -> to refer/identify object
#Para2: Demo1() -> className() -> Constructor -> copy all the members of class into object

print("-----------------")


class ArithMaticOperation:

    def add(self,n1,n2):
        print(n1+n2)

    def mult(self,n1,n2):
        print(n1*n2)

    def sub(self,n1,n2):
        print(n1-n2)

    def div(self,n1,n2):
        print(n1/n2)

obj1=ArithMaticOperation()
obj1.add(10,20)
obj1.mult(10,20)
obj1.sub(10,20)
obj1.div(10,20)
obj1.div(4,5)

print("--Create n objects of same class")

obj2=ArithMaticOperation()
obj2.add(4,9)
obj2.sub(55,22)





