print("------Ex13: Occurrence, Duplicate & Unique chars in string------")

name = "abcdab"
dict= {}


for char in name:
   if dict.__contains__(char):
       dict[char]=dict.get(char)+1
   else:
       dict[char]=1


    #   k     V
   #    a     2
   #    b     2
   #    c     1
   #    d     1


print("------Print Occurrence of each char in string------")
for k in dict:
       print(k, dict.get(k))


print("------Print only duplicate char in string------")
for k in dict:
   if dict.get(k)>1:
       print(k, dict.get(k))


print("------Print only unique char in string------")
for k in dict:
   if dict.get(k)==1:
       print(k, dict.get(k))

