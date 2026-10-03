
class Demo3:

    #instance method
    def m1(self):
        print("running without parameter method")

    # instance method
    def m2(self,n1,n2):
        n3=n1+n2
        print("running with parameter method-",n3)

    # instance method
    def m3(self,n1):
        n2=n1*n1
        print("running with return type method")
        return n2

    @staticmethod
    def m4():
        print("running without parameter static method ")

    @staticmethod
    def m5(n1,n2):
        n3=n1-n2
        print("running with parameter static method ",n3)

    @staticmethod
    def m6(n1):
        n2=n1*n1*n1
        print("running with return type static method ")
        return n2

print("---Calling instance method---")
d3=Demo3()
d3.m1()
d3.m2(2,9)
n4=d3.m3(9)
print(n4)

print("------Calling static method-------")
Demo3.m4()
Demo3.m5(5,7)
n5=Demo3.m6(4)
print(n5)