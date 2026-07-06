print("----Ex4: all types of variables in same example---------")


num1=10        #Global variable

def f1():
    num2=20        #local variable
    print(num2)     #calling local variable
    print(num1)     #calling global variable

def f2():
    num3=30        #local variable
    print(num3)       #calling local variable
    print(num1)       #calling global variable


class Test4:

    num4=40         #class variable

    def m1(self):
        num5=50
        print(num5)          #calling local variable
        print(num1)          #calling global variable
        print(self.num4)     #calling class variable

    @staticmethod
    def m2():
        num6=60
        print(num6)               #calling local variable
        print(num1)               #calling global variable
        print(Test4.num4)         #calling class variable


f1()
print("--")
f2()
print("--")
t4=Test4()
t4.m1()
print("--")
Test4.m2()



