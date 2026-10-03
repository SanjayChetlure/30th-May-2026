
print("----local, class & global variables with same name----")

a,b=10,20     #global variable


class Sample4:

  a,b=30,40      #class variable

  def add(self,a,b):        #local variable
      print(a+b)
      print(self.a+self.b)
      print(globals()['a']+globals()['b'])


s4=Sample4()
s4.add(50,60)


