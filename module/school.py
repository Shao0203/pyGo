class Classroom:

    def __init__(self, teacher, students, course):
        self.teacher = teacher
        self.students = students
        self.course = course

    def add_student(self, new_student):
        if len(self.students) < 10 and isinstance(new_student, Student):
            self.students.append(new_student)
        else:
            raise TooManyStudents

    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                break

    def change_teacher(self, new_teacher):
        self.teacher = new_teacher


class Person:

    def __init__(self, name, age=18):
        self.name = name
        self.age = age


class Teacher(Person):
    pass


class Student(Person):
    pass


class TooManyStudents(Exception):
    pass
