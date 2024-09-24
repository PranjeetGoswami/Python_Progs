class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def circumference(self):
        return 2 * 3.14 * self.radius
    
circle = Circle(10)
print("Circumference:", circle.circumference())