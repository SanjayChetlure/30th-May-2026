print("----Ex6: Inheritance with Variables-----")

class Demo1:
    num1=10

    def m1(self):
        print("running method m1 from super class")

class Demo2(Demo1):
    num2=20

    def m2(self):
        print("running method m2 from sub class")
        print(self.num1+self.num2)

d2=Demo2()
d2.m1()
d2.m2()
print(d2.num1)
print(d2.num2)


