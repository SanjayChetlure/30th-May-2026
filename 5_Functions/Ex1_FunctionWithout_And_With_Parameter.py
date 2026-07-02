
print("---------Function without/zero parameter---------")
# Function Syntax

# def functionName():        function declaration
#     functionBody


# function call/run syntax
# functionName()


def f1():
    print("---Function started -----")
    print("Hi")
    print("Hello")
    print("------Function Ended------")

f1()

def add():
    num1=10
    num2=20
    print(num1+num2)

add()


print("---------Function with parameter---------")

#function with 1 int parameter
def findSquareOfNum(num):
    print(num*num)

findSquareOfNum(3)
findSquareOfNum(4)
findSquareOfNum(8)

print("----")

#function with 2 int parameter
def add(num3, num4):      #num3=90, num4=50
    print(num3+num4)     #90+50=140

add(5,6)       #11
add(90,50)     #140
add(6,2)       #8

print("---")

#function with 2 int parameter
def arithmaricOperationDiv(num1, num2):
    print(num1/num2)       #6/2=3

arithmaricOperationDiv(6,2)
arithmaricOperationDiv(2.6,2)


print("-----")

#function 1 String parameter
def printName(name):
    print(name)

printName("Amol")
printName("Mahesh")

print("-----")

#Function with 2 String parameter
def printFullName(FN, LN):
    print("Firstname: ",FN)
    print("lastname: ",LN)

printFullName("ganesh","patil")
printFullName("suresh","patil")


print("-----------")

def studentInfo(sName, sRollNum, sPer, sGrade):
    print("Student Name: ",sName)
    print("Student Roll Num: ",sRollNum)
    print("Student Percentage: ",sPer)
    print("Student Grade: ",sGrade)


studentInfo("Ankita", 101, 65.1, "A+")
studentInfo("Nikita",102,62.3,"A+")




