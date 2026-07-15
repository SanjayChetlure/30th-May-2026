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

f=Father()
f.car()
f.money()
f.home()


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

print("------Ex3: Method override with super()--------")

class A:
   def m1(self):
       print("method m1 from parent class")

class B(A):
   def m1(self):           #method override
       super().m1()                             #call existing definition/implementation
       print("method m1 from child class")      #call new  definition/implementation

b=B()
b.m1()

print("--------EX4: Variable override--------")
print("-Ex4.1: print only override child class variable-")

class parent:
   name="amol"

class child(parent):
   name="AMOL"       #variable override/re-initialize

c=child()
print(c.name)

print("--Ex4.2: print both parent & child class variable--")

class parent1:
   name="amol"

class child1(parent1):
   name="AMOL"

   def test(self):
       print(self.name)           #call current class variable
       print(super().name)        #call super class variable

c=child1()
c.test()





