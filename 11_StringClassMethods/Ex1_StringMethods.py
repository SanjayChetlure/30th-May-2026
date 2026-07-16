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




