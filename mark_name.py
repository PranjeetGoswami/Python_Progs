class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def is_passed(self):
        return self.marks >= 40

student = Student("venkatesh", 60)
print(f"Has {student.name} passed? {student.is_passed()}")