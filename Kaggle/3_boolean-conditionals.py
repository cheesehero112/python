##### Booleans ######
# Python has a type of variable called bool. It has two possible values: True and False.

x = True
print(x)
print(type(x))

#prints:
# True
# <class 'bool'>

# Comparisons frequently work like you'd hope

3.0 == 3
# True

# But sometimes they can be tricky

'3' == 3
# False

##### Combining Boolean Values ######
# You can combine boolean values using the standard concepts of "and", "or", and "not". In fact, the words to do this are: and, or, and not.

# and is evaluated before or
True or True and False
# True

###### Conditionals ######
# Booleans are most useful when combined with conditional statements, using the keywords if, elif, and else.

def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")

inspect(0)
inspect(-15)

# 0 is zero
# -15 is negative

###### Boolean conversion ######
# We've seen int(), which turns things into ints, and float(), which turns things into floats, so you might not be surprised to hear that Python has a bool() function which turns things into bools.

print(bool(1)) # True - all numbers are treated as true, except 0
print(bool(0)) # False
print(bool("asf")) # True - all strings are treated as true, except the empty string ""
print(bool("")) # False
# Generally empty sequences (strings, lists, and other types we've yet to see like lists and tuples)
# are "falsey" and the rest are "truthy"

# using non-boolean objects in if conditions 
if 0:
    print(0)
elif "spam":
    print("spam")
# spam