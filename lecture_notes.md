# python_syntex_152_week1_day1

## Introduction

- Ice breaker
    - Name, something about yourself, and what has brought you here to this point, what inspired you to start a bootcamp?

- Rundown of how class will go every day
    - Start with lecture objectives general overview of the day
    - Go over Notion, what they need to know
        - Where to find information: Class Slides/Material, GitHub links, Class recordings
    - Openclass
        - correct link
        - homework breakdown -> Quizes and "Assignments"
        - I will always upload our lectures and class material to github and share the link
    - Slack
        - Pinned messages, bookmarked links
        - Keep an eye out for resources, I'll continue to add them as we progress through the course
    - homework and latenes
    - Just me, so don't be afraid to raise your hand and ask a question, hard to check the chat during lecture. No such thing as a dumb or stupid question!
    - Cameras! Allow me to read the room
    - Breaks! I'll try to incorporate breaks during lecture, but if you all ever feel like you need a break or if I forget, please let me know!
        - If I'm ever going too fast, or if you need more clarification, just let me know!
---

## Lecture Material <3

- ### VS Code Setup for class
    - File Structure
        - Set up coding_temple > backend > week1 > day1
    - Auto-save on!
    - Opening to a folder
        - Generally don't want to open to just one file
    - Using command line to open VS Code?
    - Maybe run through some extensions, just to make sure
        - Name: autopep8
            Description: Formatting support for Python files using the autopep8 formatter.
            https://marketplace.visualstudio.com/items?itemName=ms-python.autopep8
        - Name: Live Share
            Description: Real-time collaborative development from the comfort of your favorite tools.
            https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare
        - Name: Path Intellisense
            Description: Visual Studio Code plugin that autocompletes filenames
            https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense
        - Name: Pylance

            Description: A performant, feature-rich language server for Python in VS Code
            https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance
        - Name: Python
            Id: ms-python.python
            Description: Python language support with extension access points for IntelliSense (Pylance), Debugging (Python Debugger), linting, formatting, refactoring, unit tests, and more.
            https://marketplace.visualstudio.com/items?itemName=ms-python.python

- ### Overview of the Python Language
    - High-Level (Can write more meaningful lines of code rather than 11000110)
    - Interpreted (High-level lines are Interpreted via a compiler into machine code)
    - General-Purpose Language (Data Science, Web Development, AI, etc)
    - Dynamic Language (Data types of variables are not predefined, and can change)


- ### Test print "Hellow world!"
    - Create our first Python file
        - Python files end with the `.py` extension
    - First line of code! 

- ### First data type -> Strings
    - Comments! 
        - `# this is a comment in Python`
    - Strings are a **data type used to represent text**
    - Single quote and double quotes
        - Using a mix of the two- ex. single inside of double
        - Always use the opposite quotation inside a string
    - Concatinating strings with commas vs +
        - Commas add a space automatically
    - Docstring/multi-line string -> 3 single quotes
        - user menu as an example use   

- ### Storing and manipulating data with vairables
    - A **variables give us a place to store a piece of data** in memory so that we can access it and use it later.
    - We can re-assign the value of a variable later if we want
        - Python reads code from the top down
    - Multiple assignment
        - `first, middle, last = "Travis", "Cline", "Peck"`
    - Keywords to avoid using as variable names (Python Errors Slides)
    
- ### Python Naming Convention
    - Each coding language has its own naming convention that must be followed
        - Best practices
    - Cannot do something like this -> `number of donuts = 34`
    - `snake_case`
        - always lowercase
        - always underscores between words
        - **Python standard**
    - `camelCase`
        - JavaScript naming convention
        - first word lowercase
        - capitalize the first letter of each word that follows
    - `PascalCase`
        - similar to camelCase, just with the first word capitalized
    - `kebab-case`
        - separates each word with a dash character
    - All caps signifies a variable that will never change
        - `NUM_PI = 3.14`
    - Can't start a variable with a number

- ### Numbers
    - Integers are a data type used to represent whole numeric values
    - Floats are a data type used to represent decimal numbers

- ### Type() Function and Type Casting
    - `type()` returns the datatype of a value
    -  `str()` convert to string
    - `int()` converts to integer
    - `float()` converts to float

<!-- >### In-Class Activity
>
>Have students
> ```python
>this = 'that'
>``` -->


- ### Arithmetic operators
    - Addition `+`
        - `+=`
    - Subtraction `-`
        - `-=`
    - Multiplication `*`
    - Division `/` (always returns a float)
    - Modulo `%` (Returns the remainder of division)
        - great for mathmatical proofing, i.e. checking if a number is even or odd
    - Floor Division `//` Divides and rounds DOWN to the nearest whole number
    - Exponent `**`
    - PEMDAS

- ### Boolean Operators (Comparison Operators)
    - `True` vs `False`
        - `instructor = 'Travis'`
        - `print(bool(1))`
        - `print(bool(0))`
    - Equal to `==`
        - `print(instructor == 'Travis')`
    - Less than`<`
    - Greater than `>`
    - Not equal to `!=`
        - `location = "North America"`
        - `if location != "North America":`
    - Less than or equal to `<=`
    - Greater than or equal to `>=`

- ### Indentation
    - If/Else
        - Example: age checker
    - Organizes our code into related statements or code blocks in a seamless way, which helps with readability
    - Poor indentation leads to errors
        - Python relies on indentation!
    - Indentation defines a new block of code
    - Whitespace errors (indenting when you shouldn’t)

- ### Input
    - Getting user input with `input()`
    - `input()` always returns a string, unless you specify otherwise!

- ### Python Docs
    - Library Reference Section
        - Buit-in Functions
        - Built-in Types

- ### Errors
    - Python Errors Slides