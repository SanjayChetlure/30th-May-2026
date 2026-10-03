print("------------# Ex3.2: Constructor With Parameter---------")


class Employee:

   empCompanyName="abc"

   def __init__(self,name,id,salary):         #with 4 para constructor
       self.empName=name          #assign local variable info into class variable
       self.empID=id
       self.empSal=salary


   def empInfo(self):
       print(self.empName)
       print(self.empID)
       print(self.empSal)
       print(self.empCompanyName)


e1=Employee("Amol",101,50000.1)
e1.empInfo()

print("--")
e2=Employee("Rahul",102,682682.1)
e2.empInfo()

print("--")
e3=Employee("Heena",103,78000)
e3.empInfo()


