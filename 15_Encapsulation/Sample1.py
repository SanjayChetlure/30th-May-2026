
class Demo2:
    __num1=10
    __num2=20
    __num3=30

    def add(self):
        print(self.__num1+self.__num2+self.__num3)

    def mult(self):
        print(self.__num2 * self.__num3)

    def squareOfNum(self):
        print(self.__num1 * self.__num1)

d2=Demo2()
d2.add()
d2.mult()
d2.squareOfNum()
