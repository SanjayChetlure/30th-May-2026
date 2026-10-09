# Pattern1:

# ****
# ****
# ****

for i in range(3):  #1: create outer for loop for rows
    for j in range(4):  #2: create inner for loop for columns
        print("*", end="")  #3: print * without line break
    print()  #4: empty print() stat to move to the next line after each row

print("--------Pattern2")
#*****
#*****
#*****
#*****

for i in range(4):
    for j in range(5):
        print("*", end="")
    print()

print("--------Pattern3-------")

#*
#**
#***

star = 1
for i in range(3):
    for j in range(star):
        print("*", end="")
    print()
    star = star + 1

print("--------Pattern4-------")

#*
#***
#*****
#*******

star = 1
for i in range(4):
    for j in range(star):
        print("*", end="")
    print()
    star = star + 2

print("-----Pattern5----")
#***
#**
#*

star = 3
for i in range(3):
    for j in range(star):
        print("*", end="")
    star -= 1
    print()


print("-----Pattern6:---")
#*****
#***
#*

star=5
for i in range(3):
  for j in range(star):
      print("*",end="")
  star -=2
  print()
