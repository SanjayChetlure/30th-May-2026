print("-------Ex2: Method Overriding---------")


#super/parent/base class
class Father:
   def car(self):
       print("Car: Tata")

   def money(self):
       print("Money: 1L")

   def home(self):
       print("home: 2BHK")


#sub/child class
class Son(Father):
   def mobile(self):
       print("Mobile: Samsung")

   def car(self):       #method override
       print("Car: Kia")

   def money(self):     #method override
       print("Money: 5L")

   # def home(self):
   #     print("home: 2BHK")

s=Son()
s.mobile()
s.car()
s.money()
s.home()


print("-----Ex2: Method override in multilevel inheritance-----")
class GrandFather:
   def home(self):
       print("1 BHK")

   def money(self):
       print("1 Lakh")


class Father(GrandFather):
   def home(self):        # method override
       print("2 BHK")

   def money(self):       # method override
       print("2 Lakh")


class Son(Father):
   def home(self):        # method override
       print("3 BHK")

   def money(self):        # method override
       print("3 Lakh")


s=Son()
s.home()
s.money()


