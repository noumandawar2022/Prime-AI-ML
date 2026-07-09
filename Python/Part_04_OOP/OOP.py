class Student:
    print("this is the student class")
    college_name = "Cadet College Razmak"

    # this is used when you want to pass values in runtime means your choice of value not fix
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def get_marks(self):
        print("this is the marks instance")
        return self.marks

    

stu1= Student("Nouman",23,1013)
stu2= Student("ali",22,1050)
stu3= Student("rahul",12,900)
# stu4=Student()

print(stu1.name,stu1.age,stu1.marks)
print(stu2.get_marks())
# print(stu4) 

# for accessing the instance variable we use object
print(stu3.name)

# for accessing the class variable we use the class name and as well by object
print(Student.college_name)
print(stu3.college_name)

class Laptop:
    storage_type = "SSD"

    def __init__(self,ram,storage):
        self.ram = ram
        self.storage = storage

    def get_info(self):
        print(self)
        print(f"laptop has {self.storage_type} type storage and {self.ram} GB ram and {self.storage} backup storage")
        
    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")

l1= Laptop(16,512)
l2 = Laptop("8","256")
print((type(l1.ram)))
l1.get_info()

Laptop.get_storage_type()
l1.get_storage_type()


class Product_Store:
    print("this is the Product Store class")
    count =0

    def __init__(self,name,price):
        self.name = name
        self.price = price
        Product_Store.count +=1
    @classmethod
    def info_product(cls):
        print(f"the number of the product created is: {cls.count}")
    @staticmethod
    def calculate_discount(price,precentage):
        discount = ((precentage/100)*price)
        final_price = price - discount
        print(f"final Price is after the discount is: {final_price}")
        return final_price
        
p1= Product_Store("mobile",50_000)
p2= Product_Store("laptop",90_000)

print(p1.name , p1.price)
Product_Store.calculate_discount(p1.price,10)
Product_Store.info_product()


# =========================== Encapusulation ================
class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        # self.balance = balance
        # self._balance = balance # this is usef for Protected 
        self.__balance = balance # this is used for the Private
    
    def get_balance(self): # this is getter
        return self.__balance
    
    def set_balance(self,newBalance): # this is setter
        self.__balance = newBalance

acc1=BankAccount("nouman",20_000)
acc2 = BankAccount("ali",30_000)
print(acc1.name,acc2.get_balance())

acc1.set_balance(35_000)
print(acc1.get_balance())

# ===================== Inheritance =============================

class Employee():
    start_time = "8 am"
    end_time = "6 pm"

    # def __init__(self):
        

class Teacher(Employee):
    print("this is teacher class")
    def __init__(self,subject):
        self.subject = subject
        
t1 = Teacher("Maths")
print(t1.start_time,t1.end_time,t1.subject)

# ++++++++++++++++++++ Multi Level Inheritance +++++++++++++++++

# also continuing the above
class Admin(Teacher):
    print("this is the third level inheritance  ")
    def __init__(self, role,subject):
        super().__init__(subject)
        self.role = role

adm1 = Admin("Manager","maths")
print(f"the star time is {adm1.start_time} and end time is {adm1.end_time} and teacher subject is {adm1.subject} and admin role is {adm1.role}")

# -------------------  Multiple Inheritance -------------------

class Employee1():
    print("this is employee1 class")
    def __init__(self,name,age):
        self.name= name
        self.age = age
class Worker(Employee1):
    print("this is worker class ")
    def __init__(self,wage):
        self.wage = wage
    
class CEO(Worker):
    print("this is ceo class")
    def __init__(self,name,age,wage,worth):
        Employee1.name = name
        Employee1.age =age
        Worker.wage = wage
        self.worth = worth

ceo1 = CEO("nouman",23,26_000,5000_000)
print(ceo1.name,ceo1.age,ceo1.wage,ceo1.worth)

# +++++++++++++++ Abtraction ++++++++++++++
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Lion(Animal):
    def make_sound(self):
        print("Roar!!")

lion = Lion()
lion.make_sound()