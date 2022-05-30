class Figure:
    unit = 'cm'

    def __init__(self, perimeter=0, ploshad=0):
        self.__Perimeter = perimeter
        self.__Ploshad = ploshad

    @property
    def perimeter(self, value):
        self.__Perimeter = value

    @perimeter.setter
    def perimeter(self, value):
        self.__Perimeter = value

    def calculate_area(self, a=0, h=0):
        pass

    def calculate_perimeter(self, a1=0, b1=0):
        pass

    def info(self):
        pass


class Square(Figure):

    def __init__(self, side_length):
        self.__side_length = side_length

    def __calculate_area(self):
        return f"Square: {self.__side_length * 2}"

    def __calculate_perimeter(self):
        return f"Perimeter: {self.__side_length * 4}"

    def info(self):
        print(f"SQUARE:\n"
              f"Side length: {self.__side_length}\n"
              f"Area: {self.calculate_area()}\n "
              f"{self.__calculate_perimeter()}\n")


class Rectangle(Figure):

    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        self.perimeter = self.calculate_perimeter()

    def __calculate_area(self):
        return f"Square: {self.__side_length * 2}"

    def __calculate_perimeter(self):
        return f"Perimeter: {self.__side_length * 4}"

    def info(self):
        print(f"SQUARE:\n"
              f"Length: {self.__length}\n"
              f"Width: {self.__width}\n"
              f"Area: {self.calculate_area()}\n")

kvadrat1 = Square(side_length=10)
kvadrat2 = Square(side_length=20)
pryamo_ugolnik1 = Rectangle(10, 20)
pryamo_ugolnik2 = Rectangle(20, 30)
pryamo_ugolnik3 = Rectangle(30, 40)

list1 = [kvadrat1, kvadrat2]
list2 = [pryamo_ugolnik1, pryamo_ugolnik2, pryamo_ugolnik3]

for i in list1:
    i.info()

for i in list2:
    i.info()


