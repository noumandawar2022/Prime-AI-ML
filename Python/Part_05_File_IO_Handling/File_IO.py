

# =================reading the file================
'''
# f = open(r"D:\Prime AI ML\00. A Code Section\Python\Part_05_File_IO_Handling\sample.txt","r") # file object

# data  = f.read() # readline , readlines
# print(data)
# print(type(data))

# f.close()
'''
#  ==================== writing file ====================
'''
# f = open(r"D:\Prime AI ML\00. A Code Section\Python\Part_05_File_IO_Handling\sample.txt","w") # file object

# # f.write("this is to overwrite the existing data \n so it totally new data") # readline , readlines
# f.write("123")
# print(data)
# print(type(data))

# f.close()

'''
#  ============== files operation Modes  =================
'''
# a 
f = open(r"D:/Prime AI ML/00. A Code Section/Python/Part_05_File_IO_Handling/sample2.txt","a+") # file object
f.seek(0)
print(f.read())
# f.write("this is read for 3") # readline , readlines
# f.write("this is ...........")
print(f.read())

f.close()
'''

#  ============== open with " with" ===========
'''
with open("D:/Prime AI ML/00. A Code Section/Python/Part_05_File_IO_Handling/sample.txt","r+") as f:
    print(f.read())
    f.write("\n nouman is my name33..")
    f.seek(0)
    print(f.read())
'''
# ============ Delete a file ================

# import os

# os.remove("D:/Prime AI ML/00. A Code Section/Python/Part_05_File_IO_Handling/sample.txt")
# os.remove("D:/Prime AI ML/00. A Code Section/Python/Part_05_File_IO_Handling/reminig.py")

#  ============= find a word from txt file ===========
'''
with open("D:/Prime AI ML/00. A Code Section/Python/Part_05_File_IO_Handling/sample.txt","a+") as f:
    # f.write("this is for python programming.\n we will learn machine learinging.\n we have to code")
    f.seek(0)
    count = 0
    found = False
    while (found != True):
        a=f.readline()
        count +=1
        if a=="":
            break
            
        if "aj"  in a:
            print("print it is found and line number is: ",count)
            found = True
            break

        
    if(found == False):
        print("it is not found")


'''

#  ================ Exception Handling ==============

'''
try:
    x = int(input("enter the number"))
    div = 10/x
    

except ZeroDivisionError:
    print("you can't divided by 0 ")
except ValueError:
    print("you can't divided by string")
else:
    print(div)
finally:
    print("program is end")


'''

#  ======================== List Comprehension =================

even = []

for i in range(5):
    even.append(i**i)
print(even)

# simple way

even1 = [i**i for i in range(5) if i % 2 ==0]
print(even1)

nums = [1,-4,6,2,-9,-5,4,-7]
print(nums)
nums = [ 0 if val<0  else val for val in nums]
print(nums)