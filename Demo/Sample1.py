
class Demo1:
    def __init__(self, n1, n2):
        self.n1=n1
        self.n2=n2

    def m1(self):
        print(self.n2+self.n2)


class Demo2(Demo1):
    def __init__(self,n3,n4,str):
            super().__init__(n3,n4)
            self.str=str

    def m2(self):
        print(self.str)

d2=Demo2(10,20,"Amol")
d2.m1()
d2.m2()

