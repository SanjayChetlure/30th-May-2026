from operator import truediv

marks=20

#   20>=65
if marks>=65:
    print("Distinction")
elif marks>=60 and marks<65:    # 20>=60 & 63<65
    print("1st class")
elif marks>=50 and marks<60:    #20>=50 and 55<60
    print("2nd class")
elif marks>=35 and marks<50:   #20>=35 and 40<50
    print("pass")
elif marks<35:              #20<35
    print("Fail")


# true & true  -> true
# true & false ->false
# false & true -> false
# false & false -> false