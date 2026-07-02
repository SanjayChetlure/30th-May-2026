day="abc"

match day:
    case "mon":
        print("day 1")
    case "tue":
        print("day 2")
    case "wed":
        print("day 3")
    case "thr":
        print("day 4")
    case "fri":
        print("day 5")
    case "sat":
        print("day 6")
    case "sun":
        print("day 7")
    case _:
        print("Invalid Input")
