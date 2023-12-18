class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_grade(self):
        total_sum = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return round(total_sum / total_count, 1) if total_count > 0  else 0    

    def add_finished_course(self, course):
        self.finished_courses.append(course)

    def __str__(self):
        return (
            f'Имя: {self.name}\nФамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self.average_grade()}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}'
        )

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_lecturer(self, course, grade):
        if course in self.courses_attached:
            if course in self.grades:
                self.grades[course].append(grade)
            else:
                self.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        if self.grades:
            total_grades = sum(sum(grades) for grades in self.grades.values())
            total_count = sum(len(grades) for grades in self.grades.values())
            average_grade = total_grades / total_count
        else:
            average_grade = 0

        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade:.1f}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.add_finished_course('Введение в программирование')

some_reviewer = Reviewer('Ivan', 'Ivanov')
some_reviewer.courses_attached += ['Python']
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_lecturer = Lecturer('Petr', 'Petrov')
some_lecturer.courses_attached = ['Python']
some_lecturer.rate_lecturer('Python', 7)
some_lecturer.rate_lecturer('Python', 9)
some_lecturer.rate_lecturer('Python', 10)


print(some_reviewer)
print(some_lecturer)
print(some_student)