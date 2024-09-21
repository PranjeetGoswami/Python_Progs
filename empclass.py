class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self.salary}")
        
emp = Employee("Pranjeet Goswami", 50000)
emp.display_info()