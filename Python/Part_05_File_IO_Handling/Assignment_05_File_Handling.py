
#  ======================== Question 1 =================

'''
with open("D:/Prime AI ML/00. A Code Section/Python/Part_05_File_IO_Handling/names.txt","w") as f:
    f.writelines(["nouman\n","ali\n","javed\n","harron\n","arslan\n"])


with open("D:/Prime AI ML/00. A Code Section/Python/Part_05_File_IO_Handling/names.txt","r") as f1:
    print(f1.read())

    
'''
#  ======================== Question 2 =================

'''
with open("D:/Prime AI ML/00. A Code Section/Python/Part_05_File_IO_Handling/log.txt","a") as f:
    f.write("Program run successfully secondly")

with open("D:/Prime AI ML/00. A Code Section/Python/Part_05_File_IO_Handling/log.txt","r") as f:
    print(f.readlines())


'''

#  ======================== Question 3 =================

'''
mult_5 = [ 5*i for i in range(1,6)]
print(mult_5)

grt_15 = [ val    for val in mult_5  if val > 15]
print(grt_15)


'''

#  ======================== Question 4 =================

# '''
import json
cities ={
        "taxila": 20_000,
        "rawalpendi" : 30_000,
        "islamabad": 60_000
    }
with open("D:/Prime AI ML/00. A Code Section/Python/Part_05_File_IO_Handling/cities.json","w") as f:
  
    json.dump(cities,f)

with open("D:/Prime AI ML/00. A Code Section/Python/Part_05_File_IO_Handling/cities.json","r") as f:
    print(f.read())

with open("D:/Prime AI ML/00. A Code Section/Python/Part_05_File_IO_Handling/cities.json","a+") as f:
    city_name = input("enter the city name: ")
    city_pop = int(input("enter the population of the city: "))
    cities.update({city_name: city_pop})
    json.dump(cities,f)
    f.seek(0)
    print(f.read())
# '''


#  ======================== Question 5 =================

'''

try:
    with open("D:/Prime AI ML/00. A Code Section/Python/Part_05_File_IO_Handling/log.txt","r") as f:
        print(f.read())

except:
    print("the file does not exit")

finally:
    print("the program is finished")

'''



