class Parent:
    _salary = 50000

    def _display(self):
        print("Salary:", self._salary)

class Child(Parent):
    def show(self):
        print("Salary:", self._salary)


c = Child()
c.show()