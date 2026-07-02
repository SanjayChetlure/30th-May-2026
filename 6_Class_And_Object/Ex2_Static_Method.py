
#2: Example od Static methods call

class Demo2:

    @staticmethod
    def m1():
        print("running static without parameter method")

    @staticmethod
    def divArithmaticOperation(num1,num2):
        print(num1/num2)
        print("running static method with parameter")

    @staticmethod
    def AddArithmaticOperation(num1, num2):
        print("running static method with return type")
        return num1+num2


#To call static method
# className.methodName()

Demo2.m1()
Demo2.divArithmaticOperation(30,5)
num3=Demo2.AddArithmaticOperation(7,9)
print(num3)
print("--")
print(Demo2.AddArithmaticOperation(7,9))


