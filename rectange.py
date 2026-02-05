class Rectangle:
    def __init__(self , length , width):
        self.__length = length
        self.__width = width
    
    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)


r1 = Rectangle(5 , 4)
print(r1.area())
print(r1.perimeter())