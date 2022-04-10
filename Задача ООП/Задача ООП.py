class Student:
    def __init__(self, name, surname, gender):
        self.name = name  # имя
        self.surname = surname  # фамилия
        self.gender = gender  # пол
        self.finished_courses = []  # курсы закончены
        self.courses_in_progress = []  # курсы в процессе
        self.grades = {}  # оценки

    def rate_Lecturer(self, lecturer, course, grade):

        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached and 0 <= grade <= 10:
            lecturer.rating[course].append(grade)
        else:
            return 'Ошибка'

    @property
    def get_average_grade(self) -> object:
        grade_list = []
        for course in self.courses_in_progress:
            for grade in self.grades[course]:
                grade_list += [grade]
        if len(grade_list) == 0:
            average_grade = 0
        else:
            average_grade = sum(grade_list) / len(grade_list)
        return average_grade

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.get_average_grade}\n' \
               f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
               f'Завершенные курсы: {self.finished_courses}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name  # имя
        self.surname = surname  # фамилия
        self.courses_attached = []  # курсы преподаваемые


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rating = {}

    def get_average_grade(self):
        grade_list = []
        for course in self.courses_attached:
            for grade in self.rating[course]:
                grade_list += [grade]
        if len(grade_list) == 0:
            average_grade = 0
        else:
            average_grade = sum(grade_list) / len(grade_list)
        return average_grade

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.rating}'


class Reviewer(Mentor):  # высталяют оценки за домашку.

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


best_student1 = Student('Roy', 'Eman', 'man')
best_student1.courses_in_progress += ['Python', 'Reply']
best_student1.grades = {'Python': [8, 5, 4], 'Reply': [7, 5, 3]}
best_student1.finished_courses = ['Введение в програмирование']

best_student2 = Student('Tom', 'Holland', 'man')
best_student2.courses_in_progress += ['Python']
best_student2.grades = {'Python': [3, 9]}

cool_mentor = Mentor('Tom', 'Hardy')

cool_Lecturer1 = Lecturer('Kris', 'Taker')
cool_Lecturer1.courses_attached = ['Python']
cool_Lecturer1.rating = {'Python': [3, 6]}

cool_Lecturer2 = Lecturer('Pol', 'Faker')
cool_Lecturer2.courses_attached = ['Python']
cool_Lecturer2.rating = {'Python': [5, 9]}

cool_Lecturer3 = Lecturer('Pol', 'Faker')
cool_Lecturer3.courses_attached = ['Reply']
cool_Lecturer3.rating = {'Reply': [4, 9]}

cool_Reviewer = Reviewer('Andy', 'Dene')


#  Функция для подсчета средней оценки за домашние задания по всем студентам
#  в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);

def get_av_student_hw(students, course):
    get_av_hw = []
    for student in students:
        get_av_hw += student.grades[course]
    return sum(get_av_hw) / len(get_av_hw)


print(f'Средняя оценка студентов: {get_av_student_hw([best_student1, best_student2], "Python")}')


# Функция для подсчета для подсчета средней оценки за лекции всех лекторов
# в рамках курса (в качестве аргумента принимаем список лекторов и название курса).

def get_av_lecturer(lecturers, course):
    get_av = []
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            get_av += lecturer.rating[course]
    return sum(get_av) / len(get_av)


print(f'Средняя оценка лекторов: {get_av_lecturer([cool_Lecturer1, cool_Lecturer2, cool_Lecturer3], "Python")}')
print()
print(best_student1)
print()
print(best_student2)