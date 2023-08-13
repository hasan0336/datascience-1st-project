import datetime

name="Hasan Mehdi"
age=31
country="Pakistan"
print("My name is {}, I am {} year's old, and I live in {}".format(name,age,country))

item="laptop"
price=25.5
quantity=100
total_cost=price*quantity
print("I bought {} {} at a {} each, for a total cost of {}.".format(quantity,item,price,total_cost))

city="Karachi"
temperature="36"
print(f"the temperature in {city} is {temperature} C")


first_name = "Hasan"
last_name = "Mehdi"
birth_year = 1992
age = datetime.datetime.now().year - birth_year

print("My name is %s %s. I am %d years old" % (first_name, last_name, age))

product = "mobile"
discount = 10
original_price = 200
discount_price = original_price * (1 - discount / 100)
print(f"the discounted price for {product} is {discount_price}rs")