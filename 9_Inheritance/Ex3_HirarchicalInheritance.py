#Super class
class Father:
   def car(self):
       print("method car from father class")

   def money(self):
       print("method money from father class")

   def home(self):
       print("method home from father class")

#sub class 1
class Son1(Father):
   def bike(self):
       print("Bike: FZ V3 from Son1 class")

   # def car(self):
   #     print("method car from father class")
   #
   # def money(self):
   #     print("method money from father class")
   #
   # def home(self):
   #     print("method home from father class")

#sub class 2
class Son2(Father):
   def laptop(self):
       print("HP Laptop from Son2 class")

   # def car(self):
   #     print("method car from father class")
   #
   # def money(self):
   #     print("method money from father class")
   #
   # def home(self):
   #     print("method home from father class")


print("------Features of Son1 class-------")
s1=Son1()
s1.bike()
s1.car()
s1.money()
s1.home()

print("------Features of Son2 class-------")
s2=Son2()
s2.laptop()
s2.car()
s2.money()
s2.home()