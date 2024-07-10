# Grade students based on marks

# marks >= 90, grade = “A”

# 90 > marks >= 80, grade = “B”
# 80 > marks >= 70, grade = “C” 70 > marks, grade = “D”
# 1) Write a program which take input from user of their marks and return the grade.

mark_score = int(input("please give the marks"))

if mark_score >=90 :
    grade = "A"
elif mark_score >=80 and mark_score< 90:
    grade = "B"
elif mark_score >=70 and mark_score< 80:
    grade = "C"
else :
    grade = "D"

print ('Your grade is ', grade)