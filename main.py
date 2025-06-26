class Student:
    def __init__(self, name, roll, total_marks, student_class):
        self.name = name
        self.roll = roll
        self.total_marks = total_marks
        self.student_class = student_class      
    def add_students(self):
       data_list.append(self)

    def __str__(self):
        return f"{self.name}, {self.roll}, {self.total_marks}, {self.student_class}"
try:
   with open("students.txt", "r") as file:
      total_students = [line.strip() for line in file]
      data_list = []
   for data in total_students:
      data1 = data.split(",")
      name = data1[0]
      roll = int(data1[1])
      total_marks = int(data1[2])
      student_class = int(data1[3])
      s1 =  Student(name, roll, total_marks, student_class)
      data_list.append(s1)

except FileNotFoundError:
   data_list = []


def main_menu():
    print('''<=====Main Menu=====>
1. Add a Student
2. View all student data
3. Delete a student data
4. filter student by category
5. Exit from the program
''')          
            
def saveornot():
       save_not = input("Do you want to save changes?(yes/no): ")
       if save_not.lower().strip() == "yes":
          with open("students.txt", "w") as file:
             for students in data_list:
                file.write(str(students) + "\n")
          print("Succesfully Saved.....")
       else:
          print("Changes not saved, just added")
while True:
  main_menu()
  try:
   choice = int(input('Enter your choice(1 to 5): '))
   if choice == 1:
     while True:
      numchoice = int(input("How many students do you add?: "))
      for i in range(1, numchoice+1):
        print(f"Student {i}: ")
        name = input("Enter the Name of student: ")
        student_class = int(input("Enter Class of student: "))
        roll = int(input("Enter the Roll number: "))
        total_marks = int(input("Enter total marks of student (out of 600): "))

        s1 = Student(name, roll, total_marks, student_class)
        s1.add_students()
        print("Succesfully added.......")

       
      saveornot()
     
      again = input("Do you want to add more students? (yes/no): ")
      if again.lower().strip() == "yes":
           continue
      elif again.lower().strip() == "no":
           print('Exiting to main menu....')
           break
      else:
           print("Something went wrong, Exiting to main menu....")
           break
   elif choice == 2:
      print('No Specific Order....')
      for i,student in enumerate(data_list, start=1):
         print(f"""{i}. Name of the student: {student.name} Class: {student.student_class}
Roll Number: {student.roll} Total Marks of the student (out of 600 marks): {student.total_marks}""")
         print(" ")
   elif choice == 3:
     while True:
      for i,student in enumerate(data_list, start=1):
         print(f"""{i}. Name of the student: {student.name} Class: {student.student_class}
Roll Number: {student.roll} Total Marks of the student (out of 600 marks): {student.total_marks}""")
      print(" ")
      print('Delete particular student data based on serial number shown above')
      try:
        choices = int(input("Enter the serial number: "))
        print(f'Student data with serial number {choices} succesfully removed...')
        data_list.pop(choices - 1)
        saveornot()
        again = input('Do you want to delete again? (yes/no): ')
        if again.lower().strip() == "yes":
           continue
        elif again.lower().strip() == "no":
           print('Going back to main menu....')
           break

        else:
           print("Something went wrong")
           break

      except ValueError:
         print('Please enter serial numbers only.....')
      
   elif choice == 4:
      while True:
       print('''1. Filter data by name of student
2. Filter data by class of student
3. Exit to main menu
''')  
       try:
        filter_choice = int(input("Enter your choice (1 to 2): "))
        if filter_choice == 1:
           name = input('Enter name of student: ').lower()
           found = False
           for student in data_list:
              if student.name == name:
                 print(f"""Name of student: {student.name}
Class: {student.student_class}, Roll Number: {student.roll}, Total Marks(out of 600): {student.total_marks}""")
                 found = True
           if not found:
              print('No matches found for that student')
        elif filter_choice == 2:
           try:
             st_class = int(input('Enter class of student: '))
             if st_class >0:
               print(f'Students data based on class {st_class}')
               found = False
               for i,student in enumerate(data_list):
                 if student.student_class == st_class:
                  print(f"""{i}. Name of student: {student.name}
Class: {student.student_class}, Roll Number: {student.roll}, Total Marks(out of 600): {student.total_marks}""")
                 found = True
               if not found:
                print('No student data found for that class')
             else:
              print('Please enter correct class')
           except ValueError:
               print("Please enter correct class of the student")    
        elif filter_choice == 3:
           print('Exiting to main menu....')
           break
        else:
           print('Wrong input.. please enter correct choice')
       except ValueError:
         print('Please choose correct choice....')
   elif choice ==5:
      print('Thanks for using our program...')
      exit()
   else:
      print('Wrong input, please enter correct input/values....')
      continue
     
  except ValueError:
        print('Please enter correct input/values......')
        continue


