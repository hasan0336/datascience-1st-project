import re
first_name = "hasan"
last_name = "mehdi"
age = 31

print(f"{first_name} {last_name} {age}")

a = 2
b = 9

a = a - b
b = b + a
a = b - a
print(a,b)


print(type(5.5))

flo = 45.67
print(int(flo))

length = 10
width = 5

area = length * width
print(area)

remainder = 100%7
print(remainder)

check = 150

if(check > 10 and check < 20):
    print(check)
else:
    print(11111)


number = -5

if(number > -10 or number < 20):
    print(number)
else:
    print(33333)

text =  "Learning Python is fun!"
print(text[9:15])
print(text[-14:-8])
print("".join(text.split()[1]))

text2 = "Hello World!"
#-1 mean we are iterating it in reverse order
print(text2[::-1])

text3 = 'abcdefghijklmnopqrstuvwxyz'
print(text3[::2])

text4 = "PythonProgramming"
print(text4[::-3])


square = [square**2 for square in range(1,11) ]
print(square)

nums = [1,2,3,4,5,6,7,8,9,10]

even = [even for even in nums if(even % 2 == 0)]
print(even)

listNums = [1,2,3,4,5,6]
listNums.append(7)
print(listNums)

listTill5 = listNums[:5:].copy()
print(listTill5)

extendList = listNums[0:3]
list456 = [4,5,6]
extendList.extend(list456)
print(extendList)

print(listNums.index(3))

print(listNums)
listNums.pop(len(listNums)-1)
print(listNums)

listNums.remove(3)
print(listNums)

fruits = "apple mango apple"

fruits.replace("banana","apple")
print(fruits.split())
