# Write a program to find the greatest of 3 numbers entered by the user.

x = int(input("Please input the first number (x): "))
y = int(input("Please input the second number (y): "))
z = int(input("Please input the third number (z): "))

if x>y and y>z: 
    print ('the greatest is ', x )
elif y>x and y>z: 
    print ('the greatest is ', y )
else:
    print ('the greatest is ', z )