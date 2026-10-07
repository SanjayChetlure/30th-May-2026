
print("------Ex4: Reverse String------")

 # Apr1:
org = "hello"
rev=org[::-1]
print(rev)


# Apr2:
orgString = "abcd"
revString=""  #dcba

for singleChar in orgString:
  revString=singleChar+revString     #a+""=a. =b+a=ba, c+ba=cba, d+cba=dcba
print(rev)
