from lecturer import Lecturer

class Student:


    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.assessment_for_homework = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __mid_assessment(self):
        return round(sum(self.assessment_for_homework)/len(self.assessment_for_homework),2)

    def show_mid_assessment(self):
        return self.__mid_assessment()

    def __str__(self):
        return (f'Имя: {self.name}'
                f'\nФамилия: {self.surname}'
                f'\nСредня оценка за домашнее задание: {self.__mid_assessment()}'
                f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
                f'\nЗавершенные курсы: {"".join(self.finished_courses)}')

    def __eq__(self, other):
        return self.__mid_assessment() == other.__mid_assessment()

    def __lt__(self, other):
        return self.__mid_assessment() < other.__mid_assessment()

    def __le__(self, other):
        return self.__mid_assessment() <= other.__mid_assessment()


def mid_std_course_assessment(students, course):
    sum_ = 0
    for student in students:
        if course in student.grades:
            sum_ += sum(student.grades[course])/len(student.grades[course])
    return sum_/len(students)