c = lambda A,B: A+B
print (c(4,6))

n = lambda A,B: A+B

v = int(input('Введите первое число: '))
m = int(input('Введите второе число: '))

result = n(v, m)

print(result)

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def display_info(self):
        print(f"Name: {self.name}, Subject: {self.subject}")


class School:
    def __init__(self):
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def display_students(self):
        print("Students:")
        for student in self.students:
            student.display_info()

    def display_teachers(self):
        print("Teachers:")
        for teacher in self.teachers:
            teacher.display_info()

school = School()

student1 = Student("Alice", 15, 10)
student2 = Student("Bob", 16, 11)
school.add_student(student1)
school.add_student(student2)

teacher1 = Teacher("Mr. Smith", "Math")
teacher2 = Teacher("Ms. Johnson", "History")
school.add_teacher(teacher1)
school.add_teacher(teacher2)

school.display_students()
school.display_teachers()