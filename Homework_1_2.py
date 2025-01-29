class Student:
    def __init__(self, name: object, surname: object, gender: object) -> object:
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.student_av_grade = float()

    def rate_lecturer (self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            #как добавить и/или self.finished_courses? По ним же тоже надо оценивать?
            if course in lecturer.grade_from_student:
                lecturer.grade_from_student[course] += [grade]
            else:
                lecturer.grade_from_student[course] = [grade]
        else:
            print("Ошибка")

    def student_av_grade(self):
        sum_ = 0
        len_ = 0
        for gr in self.grades.values():
          sum_ += sum(gr)
          len_ += len(gr)
        return round(sum_ / len_, 1)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашнее задание: {self.student_av_grade}\n"
                f"Курсы в процессе изучения: {self.courses_in_progress}\n"
                f"Завершенные курсы: {self.finished_courses}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Нельзя сравнивать разныее категории!")
            return
        return self.student_av_grade() < other.student_av_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_from_student = {}
        self.lecturer_av_grade = float()

    def lecturer_av_grade (self):
        sum_grades = 0
        len_grades = 0
        for gr in self.grade_from_student.values():
          sum_grades += sum(gr)
          len_grades += len(gr)
        return round(sum_grades / len_grades, 1)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.lecturer_av_grade}")

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            print("Нельзя сравнить")
            return
        return self.lecturer_av_grade() < other.lecturer_av_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")


lecturer_1 = Lecturer('Иван', 'Иванов')
lecturer_1.courses_attached += ['Python', 'Git', 'Java']

lecturer_2 = Lecturer('Петр', 'Петров')
lecturer_2.courses_attached += ['Python', 'Git']

reviewer_1 = Reviewer('Сергей', 'Сергеев')
reviewer_1.courses_attached += ['Python', 'Java']

reviewer_2 = Reviewer('Антон', 'Антонов')
reviewer_2.courses_attached += ['Python', 'Java']

student_1 = Student("Дмитрий", "Дмитриев", "муж")
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student("Роман", "Романов", "муж")
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

student_1.rate_lecturer('lecturer_1', 'Python', 10)
student_1.rate_lecturer('lecturer_1', 'Python', 8)
student_1.rate_lecturer('lecturer_1', 'Python', 5)

student_1.rate_lecturer('lecturer_2', 'Python', 7)
# student_1.rate_lecturer('lecturer_2', 'Python', 3)
# student_1.rate_lecturer('lecturer_2', 'Python', 8)

student_2.rate_lecturer('lecturer_1', 'Python', 5)
# student_2.rate_lecturer('lecturer_1', 'Python', 10)
# student_2.rate_lecturer('lecturer_1', 'Python', 10)

student_2.rate_lecturer('lecturer_2', 'Python', 8)
# student_2.rate_lecturer('lecturer_2', 'Python', 9)
# student_2.rate_lecturer('lecturer_2', 'Python', 10)

reviewer_1.rate_hw('student_1', 'Python', 7)
# reviewer_1.rate_hw('student_1', 'Python', 4)
# reviewer_1.rate_hw('student_1', 'Python', 8)

reviewer_1.rate_hw('student_2', 'Python', 8)
# reviewer_1.rate_hw('student_2', 'Java', 7)
# reviewer_1.rate_hw('student_2', 'Java', 9)

reviewer_2.rate_hw('student_1', 'Python', 7)
# reviewer_2.rate_hw('student_1', 'Python', 4)
# reviewer_2.rate_hw('student_1', 'Python', 8)

reviewer_2.rate_hw('student_2', 'Python', 9)
# reviewer_2.rate_hw('student_2', 'Python', 7)
# reviewer_2.rate_hw('student_2', 'Python', 9)


print(student_1, f'\n')
print(lecturer_1, f'\n')
print(reviewer_1, f'\n')

# print('Сравнение людей по средним оценкам:')
# print('student_1 < student_2', student_1 < student_2)
# print('lecturer_1 > lecturer_2', lecturer_1 > lecturer_1)
# print('student_1 < lecturer_1', student_1 < lecturer_1)
# print()


student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]


def av_student_rating(student_list, course_name):
    sum_all = 0
    count_all = []
    for st in student_list:
        if st.courses_in_progress == [course_name]:
            sum_all += len(student_list[st])
            count_all.extend(st)
    return float(sum(count_all) / max(len(count_all), 1))

def av_lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = []
    for lec in lecturer_list:
        if lec.courses_attached == [course_name]:
            sum_all += len(lecturer_list[lec])
            count_all.extend(lec)
    return float(sum(count_all) / max(len(count_all), 1))


print(f"Средняя оценка по курсу за домашнее задание {'Python'}: {av_student_rating(student_list, 'Python')}\n")
print(f"Средняя оценка лектора студентами курса {'Python'}: {av_lecturer_rating(lecturer_list, 'Python')}\n")
