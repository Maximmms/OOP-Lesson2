from student import Student, mid_course_grade
from lecturer import mid_course_grade
from reviewer import Reviewer
from lecturer import Lecturer

#Создание 2-х экземпляров класса Student
student1 = Student('Victor', 'Ivanov', 'male')
student1.finished_courses = ['Git - основы']
student1.courses_in_progress = ['Go', 'C#']

student2 = Student('Max', 'Semyonov', 'male')
student2.finished_courses = ['Python для начинающих']
student2.courses_in_progress = ['C#', 'Git - основы', 'Python Fullstack-разработчик']

#Создание 2-х экземпляров класса Lecturer
lecturer1 = Lecturer('William', 'Shakespeare')
lecturer1.courses_attached = ['Git - основы', 'C#', 'Go']

lecturer2 = Lecturer('Antony', 'Hopkins')
lecturer2.courses_attached = ['C#', 'Go']

#Создание 2-х экземпляров класса Reviewer
reviewer1 = Reviewer('Emma', 'Noir')
reviewer2 = Reviewer('Helen', 'Smith')

reviewer1.rate_hw(student1, 'Go', 7)
reviewer1.rate_hw(student1, 'C#', 10)
reviewer1.rate_hw(student2, 'Git - основы', 4)
reviewer1.rate_hw(student2, 'C#', 8)
reviewer2.rate_hw(student1, 'Go', 10)
reviewer2.rate_hw(student1, 'C#', 8)
reviewer2.rate_hw(student2, 'Git - основы', 8)
reviewer2.rate_hw(student2, 'C#', 7)

student1.rate_hw(lecturer1, 'Go', 7)
student1.rate_hw(lecturer1, 'C#', 9)
student2.rate_hw(lecturer1, 'Git - основы', 10)
student2.rate_hw(lecturer1, 'C#', 5)
student1.rate_hw(lecturer2, 'Go', 7)
student1.rate_hw(lecturer2, 'C#', 9)
student2.rate_hw(lecturer2, 'Go', 10)
student2.rate_hw(lecturer2, 'C#', 5)

print(lecturer1)
print()
print(reviewer2)
print()
print(student1)
print('_' * 150)
print()

print(f'Средня оценка за домашнее задание студента {student1.name}: {student1.show_mid_grade()}')
print(f'Средня оценка за домашнее задание студента {student2.name}: {student2.show_mid_grade()}')
print()
print(f'Итог сравнения студентов оператором <= :{student1 <= student2}')
print(f'Итог сравнения студентов оператором == :{student1 == student2}')
print(f'Итог сравнения студентов оператором > :{student1 > student2}')
print()
print('_' * 150)
print()

print(f'Средня оценка за проведение лекции преподавателем {lecturer1.name} {lecturer1.surname}: {lecturer1.show_mid_grade()}')
print(f'Средня оценка за проведение лекции преподавателем {lecturer2.name} {lecturer2.surname}: {lecturer2.show_mid_grade()}')
print()
print(f'Итог сравнения лекторов оператором <= :{lecturer1 <= lecturer2}')
print(f'Итог сравнения лекторов оператором == :{lecturer1 == lecturer2}')
print(f'Итог сравнения лекторов оператором > :{lecturer1 > lecturer2}')
print()
print('_' * 150)
print()

print(f'Средняя оценка по курсу C# среди студентов : {mid_course_grade([student1, student2], "C#")}')
print(f'Средняя оценка по курсу C# среди лекторов : {mid_course_grade([lecturer1, lecturer2], "C#")}')
print('_' * 150)
print()