

print("--12: Duplicate Occurrence, Duplicate & Unique words in statement----")


s = "this is a test this is only a test b"
allWords = s.split()    # [ this   is  a   test   this  is   only   a   test  b ]
dict = {}




for word in allWords:             #this
  if dict.__contains__(word):    #false
      dict[word]=dict.get(word)+1   #1 + 1 = 2
  else:
      dict[word]=1      # this=1


dict[key]=102

      #dict
      # key        Value
    #  this          2
    #   is           2
    #   a           2
    #   test        2
    #   only        1
    #    b          1


print("------Print Occurrence of each word in statement------")
for key in dict:
      print(key, dict.get(key))


print("------Print only duplicate words in statement------")
for key in dict:
  if dict.get(key)>1:
      print(key, dict.get(key))


print("------Print only unique words in statement------")
for k in dict:
  if dict.get(k)==1:
      print(k, dict.get(k))


