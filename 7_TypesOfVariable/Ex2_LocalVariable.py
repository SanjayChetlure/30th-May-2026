print("----2: Example of Local Variable---")

def f1():
    num1=10                 #local variable
    print(num1)

def f2():
    num2=20                 #local variable
    print(num2)
    # print(num1)            #no access

class Test2:

    def m1(self):
        num3=30              #local variable
        print(num3)
        # print(num2)      #no Access

    @staticmethod
    def m2():
        num4=40               #local variable
        print(num4)


f1()
f2()
Test2.m2()

t2=Test2()
t2.m1()


