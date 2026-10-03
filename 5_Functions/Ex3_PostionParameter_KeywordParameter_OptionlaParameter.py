
print("----------Example of Positional parameter------------")

def greet(name, age):
   print("My name is",name, "& age is",age)


# Calling the function with positional arguments
greet("ganesh",15)  # Correct order
greet("suresh", 22)  # Correct order
greet(20, "ramesh")  # Incorrect order, meaning changes



print("----------Example of Keyword parameter------------")

def greet(name, age):
   print("My name is",name, "& age is",age)

# Calling the function with keyword parameter
greet(name="Amol",age=15)
greet(age=20,name="suresh")


print("-------Example of Optional/default parameter:--------")

def studentInfo(name, age=10):
   print(name,": ",age)

studentInfo(name="rahul")
studentInfo(name="pooja", age=25)


print("------")


def studentDetails(name="abc", age=10):
   print(name,": ",age)

studentDetails()
studentDetails(name="ganesh")
studentDetails(name="suresh",age=15)
