# module4: Operations2

print("----------Approach2--------------")

# syntax:
# Apr2:   from moduleName import functionName, className      (import specific/required contents from other module)
#                 functionName()        -> calling function
#                 obj=className()     -> creatingObject
#                  obj.methodName()      -> calling non-static method

                  # className.methodName()     -> static Method

          # from moduleName import *             import all contents


from Calculator1 import add, Demo1
from Calculator2 import sub,Demo2

print("-------calling content from Module1--------")

#call functions
add(10,20)


#create object
d1=Demo1()
d1.m1()
d1.m2()

#call static method
Demo1.m3()



print("-------calling content from Module2--------")

#call function
sub(4,9)

#create object
d2=Demo2()
d2.m4()

#call static method
Demo2.m5()
