#Super class 1
class A:
   def m1(self):
       print("Method m1 from A class")

#super class 2
class B:
   def m2(self):
       print("Method m2 from B class")

#subc class
class C(A,B):
   def m3(self):
       print("Method m3 from C class")

   # def m1(self):
   #     print("Method m1 from A class")
   #
   # def m2(self):
   #     print("Method m2 from B class")



print("------Features of class C-----")
c=C()
c.m1()
c.m2()
c.m3()
