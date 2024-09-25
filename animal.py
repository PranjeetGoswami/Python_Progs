class Animal:
    def make_sound(self):
        return "Some generic animal sound"
class Dog(Animal):
    def make_sound(self):
        return "Bhau!"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
dog = Dog()
cat = Cat()

print(dog.make_sound())
print(cat.make_sound())