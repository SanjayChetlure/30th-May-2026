print("----String methods-----")

s1="velocity"
s2="ABCD"
s3="abcd"
s4="my name is abc"

print(len(s1))

print(s4.title())
print(s1.capitalize())      #Velocity


print(s1.upper())      #VELOCITY
# s1=s1.upper()
print(s1)

print(s2.lower())      #abcd
# s2=s2.lower()
print(s2)
print("--------")

s6="Amol"
print(s6.swapcase())

print(s2==s3)                  #compare data & case    - False
print(s2.__eq__(s3))           #compare data & case    -False
print(s2.lower()==s3.lower())  #compare only data -> ignore case
print("---")
print("my" in s4)             #true
print("city" in s1)
print(s4.__contains__("is"))

print(s4.startswith("my"))
print(s4.endswith("abc1"))

print("--------")
s5=" abcd xyz "
print(s5)

print(s5.strip())
print(s5.lstrip())
print(s5.rstrip())

print("------------------------------------")

s1="velocity"
print(s1[2])
print(s1[4:8])                #[startIndex:endIndex+1]

s2="abcaba"
print(s2.find('a'))          # get index of char (1st occurrence)
print(s2.index('a'))         # alternate method for find

print(s2.rfind('a'))         # get index of last occurrence char

print("--------")
print(s1+s2)
s3=s1+s2
print(s3)

print(s2.count('a'))

print("--------------------------------")

s5="my name is abc"
print(s5.replace("abc","AMOL"))         #my name is xyz
print(s1.replace("city","CITY"))


ls=s5.split(" ")           #[my     name        is      abc]
print(ls[2])
print("--")
for i in ls:
    print(i)


print("---------------Additional Methods-----------------------")
str1="abc"
str2="122"
str3="abc123"
str4="  a   "
str5="my name is abc my"
print(str1.isalpha())
print(str2.isdigit())
print(str3.isalnum())
print(str4.isspace())
print(str5.count("my"))









