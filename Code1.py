class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lector, course, grade_lector):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades_lector:
                lector.grades_lector[course] += [grade_lector]
            else:
                lector.grades_lector[course] = [grade_lector]
        else:
            return 'Ошибка'

    def _aveaverage_grade_course(self):
        return sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))

    def _str_(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия:{self.surname}\n'
                f'Средняя оценка за домашние задания: {self._aveaverage_grade_course()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы:{self.finished_courses}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_lector = {}


class Lecturer(Mentor):

    def _average_grade(self):
        return sum(sum(self.grades_lector.values(), [])) / len(sum(self.grades_lector.values(), []))

    def _str_(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия:{self.surname} \n'
                f'Средняя оценка за лекции: {self._average_grade()}')


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
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname}')


def _lt_(self, _average_grade):
    return self._average_grade() < _average_grade


def _lt_(self, _aveaverage_grade_course):
    return self._aveaverage_grade_course() < _aveaverage_grade_course


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']
student_2 = Student('Ivan', 'Ivanov', 'your_gender')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Введение в программирование']


cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

lector = Lecturer('Some', 'Lecturer')
lector.courses_attached += ['Python']

reviewer = Reviewer('Some', 'Reviewer')
reviewer.courses_attached += ['Python']

print(best_student.rate_lec(lector, 'Python', 9.9))
print(lector._str_())
print(reviewer._str_())


print(reviewer.rate_hw(best_student, 'Python', 9.9))
print(best_student._str_())






