print("---8: Reverse even/odd index word of statement-----")


inp = "my name is abc"    #-> out: ym name si abc

# Split the statement into words
listObj = inp.split()     # [my   name   is   abc]

# Reverse words at even indices (0, 2, ...)
for i in range(len(listObj)):    #o to 3
    if i % 2 == 1:  # Check if the index is even
        listObj[i] = listObj[i][::-1]

# Join the words back into a statement
out = ' '.join(listObj)
print(out)  # Output: ym name si abc



#
# print("------")
# for i in range(5):
#     print(i)