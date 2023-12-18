class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in student.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _str_(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия:{self.surname}\n'
                f'Средняя оценка за домашние задания: {self._aveaverage_grade_course()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы:{", ".join(self.finished_courses)})
 
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
        self.grades = {}

    def average_grade_lectors(lecturer, course):
        all_grades = []
        for lector in lecturer:
            if course in lector.grades:
                all_grades += lector.grades[course]
                if all_grades:  
                    result = sum(all_grades) / len(all_grades)
                return result
            return False

    def _str_(self):
        return f'Имя:{self.name}, Фамилия:{self.surname}'


class Reviewer(Mentor):        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _str_(self):
        return f'Имя:{self.name}, Фамилия:{self.surname}'

 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student2 = Student('Ivan', 'Ivanov', 'man')
best_student2.courses_in_progress += ['Git']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'Git']
cool_mentor2 = Mentor('Petr', 'Petrov')
cool_mentor2.courses_attached += ['Git']
 
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor2.rate_hw(best_student2, 'Git', 10)
cool_mentor2.rate_hw(best_student2, 'Git',9 )
cool_mentor2.rate_hw(best_student2, 'Git', 10)
 
print(best_student.grades)
