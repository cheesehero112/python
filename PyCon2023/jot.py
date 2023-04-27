from datetime import date
from pathlib import Path

jot_path = Path("jot.txt")

user_message = input("> ")
print(str(date.today()))

line = str(date.today()) + ': ' + str(user_message)
print(line)

# I can use f string to do the same thing as template literal
stringline = f"{date.today()}: {user_message}"
# this is how to use Python debugger
breakpoint()

contents = jot_path.read_text()
jot_path.write_text(contents + "\n" + line)
jot_path.read_text()

# I can use if/ else statement to check if the file exist first.
# if jot_path.is_file():
#     contents = jot_path.read_text()
# else:
#   constens = " "