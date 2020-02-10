from model.hs_student import HighSchoolStudent

# import model.hs_student # Another way of calling the import

new_student = HighSchoolStudent("", "")
var_continue = True
new_student.read_file()
while var_continue:
    user_answer = "NO"
    student_name = ""
    student_last_name = ""
    student_id = ""
    student_name = input("Enter student's name: ")
    student_last_name = input("Enter student's last name: ")
    student_id = input("Enter student's ID: ")
    new_student.__init__(student_name, student_last_name, student_id)
    new_student.save_file()
    user_answer = input("Do you want to add more students? YES/NO: ").upper()
    if user_answer == "NO":
        var_continue = False

print("Student information: ")
print(new_student.printStudents())