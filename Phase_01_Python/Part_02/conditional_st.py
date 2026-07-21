#  Categorize Person on the base of Age

# age = int(input("Enter your age: "))

# if (age < 13) :
#     print("you are child. ")
# elif (age > 13 and age <= 18 ):
#     print("you are a teenager. ")
# else:
#     print("you are adult. ")

# Email and Password authenicator

# enter_email = input("Enter your email: ")
# enter_password = input("Enter your Password: ")

# stored_email = "nouman@gmail.com"
# stored_password = "NoumanKhan12"

# if (enter_email == stored_email and enter_password == stored_password):
#     print("you have successfully Log in .")
# elif (enter_email != stored_email ):
#     print("you have entered wrong password")
# else:
#     print("you have wrong password")

# IS the Number divisible by N number
# a = int(input("Enter the value: "))
# if ( a % 5 == 0):
#     print("it is divisble by 5.")
# else:
#     print("not divisible by 5.")

# Odd or Even

# a = int(input("Enter the value: "))
# if ( a%2 ==0 ):
#     print("it is even number.")
# else:
#     print("it is odd number")


age = int(input("enter your age: "))

match age:
    case age if age > 0 and age < 18:
        print("you are teenage of 12 years.")
    case 18:
        print("you are an adult of 18 years.")
    case age if age > 17  and age < 25:
        print("you are eligiable for mariage.")
    case 22:
        print("you are an adult of 22 years.")
    case _:
        print("you are out of the  years.")