# Indentation matters in Python! 

thing = 8 

if thing > 10: # indented under the if statement, If = if the condition is true
    print(thing, "is greater than 10")
elif thing < 10: # indented under the elif statement, Else if = if the condition is true, but the previous
    print(thing, "is less than 10")
else: # indented under the else statement, Else = if none of the above conditions are true
    print(thing, "is not greater or less than 10")