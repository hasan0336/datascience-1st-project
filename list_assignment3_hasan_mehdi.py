# 'Q1'

fruits = list(("apple","banana","orange","grape","kiwi"))
fruits.append("pear")
fruits.insert(1,"mango")
fruits.remove("orange")
print(fruits)

# 'Q2'
numbers = list(range(10))
print(numbers)

print(numbers[3])

print(numbers[2:7])

print(numbers[-3:10])

# "Q3"
squares = [i**2 for i in range(1,11)]

print(squares)


even_squares = [square for square in squares if square %2 == 0]
print(even_squares)


# "Q4"
colors = ["red", "green", "blue", "yellow", "purple"]
colors[0], colors[-1] = colors[-1],colors[0]
print (colors)
colors.reverse()
print(colors)

colors.pop(1)
colors.pop(1)
print(colors)

# "Q5"
letters = ["a","b","c","d","e","f","g","h","i","j"]
print(letters[:5:])

print(letters[-3::])


# "Q6"
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][2])

matrix[1][0] = 0
print(matrix)