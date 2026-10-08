
print("----7: Reverse 1st & last word of statement----")

inp = "my name is abc"    #-> out: ym name is cba

# Split the statement into words
listObj = inp.split()        #[my    name    is    abc]


# Reverse the first and last words
listObj[0] = listObj[0][::-1]      #reinitialization
listObj[-1] = listObj[-1][::-1]


# Join the words back into a statement
out = ' '.join(listObj)
print(out)  # Output: ym name is cba
