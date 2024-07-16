# Week 1 day 1 lecture 
#This is a comment

# Our first line of code
print('hello world!')

# Using a # allow you to wrigte a comment in your code that will not run. Python and CS Code will ignore it


# This is a veriable with a string stored in it
# A string is a data type used for storing text 
first_words = "Hello World!"

print(first_words)

# Here is a string with single quotes. It is still a string data type
new_string = 'I can also use single quotes'

# Escaped character \ allows us to still use single quotes instide of a single quote string
example = 'I  can\'t use single quote\'s insside single qoute\'s' 
print(example)

# Concatenating string together - combine multiple strings together
string1 ="this is"
string2 = "super cool"

# Concatenated multiple strings together and stored them in a new variable
concat = string1 + string2 
print(concat)

# Concatenated two strings together using a + sign
print(string1 + string2) 

# Concatenated two strings together using a space in between
print(string1 + " " + string2)

print(string1, string2)  # Concatenated with a coma, will automatically add a space between the strings

# Docstring = a multi-line string 

### incorrect format for a doc string
# another_string = "
# line1
# line2
# line3
# "

### Correct format for a doc string
# initiate a docstring with triple quotes,either singe '''or double quotes """
doc = """
Enter 1 to continue 
Enter 2 to go back 
Enter 3 to figure it all out
""" 
print(doc)

# Python reads code from the top to the bottom, we've defined the varible doc, if wer redefined the data stored there, then our print function will cprint that new piece of data

doc = "This is a new thing"

print(doc)


# Unpacking - We can define multiple pieces of data at once, and unpack them positionally into their own variable (places in memory)
first, middle, last = "James", "Earl", "Sanders"
print(middle)

print(first, middle, last)

# This will throw an error because we redefined the built-in print function
#  Never create a verable wiht a reserved word

# print = "something here"
# print(print)

# Global and If are both reserved words in Python



