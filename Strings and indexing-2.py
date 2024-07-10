# 2) Write a program to create a new string made of an input string’s first, middle, and last character.

input_string = input("please input a string ")

first_char = input_string[0]

middle_index = len(input_string)//2

middle_char = input_string[middle_index]

end_char =  input_string[-1]

print ("The new string is:",first_char+middle_char+end_char)