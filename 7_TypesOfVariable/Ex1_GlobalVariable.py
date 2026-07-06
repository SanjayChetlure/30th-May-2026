print("----1: Example of Global variable----")

num1=10        #Global variable

def f1():
    print("Running F1: ",num1)                 #VariableName

def f2():
    print("Running F2: ",num1)


class Test1:

    def m1(self):
        print("running instance method m1: ",num1)             #VariableName

    @staticmethod
    def m2():
        print("running static method m2 ",num1)                #VariableName


f1()
f2()
Test1.m2()
t1=Test1()
t1.m1()