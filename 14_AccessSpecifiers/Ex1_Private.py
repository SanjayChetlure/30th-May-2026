

class Student:
    __marks = 90

    def display(self):
        print("Marks:", self.__marks)

    def __m1(self):
        print("Private method called")


s = Student()
s.display()
# s.__m1()
# print(s.__marks)  # This will raise an AttributeError because __marks is private
