class Student:
    instance_list_s = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades = 0
        Student.instance_list_s.append(self)

    def rate_lectors(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached \
                and 0 <= grade <= 10:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        if sum([len(i) for i in self.grades.values()]) > 0:
            result = round(sum([sum(i) for i in self.grades.values()]) /
                           sum([len(i) for i in self.grades.values()]), 2)
            self.average_grades = result
            return result

    def completion_course(self, course):
        self.finished_courses.append(course)
        self.courses_in_progress.remove(course)

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
                 f'Средняя оценка за домашние задания: {self.average_grades}\n' \
                 f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
                 f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return result

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_rating() > other.average_rating()
        print('Ошибка')
        return

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_rating() == other.average_rating()
        print('Ошибка')
        return


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    instance_list_l = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grades_l = 0
        Lecturer.instance_list_l.append(self)

    def average_rating(self):
        if sum([len(i) for i in self.grades.values()]) > 0:
            result = round(sum([sum(i) for i in self.grades.values()]) /
                           sum([len(i) for i in self.grades.values()]), 2)
            self.average_grades_l = result
            return result

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
                 f'Средняя оценка за лекции: {self.average_grades_l}'
        return result

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_rating() > other.average_rating()
        print('Ошибка')
        return

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_rating() == other.average_rating()
        print('Ошибка')
        return


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress \
                and 0 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result


one_student = Student('Настя', 'Беленькая', 'жен')
one_student.courses_in_progress += ['Java', 'Python', 'C#']
two_student = Student('Миша', 'Серый', 'муж')
two_student.courses_in_progress += ['Java', 'Python', 'C++']

one_mentor = Reviewer('Костя', 'Верёвкин')
one_mentor.courses_attached += ['Java', 'Python']
two_mentor = Reviewer('Света', 'Петровская')
two_mentor.courses_attached += ['Java', 'Python']
three_mentor = Lecturer('Оксана', 'Симонова')
three_mentor.courses_attached += ['Java', 'Python']
four_mentor = Lecturer('Гриша', 'Ветров')
four_mentor.courses_attached += ['Java', 'Python']

one_mentor.rate_hw(one_student, 'Python', 10)
one_mentor.rate_hw(one_student, 'Python', 8)
one_mentor.rate_hw(two_student, 'Python', 6)
one_mentor.rate_hw(two_student, 'Python', 8)
two_mentor.rate_hw(one_student, 'Java', 8)
two_mentor.rate_hw(one_student, 'Java', 10)
two_mentor.rate_hw(two_student, 'Java', 5)
two_mentor.rate_hw(two_student, 'Java', 7)

one_student.rate_lectors(three_mentor, 'Python', 10)
one_student.rate_lectors(three_mentor, 'Python', 8)
one_student.rate_lectors(three_mentor, 'Python', 9)
one_student.rate_lectors(three_mentor, 'Python', 9)
two_student.rate_lectors(four_mentor, 'Java', 9)
two_student.rate_lectors(four_mentor, 'Java', 8)
two_student.rate_lectors(four_mentor, 'Java', 6)
two_student.rate_lectors(four_mentor, 'Java', 5)

list_students = [one_student, two_student]
list_mentors = [one_mentor, two_mentor, three_mentor, four_mentor]

[instance.average_rating() for instance in Student.instance_list_s]
[instance.average_rating() for instance in Lecturer.instance_list_l]
# Что бы средняя оценка считалась функцией average_rating() для каждого экземпляра класса Student и Lecturer
# команды указываются после ввода студентов, менторов и оценок

one_student.completion_course('C#')
two_student.completion_course('C++')

print(one_student)
print(one_student.__gt__(two_student))
print(one_student.__eq__(two_student))
print()
print(four_mentor)
print(three_mentor.__gt__(four_mentor))
print(three_mentor.__eq__(four_mentor))
print()
print(one_mentor)
print()


def average_grade_in_subject(class_name, course):
    """
    Функция считает среднюю оценку по заданным параметрам,
    можно выбрать студентов или лекторов и предмет
    """
    list_instances = [_ for _ in globals().values() if isinstance(_, class_name)]
    list_grades = [_.grades[course] for _ in list_instances if course in _.grades.keys()]
    average_grade = sum([sum(i) for i in list_grades]) / sum([len(i) for i in list_grades])
    return f'Средняя оценка среди {class_name.__name__} по предмету {course} - {average_grade}'


print(average_grade_in_subject(Lecturer, 'Python'))
print(average_grade_in_subject(Student, 'Java'))
