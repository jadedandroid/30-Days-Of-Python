import math
# 💻 Exercises - Day 2
# Exercises: Level 1
# Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
# Write a python comment saying 'Day 2: 30 Days of python programming'
# Declare a first name variable and assign a value to it
first_name = "Chenyun"
# Declare a last name variable and assign a value to it
last_name = "Zhang"
# Declare a full name variable and assign a value to it
full_name = "ChenyunZhang"
# Declare a country variable and assign a value to it
country = "US"
# Declare a city variable and assign a value to it
city = "Brooklyn"
# Declare an age variable and assign a value to it
age = 200
# Declare a year variable and assign a value to it
year = 2021
# Declare a variable is_married and assign a value to it
is_married = False
# Declare a variable is_true and assign a value to it
is_true = True
# Declare a variable is_light_on and assign a value to it
is_light_on = False
# Declare multiple variable on one line
x,y,z = 1,2,3

# Exercises: Level 2
# Check the data type of all your variables using type() built-in function
print("type of first_name",type(first_name))
print("type of last_name",type(last_name))
print("type of full_name",type(full_name))
print("type of country",type(country))
print("type of city",type(city))
print("type of age",type(age))
print("type of year",type(year))
print("type of is_married",type(is_married))
print("type of is_true",type(is_true))
print("type of x",type(x))
print("type of y",type(y))
print("type of z",type(z))

# Using the len() built-in function find the length of your first name
print("length of my first name is:",len(first_name))

# Compare the length of your first name and your last name
print("the difference of the length of my first and last name:",abs(len(last_name)-len(first_name)))

# Declare 5 as num_one and 4 as num_two
num_one,num_two = 5,4

# Add num_one and num_two and assign the value to a variable _total
_total = num_one+num_two
print("_total:", _total)

# Subtract num_two from num_one and assign the value to a variable _diff
_diff = num_two - num_one
print("_diff:",_diff)

# Multiply num_two and num_one and assign the value to a variable _product
_product = num_two * num_one
print("_product:",_product)

# Divide num_one by num_two and assign the value to a variable _division
_division = num_one / num_two 
print("_division:",_division)

# Use modulus division to find num_two divided by num_one and assign the value to a variable _remainder
_remainder = num_one%num_two
print("_remainder:",_remainder)

# Calculate num_one to the power of num_two and assign the value to a variable _exp
_exp = num_one ** num_two
print("_exp:",_exp)

# Find floor division of num_one by num_two and assign the value to a variable _floor_division
_floor_division = (num_one//num_two)
print("_floor_division:",_floor_division)

# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable area_of_circle
radius = 30
area_of_circle = radius **2 * math.pi
print("area_of_circle:",round(area_of_circle,2))

# Calculate the circumference of a circle and assign the value to a variable circum_of_circle
circum_of_circle = radius * 2 * math.pi
print("circum_of_circle:",round(circum_of_circle,2))

# Take radius as user input and calculate the area.
# radius = input("enter the radius for the circle: ")
# area_of_circle = int(radius) **2 * math.pi
# print("area_of_circle:",round(area_of_circle,2))

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
# first_name = input("What's your first name: ")
# last_name = input("What's your last name: ")
# age = input("What's your age: ")
# country = input("What country are you from: ")
# print("Your name is "+first_name+" "+last_name+"."+"\n"+"You are "+age+" year-old."+"\n"+"You are from "+country)

# Run help('keywords') in python shell or in your file to check for the reserved words
help('keywords')

