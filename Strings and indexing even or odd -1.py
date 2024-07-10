# Write a program to check if a number entered by the user is odd or even.
number = input ("input a number")
last_digital = int(number[-1])
if last_digital in [0,2,4,6,8]:
    print ("it's even")
else:
    print ("it's odd")