
# import pandas
spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)

##### Above will print #####
# 0
# But I don't want ANY spam!
# Spam Spam Spam Spam 


### How to check data type
type(spam_amount)
int

# Numbers

# single slash give a float 
print(5 / 2) # 2.5
print(6 / 2) # 3.0

# double slash give rounded down int
print(5 // 2) # 2
print(6 // 2) # 3

# Math order of operations
# PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction.

8 - 3 + 2 # 7
-3 + 4 * 2 # 5

### Use parens to make sure order of operation is what I want

# example A (not what I want)
hat_height_cm = 25
my_height_cm = 190
# How tall am I, in meters, when wearing my hat?
total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters =", total_height_meters, "?")
# Height in meters = 26.9 ?

# example B (this is what I want)
total_height_meters = (hat_height_cm + my_height_cm) / 100
print("Height in meters =", total_height_meters) 
# Height in meters = 2.15

### min and max return the minimum and maximum of their arguments, respectively...

print(min(1, 2, 3)) # 1
print(max(1, 2, 3)) # 3


### abs returns the absolute value of an argument:

print(abs(32))
print(abs(-32))


### In addition to being the names of Python's two main numerical types, int and float can also be called as functions which convert their arguments to the corresponding type:

print(float(10)) # 10.0
print(int(3.33)) # 3

# They can even be called on strings!
print(int('807') + 1) #808