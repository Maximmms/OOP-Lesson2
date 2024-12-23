from mentor import Mentor
from student import Student

class Reviewer(Mentor):


    def rate_hw(self, student, course, grade):
        """

        :param student: Целевой студент
        :param course: Выбранный курс
        :param grade: Оценка за домашнее задание
        :return: Метод ничего не возвращает

        """
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        # Переопределение магического метода __str__ в соответствии с заданием 3
        return (f'Имя: {self.name}'
                f'\nФамилия: {self.surname}')