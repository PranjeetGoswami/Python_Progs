class Shape:
    def area(self):
        pass
class Square(Shape):
    def __init__(self,side_length):
        self.side_length = side_length
        
    def area(self):
        return self.side_length
    def area(self):
        return self.side_length **2
    
class Triangle(Shape):
    def __init__(self,base,height):
            self.base = base
            self.height = height
    def area(self):
        return 0.5*self.base*self.height
    
square = Square(4)
triangle = Triangle(3,4)

print(f"the area of the sqaure is: {square.area()}")
print(f"the area of the triangle is: {triangle.area()}")
        