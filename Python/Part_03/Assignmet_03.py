"""
Python Fundamentals 
(Assignment3) 
Assignment Problems
Q1
. Ask the user for a string and check whether it is a palindrome or not. 
A  
palindrome
“madam”, “
is a string which is same when we read it forward & backward. Eg - 
racecar” etc.
[ 
Hint- A palindrome string is equal to the reversed version of the string. We can 
use a loop to reverse the string manually. ]
Q2.
Q3
Given a list of integers compute the average of all numbers in the list.
. Input two lists of integers from the user. Merge them into one list and sort the 
result.
Eg -  
list1 = [1, 2, 7]
,  
list2 = [2, 4, 5]
result = [1, 2, 3, 54, 5, 7]
Q4
. Given a tuple of integers, create:
• 
A tuple of all even numbers
• 
A tuple of all odd numbers
. Create a dictionary where:
Q5
Q6
• 
Keys = student names
• 
Values = marks (integer)
A
Write a menu-based program where user presses a key (ʼAʼ, ‘Bʼ, ‘Cʼ, ‘Dʼ) 
depending on the operation they want to perform on the dictionary:
1. - Add a student
B
2. - Update marks
C
3. - Search for a student
D
4. - Display all students and marks
. Given a list of words:
words = ["apple", "banana", "kiwi", "cherry", "mango"]
Create a dictionary that maps each word to its length.
Example:
{"apple": 5, "banana": 6, "kiwi": 4, ...}
Q7
. Write a program that takes a string from the user and prints the number of 
spaces in the string.
Q8
. Write a program to check whether two lists share no common elements. 
# share no common elements list1 = [1, 2, 3, 4] list2 = [5, 6, 7, 8]
# share common elements list1 = [1, 2, 3] list2 = [3, 4]
[ 
Hint
Q9- use sets]
. Given a list, print all elements that appear more than once in the list.
[ 
Hint- use sets]
. Ask the user for a string and print:
Q10
• 
All unique characters
• 
The count of unique characters

"""

#               Question 01

# word = input("Enter the string: ")
# if (word ==  word[::-1]):
#     print("it is palindrome")

#           Question 02

# int_list = [2,5,2,6,3,9]
# sum = 0
# count=0
# for i in int_list:
#     sum += i
#     count +=1
# avegerage_list = sum/count
# print(avegerage_list)


#           Question 03

# count_list_1 = int(input("enter the number of entity to enter for list_1: "))
# count_list_2 = int(input("enter the number of entity to enter for list_2: "))

# list_1 = []
# list_2 = []
# i =0
# while( i < count_list_1):
#     number = int(input("enter the numbersfor list_1 for : "))
#     list_1.append(number)
#     i +=1
# print(list_1)
# j=0
# while( j < count_list_2):
#     number = int(input("enter the numbers for list_2: "))
#     list_2.append(number)
#     j +=1

# print(list_2)

# list_3= list_1 + list_2
# print(f"the combine list of list_1 and list_2 {list_3}")
# print(type(list_3))


#           Question 04----------------------------------

# tuple_q = int(input("enter the number of elements to enter for tuple_q: "))

# # tuple_combine = ()
# list_for_tuple =[]
# i = 0
# count =0
# while (i < tuple_q):
#         number = int(input("enter the values for tuple: "))
#         list_for_tuple.append(number)
#         i +=1
# #best practice
# # input1=input("Enter the elements of list with spaces")
# # input1.split()

# tuple_combine = tuple(list_for_tuple)
# print(tuple_combine)
# print(type(tuple_combine))
# even_list =[]
# odd_list =[]
# for i in list_for_tuple:
#         if (i %2 == 0):
#                 even_list.append(i)
#         else:
#                 odd_list.append(i)

# odd_tuple = tuple(odd_list)
# even_tuple = tuple(even_list)
# print(odd_tuple)
# print(even_tuple)


#       ----------------- Question 05 ----------------------------

# std_marks ={ 
#     "nouman": 45,
#     "ali":34
# }

# while True:
#     option = input("enter the option  for the operation: ")
#     match option:
#         case "A":
#             print("Your are performing adding student----")
#             std_name = input("enter the name of the studnet: ")
#             st_marks = int(input("enter the marks: "))
#             std_marks.update({std_name:st_marks})
#             for name, marks in std_marks.items():
#                 print(name,marks)
                


#         case "B":
#             print("Your are performing Updating Marks ----")
#             upt_marks_name = input("which student marks you want to update: ")
#             upt_marks=int(input("what marks you want to update: "))
            
#             if(std_marks.get(upt_marks_name) != None):
#                 std_marks[std_name]=upt_marks
#             else:
#                 print("name is not found")
            
#             for name, marks in std_marks.items():
#                 print(name,marks)
                

#         case "C":
#             print("Your are performing a seaching for a student----")
#             name_search = input("enter the name to search: ")
#             if name_search in std_marks:
#                 print(std_marks.get(name_search))
#             else:
#                 print("student not found")
#         case "D":
#             print("Your are performing Displaying all students  and Marks ----")
#             for name , marks in std_marks.items():
#                 print(f"name: {name} and marks:{marks}")
#         case "E":
#             print("you are quiting")
#             break


#  ------------- Question 06 --------------------

# dict_count = { }

# words = ["apple", "banana", "kiwi", "cherry", "mango"]

# for ch in words:
#     print(f"the leng of the ch: {len(ch)}")
#     dict_count.update({ch:len(ch)})

# for name , count in dict_count.items():
#     print(name,count)
    
# -----------------------Qurestion 07---------j

# sen = input("enter th string: ")

# sen = sen.count(" ")
# print(sen)
    

# -----------------------Qurestion 08---------

# list_1 = [1, 2, 3, 4,5,8] 
# list_2 = [5, 6, 7, 8,1,3]
# list_1_set = set(list_1)
# list_2_set = set(list_2)
# print(type(list_1_set))

# inter_set = list_1_set.intersection(list_2_set)
# print(inter_set)
# print(f"is there any common elements ")

# -----------------------Qurestion 09 ---------

# list_1 = [1, 2, 3, 4,5,8,1,1,2,3]

# uniqe = set()
# dup = set()

# for i in list_1:
#     if i in uniqe:
#         dup.add(i)
#     else:
#         uniqe.add(i)
# # set_list = set(list_1)
# print(uniqe)
# print(dup)
# # set_list# -----------------------Qurestion 10---------

string_user = input("enter the number: ")
set_unique = set()
cout_uniqu = 0
for i in string_user:
    set_unique.add(i)

for i in set_unique:
    cout_uniqu +=1
print(cout_uniqu)
print(set_unique)

