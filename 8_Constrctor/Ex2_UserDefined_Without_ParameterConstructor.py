print("-----user defined without constructor------")

class Demo2:

    # user defined without constructor -> provided user/programmer
    # use1: copy all the members of class into object
    def __init__(self):
        print('running user defined without parameter constructor')

    def m1(self):
        print("running method m1")

    def m2(self):
        print("running method m2")


d2=Demo2()       #calling user defined without parameter constructor
d2.m1()
d2.m2()