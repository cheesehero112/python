# Temperature Checker
# Either from the Python REPL or from your text editor, write a program that:

# Sets a temperature variable to a temperature of your choosing

# Prints out Just right if the temperature is between 65 and 75

# Prints out It's hot! if the temperature is above that range

# Prints out It's a little cold. if the temperature is below 65

temp = input("What's your current temp?: ")

if int(temp) >= 65 and int(temp) <= 75:
    print("just right!")
elif int(temp) > 75:
    print("too hot!")
else:
    print("It's a little cold")