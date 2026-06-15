

PEM=201

#  201>=200
if PEM>=200:          #outer if
    print("selected in prelim exam")
    print("preparing for mains exam")
    MEM=501
    #501>=500
    if MEM>=500:        #nested/inner if
        print("Selected in mains exam")
    else:
        print("rejected in mains exam")
else:
    print("rejected from prelim exam")


print("hi")