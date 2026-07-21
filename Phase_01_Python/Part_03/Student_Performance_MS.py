students_big_list = [
     {'roll_num': 34, 'name': 'a', 'dep': 'cs', 'marks': [34, 63, 11, 89, 10],'avg_marks': 61.4, 'total_marks': 307, 'grade': 'B'},
     {'roll_num': 90, 'name': 'javed', 'dep': 'sy', 'marks': [34, 35, 35, 23, 90],'avg_marks': 61.4, 'total_marks': 307, 'grade': 'A'},
     {'roll_num': 28, 'name': 'awis', 'dep': 'hard', 'marks': [24, 25, 27, 85, 11],'avg_marks': 65, 'total_marks': 307, 'grade': 'C'},
     {'roll_num': 29, 'name': 'har', 'dep': 'civil', 'marks': [24, 25, 22, 53, 69], 'avg_marks': 34.0,'total_marks': 307, 'grade': 'B'},
     {'roll_num': 79, 'name': 'ars', 'dep': 'mech', 'marks': [38, 79, 30, 90, 70], 'avg_marks': 70, 'total_marks': 307, 'grade': 'B'}

]

def calculate_avg(marks_list):
     sum=0
     for i in marks_list:
          sum +=i
          
     avg = sum/len(marks_list)
    #  print(f"the average marks of the studen is {avg}")
     return avg


def calculate_total(marks_list):
     total=0
     for i in marks_list:
          total +=i
     return total

def calculate_grade(marks_list):
     grade = ""
     t_marks = calculate_avg(marks_list)
     if t_marks < 50:
          grade = 'C'
          
     elif ( 50 < t_marks < 70 ):
          grade = 'B'
     else:
          grade = 'A'
        
     return grade

def update_marks():
     roll_num = int(input("enter the roll Number: "))
     find = False
     for i in students_big_list:
          if(i["roll_num"]==roll_num):
                marks_list = []
                j = 0
                while j < 5:
                    j +=1
                    marks = int(input("enter the marks: "))
                    marks_list.append(marks)
                i["marks"]=marks_list
                i["avg_marks"]=calculate_avg(marks_list)
                i["total_marks"]=calculate_total(marks_list)
                i["grade"]=calculate_grade(marks_list)
                found = True
                break
          if (found==False):
               print("not found")
     
def delete_student():
     roll_num = int(input("enter the roll Number: "))
     found = False
     for i in students_big_list:
          if(i["roll_num"]==roll_num):
               students_big_list.remove(i)
               print("you have successfully remove the student.")
               found = True
               break
     if (found == False):
        print("item not found")
          
def report():
     print("showing the top scorer: ")
     highest_score = 0
     for i in students_big_list:
          if(i["avg_marks"] > highest_score):
               highest_score = i["avg_marks"]
               name = i["name"]
    
     print("highest marks of the student is: ",highest_score)
     print("the name of the student is: ",name)

     print("showing the lowest scorer:  ")
     lowest_score = 100
     for i in students_big_list:
          if(i["avg_marks"] < highest_score):
               lowest_score = i["avg_marks"]
               name = i["name"]
     print("lowest marks of the student is: ",lowest_score)
     print("the name of the student is: ",name)

     print("number of students passed")
     pass_students = 0
     for i in students_big_list:
          if(i["avg_marks"] >= 50):
               pass_students +=1
     print(f"the number of student passed are: {pass_students}")

     print("number of students failed")
     fail_students = 0
     for i in students_big_list:
          if(i["avg_marks"] < 50):
               fail_students +=1
     print(f"the number of student failed are: {fail_students}")

     print("overall class average: ")
     overall_sum= 0
     count=0
     for i in students_big_list:
          overall_sum += i["avg_marks"]
          count +=1
     overall_avg = overall_sum/count
     print("the overall average of the class is: ",overall_avg)

     print("\n Highest mark obtained in every subject ")
     high_subject1= 0

     # for i in students_big_list:
     #      for a in i["marks"][]
     #      if(i["marks"][0] > high_subject1):
     #           high_subject1 = i["marks"][0]
     # print("the high socore int the first subject is: ",high_subject1)



while True:
   print(" ========= Student Management ========= ")
   print("1. Add Student ")
   print("2. Display All Students ")
   print("3. Search Student ")
   print("4. Update Student Marks") 
   print("5. Delete Student ")
   print("6. Generate Reports") 
   print("7. Subject Statistics ")
   print("8. Exit")

   

   try:
        option = int(input("Enter the option: "))
   except:
      print("enter the right option")

# ----------------  Options --------------------------

   match option:
        # -------------------------------- Add Student--------------------
      case 1:
           student_dit = {}
           print(" you are in Add Student ")
        #    Condition for uniqueness for the roll number
           unique=False
           while unique==False:                
                   roll_num = int(input("enter the roll number: "))
                   for i in students_big_list:
                        if (i["roll_num"] == roll_num):
                            print("roll number already exists...")
                            unique=False
                            break
                        else:
                             unique=True
           
        #  --------- checking the eligible age -------
           unique = False
           while unique==False:
                age = int(input("enter the age: "))
                if (age >= 15 and age < 30 ):
                     print("you have eligible")
                     unique = True
                     break
                else:
                     print("you are not eligible. try again...")
                
           name = input("enter student name: ")
           dep = input("enter the dep name: ")

        #    ------taking marks for 5 subjcts ----------

           marks_list = []
           i = 0
           while i < 5:
                i +=1
                marks = int(input("enter the marks: "))
                marks_list.append(marks)

        #    ------- calcuating the  average marks and total marks ----
           avg_marks = calculate_avg(marks_list)
           total_marks = calculate_total(marks_list)
           grade = calculate_grade(marks_list)
        
            # storing the data entered in dit from user
           student_dit.update({
                "roll_num":roll_num,
                "name": name,
                "dep": dep,
                "marks": marks_list,
                "avg_marks":avg_marks,
                "total_marks": total_marks,
                "grade" : grade

           })
           
        #    storing the dict in list 
           students_big_list.append(student_dit)
        # showing the entered data into the list
           for i in students_big_list:
                print(i)

           print("\n")

        # ============================ 2. Display All Students==================================================
      case 2:
           print("2. Display All Students ")

           print(f"Roll No\t Name\t Dep\t Avg\t Total\t Grade Marks\t")
           for i in students_big_list:
                print(i["roll_num"],"\t", i["name"],"\t", i["dep"],"\t",i["avg_marks"],"\t" ,i["total_marks"],"\t",i["grade"],i["marks"])
                        
      case 3:
           print("3. Search Student ")
           search_student = int(input("enter roll number to search: "))
           found =False
           for i in students_big_list:
                if(i["roll_num"] ==search_student ):
                     print(i)
                     found = True
                     break
           if not found:
            print("not found")

                    
        
      case 4:
           print("4. Update Student Marks") 
           update_marks()
      case 5:
           
           print("5. Delete Student ")
           delete_student()
      case 6:
           print("6. Generate Reports") 
           report()
      case 7:
           print("7. Subject Statistics ")
      case 8:
           break
           print("8. Exit")
        
         
         