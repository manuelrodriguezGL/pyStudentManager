students = []


class Student:

    name = ""
    last_name = ""
    student_id = ""
    school_name = "Miraflores"

    def __init__(self, name, last_name, student_id=000):
        """
        :param name:
        :param student_id:
        """
        self.name = name.title()
        self.last_name = last_name.title()
        self.student_id = student_id
        students.append(self)

    def add_student(self, name, last_name, student_id=000):
        self.name = name.title()
        self.last_name = last_name.title()
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student: " + self.last_name + ", " + self.name

    def printStudents(self):
        line = ""
        i = 0
        for student in students:
            line = line + student.name + " " + student.last_name + "\n"
            i = i + 1
        return line

    def get_name_capitalized(self):
        return self.name.capitalize() + " " + self.last_name.capitalize()

    def get_school_name(self):
        return self.school_name

    def save_file(self):
        try:
            f = open("students.txt", "a")
            f.write(self.name + " " + self.last_name + "\n")
            f.close()
        except Exception:
            print("Could not save file!")

    def read_file(self):
        try:
            f = open("students.txt", "r")
            for student in self.read_students(f):
                students.append(student)
            f.close()
        except Exception:
            print("Could not read file!")

    def read_students(self, f):
        for line in f:
            yield line

