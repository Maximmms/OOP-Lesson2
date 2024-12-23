from mentor import Mentor

class Lecturer(Mentor):


    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __mid_rate(self):
        rates = []
        for grade in self.grades.values():
            rates.append(sum(grade)/len(grade))
        return round(sum(rates)/len(rates), 2)

    def __str__(self):
        return (f'Имя: {self.name}'
                f'\nФамилия: {self.surname}'
                f'\nСредняя оценка за лекции: {self.__mid_rate()}')

    def show_mid_assessment(self):
        return self.__mid_rate()

    def __eq__(self, other):
        return self.__mid_rate() == other.__mid_rate()

    def __lt__(self, other):
        return self.__mid_rate() < other.__mid_rate()

    def __le__(self, other):
        return self.__mid_rate() <= other.__mid_rate()


def mid_ltr_course_assessment(lectors, course):
    sum_ = 0
    for lector in lectors:
        if course in lector.grades:
            sum_ += sum(lector.grades[course])/len(lector.grades[course])
    return sum_/len(lectors)