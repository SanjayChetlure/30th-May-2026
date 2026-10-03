#packageName: T13_package2
#moduleName: Test3

#from packageName import moduleName
        # moduleName.fn()                       -> calling function
        # obj=moduleName.className()             -> create object
        # obj.methodName()                      ->non-static method calling
        # moduleName.className.methodName()     -> static method calling


from T13_Package1 import Test1

#call function
Test1.f1()
Test1.f2()

#create object
obj1=Test1.Demo1()

#call non-static method
obj1.m1()

#static method calling
Test1.Demo1.m2()