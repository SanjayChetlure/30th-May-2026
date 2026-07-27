
from T13_Package1 import Test1,Test2

#call fn
Test1.f1()
Test1.f2()
Test2.f3()
Test2.f4()


#create objet
d1=Test1.Demo1()
d2=Test2.Demo2()

#call non-static methods
d1.m1()
d2.m3()

#call static methods
Test1.Demo1.m2()
Test2.Demo2.m4()