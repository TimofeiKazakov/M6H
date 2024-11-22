import math

class Figure:
    sides_count = 0
    filled = False

    def __init__(self, color, sides, filled = False):
        self.__color = color
        self.__sides = sides
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(0 <= value <= 255 and isinstance(value, int) for value in [r, g, b])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        return len(args) == self.sides_count and all(isinstance(i, (int, float)) and i > 0 for i in args)

    def get_sides(self):
        return [*self.__sides]

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides

class Circle(Figure):
    sides_count = 1
    __radius = None

    def __init__(self, color, radius, filled = False):
        super().__init__(color, radius, filled = filled)

    def get_square(self):
        radius = self.get_sides()[0]
        return math.pi * (radius ** 2)

class Triangle(Figure):
    sides_count = 3
    __height = None

    def __init__(self, color, radius, filled = False):
        super().__init__(color, radius, filled = filled)

    def get_square(self):
        return (self.side ** 2) * (3 ** 0.5) / 4

    def set_height(self):
        self.__height = self.side * (3 ** 0.5) / 2
        return self.__height

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length, filled = False):
        sides = [side_length] * 12
        super().__init__(color, sides, filled=filled)

    def get_volume(self):
        side_length = self.get_sides()[0]  
        return side_length ** 3

if __name__ == "__main__":

    circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77) # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15) # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15) # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

