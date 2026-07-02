
UN="abc"
PWD="xyz"


# abc==abc1
if UN=="abc":              #outer if
    print("Correct UN entered")
    print("Enter PWD")
    #  xyz==xyz1
    if PWD=="xyz1":          #inner/nested if
        print("correct pwd entered")
        print("home page visible")
    else:
        print("wrong pwd entered")
else:
    print("Wrong UN entered")