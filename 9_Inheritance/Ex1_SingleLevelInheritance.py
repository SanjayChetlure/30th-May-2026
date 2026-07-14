#Parent/super/base class
class Father:
   def car(self):
       print("method car from father class")

   def money(self):
       print("method money from father class")

   def home(self):
       print("method home from father class")

#sub/child class
class Son(Father):
   def bike(self):
       print("Bike: FZ V3 from Son class")

   # def car(self):
   #     print("method car from father class")
   #
   # def money(self):
   #     print("method money from father class")
   #
   # def home(self):
   #     print("method home from father class")



s=Son()
s.bike()
s.car()
s.money()
s.home()

