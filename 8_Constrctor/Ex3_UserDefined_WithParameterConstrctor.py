print("----Ex3: User defined with parameter constructor----")

class Demo3:

    #user defined with 2 parameter constructor
    #use2: initialize class variable
    def __init__(self,a,b):     #a=10, b=20 #local variable
        self.num1=a        #10     #assign local variable info into class variable
        self.num2=b        #20

    def add(self):
        print(self.num1+self.num2)    #10+20

    def mult(self):
        print(self.num1*self.num2)

    def sub(self):
        print(self.num1-self.num2)


d1=Demo3(10,20)
d1.add()      #30
d1.mult()     #200
d1.sub()      #-10
print("-----")

d2=Demo3(50,60)
d1.add()
d1.mult()
d1.sub()
print("-----")

d3=Demo3(2,3)
d3.add()
d3.mult()
d3.sub()



print("-------------------Example without user defined with parameter Constructor------------------")



class Demo4:

    num1=5        #class variable
    num2=6

    def add(self):
        print(self.num1+self.num2)    #30+18=48

    def mult(self):
        print(self.num1*self.num2)

    def sub(self):
        print(self.num1-self.num2)

d4=Demo4()
d4.add()
d4.mult()
d4.sub()
print("---------------")
d5=Demo4()
d5.add()
d5.mult()
d5.sub()