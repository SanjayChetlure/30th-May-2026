
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

print("-----Remove any specific key-value pair------")
print(dictObj1)
dictObj1.pop(2)
print(dictObj1)

print("-----Remove last inserted k-v pair------")
dictObj1.popitem()
print(dictObj1)

print("-----check if any specific key available in dict object------")
print(1 in dictObj1)          #True
print(8 in dictObj1)          #False

print("------get all keys------")
allKeys=dictObj1.keys()
for singleKey in allKeys:
    print(singleKey)

print("----")

for singleKey in dictObj1.keys():
    print(singleKey)


print("-----get all values----")
allValues=dictObj1.values()
for singleValue in allValues:
    print(singleValue)

print("------")
for singleValue in dictObj1.values():
    print(singleValue)


print("-----get all keys-values----")
allItems=dictObj1.items()
for key,value in allItems:
    print(key,"-",value)

print("--")

for k, v in dictObj1.items():
    print(k, "=", v)

print("----")

allKeys=dictObj1.keys()
for singleKey in allKeys:
    print(singleKey,"-",dictObj1[singleKey])


print("---clear dict object----")
dictObj1.clear()
print(dictObj1)


print("----delete dict object---")
del dictObj1
print(dictObj1)



