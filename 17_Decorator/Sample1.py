def deco1(f1):
    def m2():
        print("Before function")
        f1()
        print("After function")
    return m2


@deco1
def m1():
    print("HI....")


m1()