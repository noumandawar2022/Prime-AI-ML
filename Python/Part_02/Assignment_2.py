
# salary = int(input("Enter your salary: "))

# if salary < 30000:
#     final_tax = salary * 0.05
#     print("the tax small on your salary is: ",final_tax)
# elif (salary > 30000 and salary < 70000) :
#      final_tax = salary * 0.15
#      print("the tax range on your salary is: ",final_tax)
# else:
#     final_tax = salary * 0.25
#     print("the tax highest on your salary is: ",final_tax)


# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

# for i in range(a,b+1):
#     if(i % 2 == 0):
#         print(i)


#                       Question 03


# def digits_count(n):
#     for i in n:
#         print(i)

# n = input("enter the digits: ")
# digits_count(n)


#                   Question 04

# def count_digits(n):
    
#     print("the count number of the digits are: ", count)
#     return count

# n = int(input("enter the number: "))

# count_digits(n)


# # Question 06

# def print_numbers(n):
#     for i in range(n):
#         if (i % 3 == 0 and i % 5 == 0):
#             print("skipping")
#             continue
#         print ( i)

# n = int(input("Enter the number: "))
# print_numbers(n)


#  Question 07

# def pos_neg():
#     while(True):
#         try:
#             n = input("enter the number. ")
#             if( n == "Quit" ):
#                 print("we are quiting")
#                 break
#             n = int(n)
#             if(float(n) >= 0 ): 
#                 print("it is positive")
#             else:
#                 print("it is negative")
#         except:
#             print("invalid")
# pos_neg()

#  Question 8 

# def calculator(a,b,operation):
    
#     # for addition
#     if (operation == "+"):
#         sum= a+b
#         print(f"the sum is: {sum}")
#     elif(operation == "-"):
#         difference = a-b
#         print(f"the difference is: {difference}")
#     elif(operation == "*"):
#         multiplication = a*b
#         print(f"the multiplication is: {multiplication}")
#     elif(operation == "/"):
#         division = a/b
#         print(f"the division is: {division}")
    
# calculator(4,2,"+")
# calculator(40,10,"*")
# calculator(45,22,"-")
# calculator(48,6,"/")

# Question 9

# def is_prime():
#     n = int(input("enter a number: "))
#     if(n < 2):
#         print("it is not prime number.")
#     for i in range(2,n//2+1):
#         if(n % i == 0):
#             print("it is non-prime number.",n)
#             return
#     print("prime ")
    
    
# is_prime()

# Question 10

def number_guessing_game():
    count = 3
    secret_n= 2020
    print("you have three attempt!")
    while(count != 0):
        count -=1
        print("youe remaining attempt is: ", count)

        n = int(input("Enter the number: "))
        if(n==secret_n):
            print("you have guessed it rightly,",n)
        else:
            if(secret_n - n > 0 ):
                print("too low guess...")
            else:
                print("too high guess...")
            print("try agian.")
        
number_guessing_game()
    

        
        
    

