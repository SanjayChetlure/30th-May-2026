
print("----3: Example of class variable----")

class Test3:

    num1=10     #class variable

    def m1(self):
        print(self.num1*self.num1)       #self(CurrentClassObjName).classVariableName

    @staticmethod
    def m2():
        print(Test3.num1)                #ClassName.classVariableName

t3=Test3()
t3.m1()      #10*10=100
print(t3.num1)
