# Write a program to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.


marks_dict ={}
for i in range (3):
    subject = input(" please input subject: " )
    marks = int(input(" please input the mark"))
    marks_dict[subject] = marks

print("Marks dictionary:", marks_dict)



