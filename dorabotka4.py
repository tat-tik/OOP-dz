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


    def __lt__(self, student):
        if isinstance(student, Student):
            return self.average_grade() < student.average_grade()


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


    def average_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return round(total_grades/ total_count, 1) if total_count > 0  else 0


    def __lt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.average_grade() < lecturer.average_grade()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'


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

some_student1 = Student('Ruoy', 'Eman', 'your_gender')
some_student1.courses_in_progress += ['Python', 'Git']
some_student1.add_finished_course('Введение в программирование')

some_student2 = Student('Igor', 'Petrov', 'm')
some_student2.courses_in_progress += ['Python', 'Git', '1C']
some_student2.add_finished_course('Введение в программирование')

some_student3 = Student('Olga', 'Semenova', 'w')
some_student3.courses_in_progress += ['Python', 'Git']
some_student3.add_finished_course('Введение в программирование')

some_reviewer = Reviewer('Ivan', 'Ivanov')
some_reviewer.courses_attached += ['Python']
some_reviewer.rate_hw(some_student1, 'Python', 8)
some_reviewer.rate_hw(some_student1, 'Python', 7)
some_reviewer.rate_hw(some_student1, 'Python', 10)
some_reviewer.rate_hw(some_student2, 'Python', 10)
some_reviewer.rate_hw(some_student2, 'Python', 10)
some_reviewer.rate_hw(some_student2, 'Python', 10)
some_reviewer.rate_hw(some_student3, 'Python', 8)
some_reviewer.rate_hw(some_student3, 'Python', 9)
some_reviewer.rate_hw(some_student3, 'Python', 10)
some_lecturer1 = Lecturer('Petr', 'Petrov')
some_lecturer1.courses_attached = ['Python']
some_lecturer1.rate_lecturer('Python', 8)
some_lecturer1.rate_lecturer('Python', 9)
some_lecturer1.rate_lecturer('Python', 10)
some_lecturer2 = Lecturer('Semen', 'Semenov')
some_lecturer2.courses_attached = ['Python']
some_lecturer2.rate_lecturer('Python', 10)
some_lecturer2.rate_lecturer('Python', 10)
some_lecturer2.rate_lecturer('Python', 10)
some_lecturer3 = Lecturer('Nik', 'Name')
some_lecturer3.courses_attached = ['Python']
some_lecturer3.rate_lecturer('Python', 7)
some_lecturer3.rate_lecturer('Python', 9)
some_lecturer3.rate_lecturer('Python', 10)


print(some_reviewer)
print(some_lecturer1)
print(some_lecturer2)
print(some_lecturer3)
print(some_student1)
print(some_student2)
print(some_student3)

print(some_lecturer1 < some_lecturer2)
print(some_student1 < some_student2)


students = [some_student1, some_student2, some_student3]
def total_avg_grade(students, course):
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades.extend(student.grades[course])
            result = round(sum(all_grades) / len(all_grades),1)
        print(result)



lecturers = [some_lecturer1, some_lecturer2, some_lecturer3]
def average_grade_lecturers(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])
            result = round(sum(all_grades) / len(all_grades),1)
        print(result)
 

total_avg_grade(students, "Python")
average_grade_lecturers(lecturers, "Python")