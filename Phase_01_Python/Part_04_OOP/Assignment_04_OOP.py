"""
    Q1. Create a 
    BankAccount 
    class with attributes account_number, owner_name, 
    and balance. 
    Add methods to deposit, withdraw, and check balance. 
"""
#  ======================== Question 1 =================
# class BankAccount:
#     def __init__(self,account_number,owner_name,balance):
#         self.account_number = account_number
#         self.owner_name = owner_name
#         self.balance = balance
    
#     def deposit(self,amount_add):
#         print("you are adding the amount into your account: ",amount_add)
#         self.balance= self.balance + amount_add
        
        
#     def check_balance(self):
#         print("your current amount is: ",self.balance)

#     def withdraw(self,amount_less):
#         print("you are subtracting the amount into your account: ",amount_less)
#         self.balance = self.balance - amount_less

# acc1 = BankAccount(104,"nouman",20_000)
# print("account number is: ",acc1.account_number,"and name is: " ,acc1.owner_name, "and balance is: ",acc1.balance)
# acc1.check_balance()
# acc1.deposit(10_000)
# acc1.check_balance()
# acc1.withdraw(5_000)
# acc1.check_balance()

# 
#  ======================== Question 2 =================

# class Book:
    
#     def __init__(self,title,author,list_reviews):
#         self.list_reviews =[]
#         self.title = title
#         self.author = author
#         # self.reviews = reviews
#         self.list_reviews.append(list_reviews)

#     def add_review(self,review):
#         print("this is the review adding section")
#         self.list_reviews.append(review) 
    
#     def display_reviews(self):
#         print("displaying all the reviews. ")
#         for i in self.list_reviews:
#             print(i)
#     def count_reviews(self):
#         print("count the number of the reviews...")
#         count = 0
#         for i in self.list_reviews:
#             count +=1
#         print("the total number of the reviews are: ",count)
# b1 = Book("What IF","John","this is nice book")
# print(f"the book name is: {b1.title}, and author is: {b1.author} and review is: {b1.list_reviews}")
# b1.add_review("good for self improvement")
# print(type(b1.list_reviews))
# b1.display_reviews()
# b1.count_reviews()

#  ======================== Question 3 =================
'''
class Student:
    creat = False
    def __init__(self,name,roll_no,marks):
        
        
        if(( name != "") and ( 1 < roll_no < 100) and (marks > 0 ) ):
            print("tis is if")
            self.__roll_no = roll_no
            self.__marks = marks
            self.__name = name
            creat = True
        
    def set_info(self,new_roll_no, new_marks):
        if( ( 1 < new_roll_no < 100) and (new_marks > 0 )):
            print("assigning the new marks and roll no")
            self.__roll_no = new_roll_no
            self.__marks=new_marks
        else:
            print("not assign")
    def get_info(self):
        print(f"the name is: {self.__name} and roll no is: {self.__roll_no} and marks is: {self.__marks}")

st1= Student("",10,1013)
if (Student.creat != False):
    st1.get_info()
    st1.set_info(101,500)
    st1.get_info()
else:
    print("no further action")

'''
'''
#  ======================== Question 4 =================

class Shape:
    def __init__(self):
        print("this is the init of the shape")
        # pass

    def area(self):
        print("this is the shape method")
        # pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        print("this is the init method of the circle")
    
    def area(self):
        area = 3.14*(self.radius**2)
        print("area of the circle is ",area)
        # return

class Rectangle(Shape):
    def __init__(self,len,brth):
        self.len = len
        self.brth = brth
        print("this is the init method of the rectangle")
    
    def area(self):
        area = self.len*self.brth
        print("area of the rectangle is ",area)


# shp1 = Shape ()
ci1= Circle(10)
ci1.area()

# rt1= Rectangle(10,20)
# print(rt1.area())

'''
#  ======================== Question 5  =================
'''
class Vehicle:
    def __init__(self):
        brand_in = input("enter the name of the brand: ")
        model_in = int(input("enter the model no: "))
        self.brand_in = brand_in
        self.model_in = model_in

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        seats= int(input("enter the number of seats: "))
        self.seats = seats

    def info(self):
        print(f"the brand is: {self.brand_in} and model is: {self.model_in} and seats are: {self.seats}")

class Bike(Vehicle):
    def __init__(self,eng_cap):
        super().__init__()
        self.eng_cap = eng_cap
    def info_bike(self):
        print(f"the brand is: {self.brand_in} and model is: {self.model_in} and seats are: {self.eng_cap}")
# v1= Vehicle()
# c1 = Car()
b1 = Bike(125)

# print(v1.brand_in,v1.model_in)
# c1.info()
b1.info_bike()

'''

# -----------------------Qurestion 06---------
'''
from abc import ABC , abstractmethod

class Empoyee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Empoyee):
    def __init__(self,name,rate,time):
        self.name = name
        self.rate = rate
        self.time = time
    def calculate_salary(self):
        print("inern stipend")
        stipend = self.rate * self.time
        print("your stipend is: ",stipend)
        
class FullTimeEmployee(Empoyee):
    def __init__(self,name,salary,bouns):
        
        self.name = name
        self.salary = salary
        self.bouns = bouns
    def calculate_salary(self):
        print("full time salary")
        full_salary = self.salary+ self.bouns
        print("your full salary is: ",full_salary)

i1 = Intern("ali",5,90)
i1.calculate_salary()
ft1= FullTimeEmployee("javed",50_000,10_000)
ft1.calculate_salary()

'''
#  ======================== Question 7 =================
'''
class Person:
    def __init__(self,name=None,age=None,address=None):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        print(f"my name is: {self.name} and my age is: {self.age} and address is: {self.address}")

p1= Person()
p2= Person("nouman")
p3= Person("ali",23,"taxila")
p1.info()
p2.info()
p3.info()
'''
#  ======================== Question 8 =================
'''
class Player:
    player_count =0
    def __init__(self,name,level):
        self.name = name
        self.level = level
        Player.player_count +=1

    def info(self):
        print(f"the nubmer of the player created is: {Player.player_count}")
p1= Player("ali",5)
p2 = Player("javed",2)
p3= Player("nouman",8)
p1.info()

'''
#  ======================== Question 9 =================
'''
class Herbivore:
    def __init__(self,h_name,age,weight):
        self.h_name = h_name
        self.age = age
        self.weight = weight
    def mass(self):
        h_mass =  self.age  / self.weight 
        return h_mass
    

class Carnivore:
    def __init__(self,c_name,hight,width):
        self.c_name = c_name
        self.hight = hight
        self.width = width
    def voulume(self):
        c_volume = self.hight * self.width
        return c_volume
    

class Omnivore:
    def __init__(self,o_name,rate,distance):
        self.o_name = o_name
        self.rate = rate
        self.distance = distance
    def walk(self):
        o_walk = self.rate + self.distance
        return o_walk

class Bear(Herbivore,Carnivore,Omnivore):
    def __init__(self, h_name, age, weight ,c_name,hight,width,o_name,rate,distance,b_name):
        super().__init__(h_name, age, weight)
        Carnivore.__init__(self,c_name,hight,width)
        Omnivore.__init__(self,o_name,rate,distance)
        self.b_name = b_name

    def show(self):
        print(f"the return of a: {self.mass(),self.voulume(), self.walk() }")
        print(f"the info of first class is: {self.h_name,self.age,self.weight} and he info of second class is: {self.c_name,self.hight,self.width} and the third info is: {self.o_name,self.rate,self.distance} and the fourth is: {self.b_name}")

b1 = Bear("a",30,300,"b",50,30,"c",30,20,"d")
b1.show()

'''

