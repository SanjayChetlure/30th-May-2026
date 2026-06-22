
# rollNum-int(key):per-float(value)

# key:value
# 1:59.2
# 2:98.5
# 3:90.4
# 5:62.2
# 4:89.1

dictObj1={1:59.2, 2:98.5, 3:90.4, 5:62.2, 4:90.4}
print(dictObj1)

dictObj2={"Mahesh":5, "Ganesh":1, "Suresh":4, "Ramesh":3}
print(dictObj2)

dictObj3={"Mahesh":"B+", "Ganesh":"C+", 1:"A+", 2:"D+"}      #not recommended
print(dictObj3)

print("---get length of dict---")
print(len(dictObj1))     #5

print("---get value of any specific key---")
print(dictObj1[3])          #90.4

print("----Add new key-value pair -----")
dictObj1[6]=68.9
print(dictObj1)

print("----Update value of existing key -----")
dictObj1[2]=99.5
print(dictObj1)

print("----")
print(dictObj2)
dictObj2["Ramesh"]=10
print(dictObj2)


