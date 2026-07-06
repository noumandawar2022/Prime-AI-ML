# name = "Muhammad Nouman Khan"

# print(len(name))
# print(name[4:19])

# # for i in name:
# #     print(i)

# print(name[::2])
# print(name[::-1])

#                       list 

# marks = [22,43,63]
# print(marks)
# print(len(marks))
# marks[1]= 55
# print(marks[1:2])

# # Methods

# marks.append(99)
# print(marks)
# marks.insert(0,202)
# print(marks)
# marks.sort()
# print(marks)
# marks.sort(reverse=True)
# print(marks)

# marks.reverse()
# a = marks.count(22)
# print("this is ab",a)

# print(marks)


#               for loop in list

# marks = [22,43,63,89,15,6,7,24,95]
# idx = 0
# for i in marks:
#     idx +=1
#     if (i == 1):
#         print(f"{i} is found at {idx}")
#         break
#     else:
#         print(f"it is not found")
    
#           Dictionary

# info ={
#     "name": "Nouman",
#     "age": 24,
#     "class": "3rd Year",
#     "roll no ": 104
# }
# print(info)
# print(type(info))
# print(info["name"])
# info["class"]= 15

# print(info.keys())
# print(info.values())
# print(info.items())

# print(info.get("name1"))
# print(info["name"])
# print(info.update({"pho no": 304}))
# print(info)


#               Sets

# s = {3,5,2,5,2,3}
# print(s)
# print(len(s))
# print(type(s))

# s.add(9)
# print(s)



info = [
("Alice", "Math"),
("Bob", "Science"),
("Alice", "Science"),
("Charlie", "Math"),
("Bob", "Math"),
("Alice", "English"),
("Charlie", "English")

]


# # print(info[1])
# s = set()
# for i in info:
#     print(i[1])
#     s.add(i[1]) 
    

# print("this is set",s)
# print(type(s))
# unique_list = list(s)
# print(unique_list)
# print(type(unique_list))

# list_eng_enroll = []

# for i in info:
#     if (i[1]== "English"):
#         print(i[0])
#         list_eng_enroll.append(i[0])

# print(list_eng_enroll)
# print(type(list_eng_enroll))

std_courses ={ }
courses=set()
for i in info:
    if info[0]==None:
        std_courses.update({info[0]:set()})
        std_courses[info[0]].add(info[1])
    else:
        std_courses[info[0]].add(info[1])

print(std_courses)