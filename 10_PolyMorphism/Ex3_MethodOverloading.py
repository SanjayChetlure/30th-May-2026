
# print("------Ex1: Method Overloading----")

# class Sample1:
#     def add(self, num1, num2):
#         print(num1+num2)
#
#     def add(self,num1, num2, num3):
#         print(num1+num2+num3)
#
#
# s1=Sample1()
# s1.add(2, 3)
# s1.add(2,3,5)


print("------Ex1: Method Overloading----")

class Sample1:

    def add(self, num1=0, num2=0, num3=0, num4=0, num5=0):
        print(num1+num2+num3+num4+num5)

s1=Sample1()
s1.add()
s1.add(10,20)
s1.add(10,20,30)
s1.add(10,20,30,40)
s1.add(10,20,30,40,50)


print("------Ex2: Method Overloading----")

class Sample2:

   def printName(self,name="xyz"):
       print(name)

s=Sample2()
s.printName()
s.printName("Mahesh")
