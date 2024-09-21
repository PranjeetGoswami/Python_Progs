# Person class (parent class)
class Person :
    def __init__(self,name,age,gender):
        #public attributes
        self.name = name
        self.age = age
        self.gender = gender
    
    #public method to display person details
    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")
    
    #public method to introduce the person
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old.")

#student class(child class) extending person
class Student(Person):
    def __init__(self, name, age, gender, student_id, course, year):
        #call the parent class(Person) cpnstructor to initialize inherited attributes
        super().__init__(name, age, gender)
        
        #additional attributes specific to student
        self.student_id = student_id
        self.course = course
        self.year = year
        self.__grades = [] #private attributes for storing grades
        
    #public method to display both personal and student spacific details
    def display_student_details(self): 
        self.display_details() #call parent class method to display name, age, gender
        print(f"Student ID: {self.student_id}, Course: {self.course}, Year: {self.year}")
        
    #Method to simulate studying
    def study(self):
        print(f"{self.name} is studying {self.course}")
        
    #Method to add a grade to the student's private grades list
    def add_grade(self, grade):
        if 0 <= grade <= 100: #Ensure grade is valid
            self.__grades.append(grade)
            print(f"Grade {grade} added for {self.name}.")
        else:
            print("Invalid grade. Please enter a grade between 0 and 100.")
        
    #Method to calculate the average grade
    def calculate_average(self):
        if self.__grades:
            average = sum(self.__grades) / len(self.__grades)
            print(f"{self.name}'s average grade is: {average:.2f}")
        else:
            print(f"{self.name} has no grades yet")
    
    #Overriding thw introduce method from the parent class to add student details
    def introduce(self):
        super().introduce()
        print(f"I am a {self.year} year student of {self.course}")
        
#creating an instance of the student class 
student1 = Student("Pranjeet", 20, "Male","S12345", "BCA",2)

#displaying the student details
student1.display_student_details()

#Adding some grades
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(75)

#calculate the avg grade
student1.calculate_average()        