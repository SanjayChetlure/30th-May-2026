#Module3: Operations1

#Apr1: import moduleName           (import all contents from other module)
       # moduleName.fn()
       # obj=moduleName.className()
       # obj.methodName()

       #moduleName.className.staticMethodName()


import Calculator1
import Calculator2

print("----------------------------Approach1-------------------------------")
print("----call functions & methods from 1st module---")

#call functions
Calculator1.add(2,3)           # moduleName.fn()
Calculator1.mult(6,7)

#call non-static methods
d1=Calculator1.Demo1()                     # obj=moduleName.className()
d1.m1()                                    # obj.methodName()
d1.m2()

#call static method
Calculator1.Demo1.m3()


print("----call functions & methods from 2nd module---")

#function call
Calculator2.div(4,7)
Calculator2.sub(8,5)


#call non-static methods
obj2=Calculator2.Demo2()
obj2.m4()

#call static methods
Calculator2.Demo2.m5()




