...# 2) Write a program to check if a list contains a palindrome of elements. (hint: use copy( ) method)
# [1, 2, 3, 2, 1] [1, “abc”, “abc”, 1]
...
# original_list = input( "please input a list")


original_list1 =  [1, 2, 3, 2, 1]
# make a copy and reverse
copy_list = original_list1.copy()
copy_list.reverse()

# compare original vs reversed copy 
is_palindrome = (original_list1 == copy_list)

if is_palindrome:
    print (" the list ", original_list1,"is a palindrome" )
else :
    print (" the list ", original_list1,"is not a palindrome" )


original_list2 =  [1,"abc", "abc", 1]
# make a copy and reverse
copy_list = original_list2.copy()
copy_list.reverse()

# compare original vs reversed copy 
is_palindrome = (original_list2 == copy_list)

if is_palindrome:
    print (" the list ", original_list2,"is a palindrome" )
else :
    print (" the list ", original_list2,"is not a palindrome" )




# 