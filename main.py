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
            if course in lector.grades_lecturer:
                lector.grades_lecturer[course] += [grade]
            else:
                lector.grades_lecturer[course] = [grade]
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
        self.grades_lecturer = {}
        self.average_grades_l = 0
        Lecturer.instance_list_l.append(self)

    def average_rating(self):
        if sum([len(i) for i in self.grades_lecturer.values()]) > 0:
            result = round(sum([sum(i) for i in self.grades_lecturer.values()]) /
                           sum([len(i) for i in self.grades_lecturer.values()]), 2)
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
