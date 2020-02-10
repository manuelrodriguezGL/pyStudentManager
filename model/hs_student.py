import model.student


class HighSchoolStudent(model.student.Student):

    school_name = "CTP Flores"

    def __init__(self, name, last_name, student_id=000):
        model.student.Student.__init__(self, name, last_name, student_id)

    def get_school_name(self):
        return "This is a high school student"

    def get_name_capitalized(self):
        return super().get_name_capitalized() + "-HS"
