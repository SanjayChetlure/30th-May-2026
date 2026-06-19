
st={102, "Mahesh", 66.5, "Maths", "A+",102}
print(st)


#get size of set object
print(len(st))

# print(st[0])   Invalid statement

print("---Add New Single Element---")
st.add("ganesh")
print(st)


print("---Add New multiple Elements---")
st.update([75.2, "B+"])
print(st)


print("------Remove Element-----")
st.remove("B+")    #Remove Specific Element -> Through error even if element does not exist
print(st)

st.discard(103)      # No error even if element does not exist
print(st)

st.pop()    #remove random element
print(st)


print("----copying set object-----")
st1=st.copy()
print(st1)


print("----Sorting Set---")
st2={40,50,10,40,30}   #{40,50,10,30}
print("-----before sorting set object---")
print(st2)
lstObj=sorted(st2)    #[10, 20, 30, 40, 50]  sorted data stored into list object
print(lstObj)


print("------Check element present or not-----")
# count & index fn are not present in set object
print(10 in st2)


print("----clear set object")
st.clear()
print(len(st))


print("----delete set object")
del st
# print(st)       NameError: name 'st' is not defined


