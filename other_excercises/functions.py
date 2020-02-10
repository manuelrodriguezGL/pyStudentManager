# name = ""
# student_id = 0
students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    print(get_students_titlecase())


def add_student(name, student_id=000):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception as error:
        print("Could not save file!")
        print(error)


def read_file():
    try:
        f = open("students.txt", "r")
        for student in read_students(f):
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file!")


def read_students(f):
    for line in f:
        yield line


def main_run():
    var_continue = True
    read_file()
    print_students_titlecase()
    while var_continue:
        user_answer = "NO"
        student_name = ""
        student_id = ""
        student_name = input("Enter student's name: ")
        student_id = input("Enter student's ID: ")
        add_student(student_name, student_id)
        save_file(student_name)
        user_answer = input("Do you want to add more students? YES/NO: ").upper()
        if user_answer == "NO":
            var_continue = False

    print("Student information: ")
    print_students_titlecase()


main_run()
