class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades = None

    def _rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress
             and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
                lecturer._avg_grades()
            else:
                lecturer.grades[course] = [grade]
                lecturer._avg_grades()
        else:
            return 'Ошибка'            
        
    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
               f'Средняя оценка за домашнее задание: {self.average_grades}\n'
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
               f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return res
    
    def _avg_grades(self):
        self.average_grades = (round(sum(sum(v) for v in self.grades.values()) 
                                     / (sum(len(v) for v in self.grades.values())), 1))

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.average_grades < other.average_grades            

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grades = None

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {self.average_grades}')
        return res  
    
    def _avg_grades(self):
        self.average_grades = (round(sum(sum(v) for v in self.grades.values()) 
                                     / (sum(len(v) for v in self.grades.values())), 1))
        
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.average_grades < other.average_grades  


class Reviewer(Mentor):
    def _rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached 
            and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
                student._avg_grades()
            else:
                student.grades[course] = [grade]
                student._avg_grades()
        else:
            return 'Ошибка'
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
        

def average_grades_students(students, course):
    avg_grades_students, count = 0, 0
    for student in students:
        if not isinstance(student, Student):
            return 'Есть не студент'
        
    for student in students:
        if course in student.grades.keys():
            count += 1
            avg_grades_students += round(sum(v for v in student.grades[course])
                                          / len(student.grades[course]), 1)
    return round(avg_grades_students / count, 1)

def average_grades_lecturers(lecturers, course):
    avg_grades_lecturers, count = 0, 0
    for lecturer in lecturers:
        if not isinstance(lecturer, Lecturer):
            return 'Есть не лектор'
        
    for lecturer in lecturers:
        if course in lecturer.grades.keys():
            count += 1
            avg_grades_lecturers += round(sum(v for v in lecturer.grades[course])
                                           / len(lecturer.grades[course]), 1)
    return round(avg_grades_lecturers / count, 1)