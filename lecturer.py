from mentor import Mentor

class Lecturer(Mentor):


    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __mid_rate(self):
        """

        Метод определения средней оценки по всем курсам
        :return: Среднюю оценку, округленную до 2-знака после запятой

        """
        rates = []
        for grade in self.grades.values():
            rates.append(sum(grade)/len(grade))
        return round(sum(rates)/len(rates), 2)

    def __str__(self):
        # Переопределение магического метода __str__ в соответствии с заданием 3
        return (f'Имя: {self.name}'
                f'\nФамилия: {self.surname}'
                f'\nСредняя оценка за лекции: {self.__mid_rate()}')

    def show_mid_grade(self):
        """

        Вывод средней оценки по всем курсам
        :return: Среднюю оценку по всем курсам

        """
        return self.__mid_rate()

    def __eq__(self, other):
        return self.__mid_rate() == other.__mid_rate()

    def __lt__(self, other):
        return self.__mid_rate() < other.__mid_rate()

    def __le__(self, other):
        return self.__mid_rate() <= other.__mid_rate()


def mid_course_grade(lectors, course):
    """

    Функция расчета средней оценки по выбранному курсу
    :param lectors: Лектор
    :param course: Курс
    :return: Среднюю оценку лектора по выбранному курсу

    """
    sum_ = 0
    for lector in lectors:
        if course in lector.grades:
            sum_ += sum(lector.grades[course])/len(lector.grades[course])
    return sum_/len(lectors)