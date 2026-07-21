
# cgpa = float(input("Enter your CGPA: "))

# match cgpa:
#     case 4:
#         print("you are the topper")
#     case 3.5:
#         print("You are the second topper.")
#     case 3:
#         print("you are the average student.")
#     case _:
#         print("your are the below average student.")

        # Print from 1 0 to 5
# i=0
# while i <=5:
#     print(i)
#     i +=1
# print("the count now will be: ", i)

# Table of 9

# j = 1
# while j<=10:
#     print("6 x", j,"= ",6*j)
#     j +=1


# not print the multiples of 7
# i =0 
# while i <=50:
#     i +=1
#     if( i % 7 == 0):
#         print("skipping")
#         continue
#     print(i)


# For Conditions

# word = "pakistan"

# for i in word:
#     print(i)

# count = 0 
# for char in word:
#     if (char == "a") :
#         count +=1

# print(count)

# counting vowals in words

# word = "artificial"

# count=0
# for ch in word:
#     if (ch == "a" or ch ==  "e" or  ch ==  "i" or ch ==  "o" or ch == "o"):
#         count +=1
# print(count)

# range function  (start, stop, increase)

# for i in range(1,10,2):
#     print (i)

# sum of first nutural numbers
# sum = 0
# for i in range(1,10+1):
#     sum +=i
#     print(sum, i)

# Functions

# def sum(a,b):
#     s= a+b
#     return s

# ans = sum(2,4)
# print(ans)

# average functions

# def avg(a,b,c):
#     sum=a+b+c
#     average = sum/3
#     return average

# print(avg(4,6,8))

# lambda functions

# sum = lambda a,b,c: (a+b+c)/3
# print(sum(2,4,6))

# Factorail 

# n = int(input("Enter the value of factorial: "))

# def cal_fact(n):
#     fact =1
#     for i in range(1,n+1):
#         fact *=i

#     return fact

# print(cal_fact(n))

def get_largest (a, b, c):  
    if (a > b and a > c): 
        return a 
    elif b > c: 
        return b 
    else: 
        return c 

print (get_largest (3, 10, 5)) 
