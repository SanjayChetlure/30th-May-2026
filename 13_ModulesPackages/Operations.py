#ModuleName1: Operations

#Apr1: import moduleName
       # moduleName.fn()
       # obj=moduleName.className()
       # obj.methodName()

       #moduleName.className.staticMethodName()


import Calculator
import Calculator2


print("----call functions & methods from 2nd module---")

#call functions
Calculator.add(2,3)           # moduleName.fn()
Calculator.mult(6,7)

#call non-static methods
d1=Calculator.Demo1()                     # obj=moduleName.className()
d1.m1()                                    # obj.methodName()
d1.m2()

#call static method
Calculator.Demo1.m3()


print("----call functions & methods from 3rd module---")

#function call
Calculator2.div(4,7)
Calculator2.sub(8,5)


#call non-static methods
obj2=Calculator2.Demo2()
obj2.m4()

#call static methods
Calculator2.Demo2.m5()
