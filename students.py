
class Student:

    def __init__(self, name: str, grade: str, age: int):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

    def __str__(self):
        return f'Name: {self.name}, Grade: {self.grade}, Age: {self.grade}'


if __name__ == '__main__':
    students = [
        Student('John', 'A', 15),
        Student('Jane', 'B', 25),
        Student('Dave', 'A', 18)
    ]

    print(f'Sorted studants: {sorted(students, key=lambda student: student.age)}')

    print(f'Sorted studants: {sorted(students, key=lambda student: student.age, reverse=True)}')

    for student in sorted(students, key=lambda student: student.age):
        print(f'Student: {student}')

