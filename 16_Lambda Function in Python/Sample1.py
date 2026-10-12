
# def add(a,b):
#     return a+b

# name=lambda inputs: operation


print("---Ex1: add of 2 num using lambda function--")
add=lambda a,b: a+b

print(add(5,6))

print("---Ex2: Square of num using lambda function--")
squre=lambda num: num*num

print(squre(10))

print("---Ex3: Even or Odd using lambda function--")
check = lambda num: "Even" if num % 2 == 0 else "Odd"

print(check(7))

print("---Ex4: Using lambda function with map()--")
listObj = [1, 2, 3, 4]

result = list(map(lambda x: x*2, listObj))

print(result)


print("---Ex5: Using lambda function with filter()--")
# filter() is used to select items based on a condition.

listObj= [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, listObj))

print(result)




