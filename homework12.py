class Student:
    def __init__(self, name, groupnumber, age):
        self.name = name
        self.groupnumber = groupnumber
        self.age = age


student1 = Student('Ivan', '10A', '18')
student2 = Student('Igor', '10B', '19')
student3 = Student('Nastya', '10C', '18')
student4 = Student('Vlad', '10D', '17')
student5 = Student('Mashsa', '10E', '18')

print(student1.name)