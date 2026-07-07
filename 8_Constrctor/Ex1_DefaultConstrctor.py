print("-----Example of default constructor-------")

class Demo1:

   #default constructor
   # use1: copy all the members of class into object

   # def __init__(self):
   #     constructor body

   def m1(self):
       print("running non-static method m1")


d1=Demo1()         #constructor call
d1.m1()

#1: d1 -> objectName -> to identify/refer object
#2: Demo1() -> className() -> Constructor call -> copy all the non-static members class into object


print("-----Example of default constructor with static method-------")

class Demo2:

    @staticmethod
    def m2():
        print("running static method")

Demo2.m2()
