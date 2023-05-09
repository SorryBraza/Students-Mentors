from students_mentors import (Student, Lecturer, Mentor, Reviewer, 
                              average_grades_lecturers, average_grades_students)

student1 = Student('Olga', 'Petrova', 'female')
student1.courses_in_progress += ['Git', 'Python']
student1.finished_courses += ['Введение в программирование']
student2 = Student('Ivan', 'Lobov', 'male')
student2.courses_in_progress += ['Git', 'Python']
student2.finished_courses += ['Введение в программирование']

reviewer1 = Reviewer('Victor', 'Borisov')
reviewer1.courses_attached += ['Python']
reviewer2 = Reviewer('Evgeny', 'Savinov')
reviewer2.courses_attached += ['Git']

lecturer1 = Lecturer('Vasily', 'Gubov')
lecturer1.courses_attached += ['Python', 'Git']
lecturer2 = Lecturer('Nadezhda', 'Volosova')
lecturer2.courses_attached += ['Python', 'Git']

reviewer1._rate_hw(student1, 'Python', 10)
reviewer1._rate_hw(student1, 'Python', 9)
reviewer1._rate_hw(student1, 'Python', 8)
reviewer1._rate_hw(student2, 'Python', 8)
reviewer1._rate_hw(student2, 'Python', 9)
reviewer1._rate_hw(student2, 'Python', 9)

reviewer2._rate_hw(student1, 'Git', 9)
reviewer2._rate_hw(student1, 'Git', 10)
reviewer2._rate_hw(student1, 'Git', 8)
reviewer2._rate_hw(student2, 'Git', 7)
reviewer2._rate_hw(student2, 'Git', 10)
reviewer2._rate_hw(student2, 'Git', 9)

student1._rate_lecture(lecturer1, 'Python', 10)
student1._rate_lecture(lecturer1, 'Python', 8)
student1._rate_lecture(lecturer1, 'Python', 8)
student1._rate_lecture(lecturer1, 'Git', 9)
student1._rate_lecture(lecturer1, 'Git', 10)
student1._rate_lecture(lecturer1, 'Git', 8)

student2._rate_lecture(lecturer2, 'Python', 10)
student2._rate_lecture(lecturer2, 'Python', 9)
student2._rate_lecture(lecturer2, 'Python', 8)
student2._rate_lecture(lecturer2, 'Git', 9)
student2._rate_lecture(lecturer2, 'Git', 10)
student2._rate_lecture(lecturer2, 'Git', 9)

print(f'Данные 1-ого студента:\n{student1}\n')
print(f'Данные 2-ого студента:\n{student2}\n')

print(f'Данные 1-ого проверяющего:\n{reviewer1}\n')
print(f'Данные 2-ого проверяющего:\n{reviewer2}\n')

print(f'Данные 1-ого лектора:\n{lecturer1}\n')
print(f'Данные 2-ого лектора:\n{lecturer2}\n')

print(f'Средняя оценка за домашнее задание 1-ого студента выше, чем у 2-ого студента?'
      f'\nОтвет: {student1 > student2}\n')
print(f'Средняя оценка за лекции 1-ого лектора выше, чем у 2-ого лектора?'
      f'\nОтвет: {lecturer1 > lecturer2}\n')

print(f'Средняя оценка по всем студентам за ДЗ по курсу Python: '
      f'{average_grades_students([student1, student2], "Python")}')
print(f'Средняя оценка по всем студентам за ДЗ по курсу Git: '
      f'{average_grades_students([student1, student2], "Git")}')

print(f'Средняя оценка по всем лекторам за лекции по курсу Python: '
      f'{average_grades_lecturers([lecturer1, lecturer2], "Python")}')
print(f'Средняя оценка по всем лекторам за лекции по курсу Git: '
      f'{average_grades_lecturers([lecturer1, lecturer2], "Git")}')