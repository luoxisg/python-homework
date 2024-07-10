# Write a program to check if a number is a multiple of 7 or not

number = int(input("Please input the  number : "))

is_multi7 = int(number%7)

if is_multi7 == 0:
    print (str(number),"this  number can be multiped by 7 ")
else:
    print (str(number),"this  number can not  multiped by 7 ")
