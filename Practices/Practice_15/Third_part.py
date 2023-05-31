class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.courses_in_progress.append(course_name)

    def finish_course(self, course_name):
        if course_name in self.courses_in_progress:
            self.courses_in_progress.remove(course_name)
            self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses:
            if course in self.grades:
                self.grades[course].append(grade)
            else:
                self.grades[course] = [grade]

    def __float__(self):
        total_sum = 0
        count = 0
        for grades in self.grades.values():
            for grade in grades:
                total_sum += grade
                count += 1
        if len(count) == 0:
            return 'нет оценок'
        return round(total_sum / count, 2)

    def __name__(self):
        return "Student"

    def __str__(self):
        avg_grade = sum(sum(grades) for grades in self.grades.values()) / sum(
            len(grades) for grades in self.grades.values())
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nПол: {self.gender}\nСредняя оценка за домашние задания: {avg_grade:.1f}\n' \
               f'Изучаемые курсы: {courses_in_progress}\nИзученные курсы: {finished_courses}\n'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses = []

    def rate_student(self, student, course, grade):
        student.grades[course] = [grade]

    def add_course(self, course):
        self.courses.append(course)

    def __bool__(self, student):
        for course in student.courses_in_progress:
            if self.courses.__contains__(course):
                return True
        return False


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}
        self.courses = []

    def rate_st(self, student, course, grade):
        if student is Student and course in student.finished_courses and course in self.courses:
            if course in self.grades:
                self.grades[course].append(grade)

    def get_avg_lecture(self):
        total_sum = 0
        count = 0
        for grades in self.grades.values():
            for grade in grades:
                total_sum += grade
                count += 1
        if len(count) == 0:
            return 'нет оценок'
        return round(total_sum / count, 2)

    def __str__(self):
        if len(self.grades) == 0:
            return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: нет оценок\n'
        avg_grade = sum(sum(grades) for grades in self.grades.values()) / sum(
            len(grades) for grades in self.grades.values())
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.1f}\n'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)

    def rate_student(self, student, course, grade):
        if course in self.courses and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'


#средняя по ученикам
def avg_grade_st(studentsList, course):
    grades = []
    for student in studentsList:
        if course in student.grades:
            grades.extend(student.grades[course])
    if grades:
        return sum(grades) / len(grades)
    else:
        return

#средняя по лекторам
def avg_grade_lect(lecturersList, course):
    grades = []
    for lecturer in lecturersList:
        if course in lecturer.grades:
            grades.extend(lecturer.grades[course])
    if grades:
        return sum(grades) / len(grades)
    else:
        return


course1 = 'Git'
course2 = 'Python'
reviewer1 = Reviewer('Aleister', 'Crowley')
reviewer2 = Reviewer('Annie', 'Kerber')
lecturer1 = Lecturer('Arsene', 'Lupin')
lecturer2 = Lecturer('James', 'Moriarty')
student1 = Student('John', 'Watson', 'man')
student2 = Student('Sherlock', 'Holmes', 'man')
student1.add_courses(course1)
student1.add_courses(course2)
student2.add_courses(course1)
student2.add_courses(course2)
lecturer1.add_course(course1)
lecturer2.add_course(course1)
lecturer2.add_course(course2)

# Оценки лекторам и студентов
lecturer1.grades = {course1: [8], course2: [9]}
lecturer2.grades = {course1: [7], course2: [6]}
student1.grades = {course1: [9], course2: [10]}
student2.grades = {course1: [9], course2: [8]}
student1.finish_course(course1)
student2.finish_course(course2)


print(f'Проверяющий:\n{reviewer1}')
print(f'Проверяющий:\n{reviewer2}')
print(f'Лектор:\n{lecturer1}')
print(f'Лектор:\n{lecturer2}')
print(f'Студент:\n{student1}')
print(f'Студент:\n{student2}')

print(f"Лектор ведёт пары у студента:\n{lecturer2.__bool__(student1)}\n")
print(f"Лектор ведёт пары у студента:\n{lecturer1.__bool__(student1)}\n")

print(f"Cредняя оценка за курс\n{course2} студентов {student1}\n{student2}\nсоставляет: {avg_grade_st([student1, student2], course2)}\n")
print(f"Cредняя оценка за курс\n{course1} лекторов {lecturer1}\n{lecturer2}\nсоставляет: {avg_grade_lect([lecturer1, lecturer2], course1)}")
