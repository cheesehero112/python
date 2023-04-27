# import threading

# def breathe_in():

#   print("breathe in")

# def breathe_out():

#   print("breathe out")

# # Create a timer that will call my_function() after 5 seconds

# def breathe():
#   breatheIn = threading.Timer(0, breathe_in)

#   breatheIn.start()

#   breatheOut = threading.Timer(7, breathe_out)

#   breatheOut.start()

# breathe = threading.Timer(0, breathe)


# print(breathe)

#Answers in lecture
import time
times = 2*60/6
# I can also do 2*60//6
for x in range(int(times)):
  print("Breath in")
  time.sleep(6)
  print("Breath out")
  time.sleep(6)