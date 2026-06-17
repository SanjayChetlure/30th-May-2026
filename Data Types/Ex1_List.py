num=10
print(type(num))


studentData=["Amol", 101, 75.1,"A+", 101]

#display data
print(studentData)

#print type of object
print(type(studentData))

#print length/size of list
print(len(studentData))

#get specific data from list object
print(studentData[4])

# Note: in case of wrong index:- IndexError: list index out of range

#Add new data in list object
#append/extend/
# 1: append- Add new element/data at last position
studentData.append("xyz")
print(studentData)

#2: extend - add multiple new elements at the end of list object
studentData.extend([50,10,"abc",88.1])
print(studentData)

# 3: add new element at specific position/index in list object (right shift operation)
studentData.insert(4,500)
print(studentData)


#remove data from list
#pop()/pop(index)/remove(object/element)

#1: pop() :-  remove data from last position
studentData.pop()
print(studentData)

#2: pop(index) :- remove data from specific index  -> left shift operation
studentData.pop(3)
print(studentData)

#3: remove(element/object) :- remove specific element from list
studentData.remove(101)
print(studentData)


#copy list object
newStudentData=studentData.copy()
print(newStudentData)


print("-----Print all data from List Object -----")
#              8<8
for i in range(0,8):
    print(studentData[i])

print("----")

for i in range(0,len(studentData)):
    print(studentData[i])

print("----")

for singleData in studentData:
    print(singleData)