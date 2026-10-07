print("------Ex6: Reverse Statement------")


inp = "my name is abc"   # Exp output ->  abc is name my
print(inp)

#1: spint statement into list of words
l1=inp.split()     #[my name is abc]

#2: reverse the list of words
l1.reverse()      # l1=l1[::-1]     ->  [abc is name my]
# print(l1)

#3: join the list of words into statement/String
out=' '.join(l1)     #  abc is name my
print(out)
