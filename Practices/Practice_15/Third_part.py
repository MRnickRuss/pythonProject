class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses:
            if course in self.grades:
                self.grades[course].append(grade)
            else:
                self.grades[course] = [grade]

    def get_avg_student(self):
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
        avg_grade = sum(sum(grades) for grades in self.grades.values()) / sum(
            len(grades) for grades in self.grades.values())
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nПол: {self.gender}\nСредняя оценка за домашние задания: {avg_grade:.1f}\n' \
               f'Курсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses = []

    def rate_student(self, student, course, grade):
        student.grades[course] = [grade]

    def add_course(self, course):
        self.courses.append(course)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}

    def rate_student(self, student, course, grade):
        if student is Student and course in student.finished_courses and course in self.courses:
            if course in self.grades:
                self.grades[course].append(grade)

    def __str__(self):
        avg_grade = sum(sum(grades) for grades in self.grades.values()) / sum(
            len(grades) for grades in self.grades.values())
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.1f}'


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
        return f"Имя: {self.name}\nФамилия: {self.surname}"


course1 = 'Git'
course2 = 'Python'
reviewer1 = Reviewer('Aleister', 'Crowley')
reviewer2 = Reviewer('Annie', 'Kerber')
lecturer1 = Lecturer('Arsene', 'Lupin')
lecturer2 = Lecturer('James', 'Moriarty')
student1 = Student('John', 'Watson', 'man')
student2 = Student('Sherlock', 'Holmes', 'man')
student1.add_courses(course1)
student2.add_courses(course2)
lecturer1.add_course(course1)
lecturer2.add_course(course2)


#Оценки лекторам и студентов
student1.grades = {course1: [5], course2: [4]}
student2.grades = {course1: [4], course2: [3]}
lecturer1.grades = {course1: [4], course2: [5]}
lecturer2.grades = {course1: [4], course2: [5]}

print(reviewer1)
print(reviewer2)
print(lecturer1)
print(lecturer2)
print(student1)
print(student2)


#для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса
def avg_student_course(students_list, course_name):
    grades = []
    for student in students_list:
        if course_name in student.grades:
            grades.extend(student.grades[course_name])
    if grades:
        return sum(grades) / len(grades)
    else:
        return 0


print(avg_student_course([student1, student2], course1))
print(avg_student_course([student1, student2], course2))


#для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список лекторов и название курса)
def avg_lecturer_course(lecturers_list, course_name):
    grades = []
    for lecturer in lecturers_list:
        if course_name in lecturer.courses:
            grades.extend(lecturer.grades[course_name])
    if grades:
        return sum(grades) / len(grades)
    else:
        return 0


print(avg_lecturer_course([lecturer1, lecturer2], course1))
print(avg_lecturer_course([lecturer1, lecturer2], course2))