# name = ""
# student_id = 0
students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
        return students_titlecase


def pirint_students_titlecase():
    print(get_students_titlecase())


def add_student(name, student_id=000):
    student = {"name": name, "student_id": student_id}
    students.append(student)
