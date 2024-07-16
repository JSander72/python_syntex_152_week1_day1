## Second data type --> NUMBERS! 

# Integers (whole numbers) 
num1 = 200 # this is a interger 

# Float (decimal numbers)
num2 = 5.89
num3 = 5.00 # this is still a float (because it has a decimal point)

print("num1 data type:", type(num1)) #num1 data type: <class 'int'> "int" = interger
print("num2 data type:", type(num2)) #num2 data type: <class 'float'> "float" = decimal number
print("num3 data type:", type(num3)) #num3 data type: <class 'float'> "float" = decimal number

#typecasting - converting one data type to another data type
new_num_string = str(num1)
print(new_num_string)
print(type(new_num_string)) # new_num_string data type: <class 'str'> "str" = string
# print(num1 + "this is a number") this will throw an error because we can't concatenate an integer and a string



new_thing = str(num2) 
#"str" = string
print(new_thing)
print(type(new_thing)) # new_thing data type: <class'str'> "str"

print("="*50) # just making a line in terminal printing "=" 50 times to make it look nicer

user_input = input("Enter a number here: ")
#input funtion will always return a string
print(user_input)
print(type(user_input)) # user_input data type: <class'str'> "str"

# print(user_input + 25) this will throw an error because we can't concatenate an integer and a string
print(int(user_input) + 25) # convert the string input to an integer and then add 25

user_input = int(input("Enter a number here: ")) # convert the string input to an integer
# "int" = interger

print("="*50) # just making a line in terminal printing "=" 50 times to make it look nicer

# must comment out user_input above in order for it to "run" correctly below (fyi)

# Addition +
add_this = 10 + 25 
print(add_this) 

# Subtraction -
subtract_this = 50 - 30
print(subtract_this)

# Multiplication *
multiply_this = 10 * 100
print(multiply_this) 

# Division /
divide_this = 100 / 3
print(divide_this)

# Modulus %
remainder = 100 % 3
print(remainder)

num1 = 50
is_even = num1 % 2
print(is_even) # True if the remainder is 0, False otherwise

is_odd = 7 % 2
print(is_odd) # True if the remainder is 1, False otherwise

# Exponentiation **
power_this = 10 ** 2
print(power_this) # 100

# PEMDAS/BODMAS rules apply here, Brackets, Orders, Division and Multiplication (order of operation)
ex = (5 + 5) ** (2 + 2) - (3 / 4)
print(ex) 

ex2 = 5 + 5 ** (2 + 2) - (3 / 4)
print(ex2) 