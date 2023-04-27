# https://pycon2023.pym.dev/lists/#list-exercises

import random

answer = input("Tell me how you are doing? : ")

possibleAnswers = ["good", "ok", "bad", "so so", "great", "fantastic", "can be better"]

myAnswers = ["I'm great, thank you!", "I'm ok", "could be better, thanks for asking"]

if answer in possibleAnswers:
    print("I'm glad to hear that!")
elif answer == "How are you?":
    print(random.choice(myAnswers))
else:
    print("I truly don't know what that is like.")

# How do I make it so I can detect a "good" in "I'm good"?
# ==> I can loop and compare the two words