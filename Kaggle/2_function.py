###### Getting Help #######
# You saw the abs function in the previous tutorial, but what if you've forgotten what it does?

# The help() function is possibly the most important Python function you can learn. If you can remember how to use help(), you hold the key to understanding most other functions.

# Here is an example:

help(round)


##### Defining functions ########
# Builtin functions are great, but we can only get so far with them before we need to start defining our own functions. 

#Below is a simple example.

def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

# To see what returns from a function, use print()!

print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7), # Python allows trailing commas in argument lists. How nice is that?
)
# Prints: 9 0 1


####### DocStrings #########
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

###### Functions that don't return ########

# Python allows us to define such functions. The result of calling them is the special value None. (This is similar to the concept of "null" in other languages.)

mystery = print()
print(mystery)

# Prints: None

##### Default arguments ######

print(1, 2, 3, sep=' < ')
# 1 < 2 < 3

# But if we don't specify a value, sep is treated as having a default value of ' ' (a single space).

print(1, 2, 3)
# 1 2 3

# Adding optional arguments with default values to the functions we define turns out to be pretty easy:

def greet(who="Colin"):
    print("Hello,", who)
    
greet()
greet(who="Kaggle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")

# Hello, Colin
# Hello, Kaggle
# Hello, world

####### Functions Applied to Functions ########

# Functions that operate on other functions are called "higher-order functions." 

def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1), 
    sep='\n', # '\n' is the newline character - it starts a new line
)
# Prints:
# 5
# 25

#Here's an interesting example using the max function.

# By default, max returns the largest of its arguments. But if we pass in a function using the optional key argument, it returns the argument x that maximizes key(x) (aka the 'argmax').

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)

# Prints:
# Which number is biggest?
# 100
# Which number is the biggest modulo 5?
# 14


def f(x):
    y = abs(x)
    return y

# Exercise: Functions and Getting Help

def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    
    return round(num, 2)
    
    
print(
    "round_to_two_places(3.14159) answer: ", 
    round_to_two_places(3.14159)
)

#2.
# The help for round says that ndigits (the second argument) may be negative. What do you think will happen when it is? Try some examples in the following cell.

print(
    "round(3.14159, -1) answer: ", 
    round(3.14159, -1)
)

# 3.
# In the previous exercise, the candy-sharing friends Alice, Bob and Carol tried to split candies evenly. For the sake of their friendship, any candies left over would be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.

# Below is a simple function that will calculate the number of candies to smash for any number of total candies.

# Modify it so that it optionally takes a second argument representing the number of friends the candies are being split between. If no second argument is provided, it should assume 3 friends, as before.

# Update the docstring to reflect this new behaviour.

def to_smash(total_candies, n_friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between n friends (default is 3).
    
    >>> to_smash(91)
    1
    """
    return total_candies % n_friends

#answer should be 0
print("number of candies that need to be smashed: ",
    to_smash(25, 5)
)
#answer should be 1
print("number of candies that need to be smashed: ",
    to_smash(31)
)
#answer should be 1
print("number of candies that need to be smashed: ",
    to_smash(45, 2)
)