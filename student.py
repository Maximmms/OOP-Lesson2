from lecturer import Lecturer

class Student:


    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        """

        Метод rate_hw позволяет выставлять оценки лекторам у класса Student
        :param lecturer: Целевой лектор
        :param course: Курс за который выставляется оценка
        :param grade: оценка за курс по 10-ти бальной шкале
        :return: Метод ничего не возвращает

        """
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __mid_hw_rate(self):
        """

        Метод для определения средней оценки за домашние задания по всем курсам
        :return: Среднюю оценку, округленную до 2-х знаков после запятой

        """
        rates = []
        for grade in self.grades.values():
            rates.append(sum(grade) / len(grade))
        return round(sum(rates) / len(rates), 2)

    def show_mid_grade(self):
        """

        Метод позволяет получить значение средней оценки за домашние задания по всем курсам
        :return: Среднюю оценку за домашние задания по всем курсам

        """
        return self.__mid_hw_rate()

    def __str__(self):
        # Переопределение магического метода __str__ в соответствии с заданием 3
        return (f'Имя: {self.name}'
            f'\nФамилия: {self.surname}'
            f'\nСредня оценка за домашнее задание: {self.__mid_hw_rate()}'
            f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
            f'\nЗавершенные курсы: {"".join(self.finished_courses)}')

    def __eq__(self, other):
        return self.__mid_hw_rate() == other.__mid_hw_rate()

    def __lt__(self, other):
        return self.__mid_hw_rate() < other.__mid_hw_rate()

    def __le__(self, other):
        return self.__mid_hw_rate() <= other.__mid_hw_rate()


def mid_course_grade(students, course):
    """

    Функция для получения средне оценки за домашнее задание по выбранному курсу
    :param students: Студент, по которому получаем расчет
    :param course: Курс
    :return: Среднюю оценку по выбранному курсу

    """
    sum_ = 0
    for student in students:
        if course in student.grades:
            sum_ += sum(student.grades[course])/len(student.grades[course])
    return sum_/len(students)