def lab_1():
    a, n = list(map(int, input("Enter a n: ").split(" ")))
    result = 1
    for i in range(0, n + 1):
        result *= a - i * n

    print(f"Result: {result}")


def lab_2():
    numbers = list(map(int, input("Enter numbers: ").split(" ")))
    numbers_count = sorted([[number, numbers.count(number)] for number in set(numbers)], key=lambda x: x[1],
                           reverse=True)
    numbers_same_count = sorted([number for number in numbers_count if number[1] == numbers_count[0][1]])
    print(f"the most common: {numbers_same_count[0][0]}")


def lab_3():
    words = input("Enter words (a,b,c,d ...): ").split(",")
    print(*[word for word in words if word[0] in word[1:]])


def lab_4():
    from random import randint
    matrix = []
    n, m = 5, 6
    for i in range(n):
        matrix.append([randint(0, 9) for j in range(m)])

    for row in matrix:
        print(*row)

    lst = [el for row in matrix for el in row]
    print(f"max count element: {max(lst, key=lambda el: lst.count(el))}")
    # якщо є декілька елементів які появляються найбільшу кількість раз
    # то серед них буде обрано менший з цих елементів за значенням


def lab_5(info_about_animal: dict):
    # info_about_animal = {
    #     "zebra": {"ave_life": 20, "speed": 20, "population": 100},
    #     "lion": {"ave_life": 30, "speed": 17, "population": 50},
    #     "hyene": {"ave_life": 10, "speed": 24, "population": 70},
    #     "crocodile": {"ave_life": 23, "speed": 50, "population": 200}
    # }

    speediest_animal = sorted(info_about_animal.items(), key=lambda el: el[1]["speed"], reverse=True)[0][0]
    smallest_population = sorted(info_about_animal.items(), key=lambda el: el[1]["population"])[0][0]
    print(f"The speediest animal is {speediest_animal}")
    print(f"The smallest population has {smallest_population}")

class Rect:
    def __init__(self, width, long):
        self.__width = width
        self.__long = long

    @property
    def width(self):
        return self.__width

    @property
    def long(self):
        return self.__long

    def length_diagonal(self):
        return pow(self.__long ** 2 + self.__width ** 2, 0.5)

    def perimeter(self):
        return 2 * (self.__long + self.__width)

    def square(self):
        return self.__long * self.__width

    def __eq__(self, other):
        if (self.__width == other.__width and self.__long == other.__long) or \
                self.__width == other.__long and self.__long == other.__width:
            return True
        else:
            return False

    def __ne__(self, other):
        if (self.__width != other.__width or self.__long != other.__long) or \
                self.__width != other.__long or self.__long != other.__width:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.perimeter() < other.perimeter():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.perimeter() > other.perimeter():
            return True
        else:
            return False

    def __str__(self):
        return f"Width: {self.__width}\nLong: {self.__long}\nPerimeter: {self.perimeter()}\nSquare: {self.square()}\n"


class OperationRect:
    def __init__(self, lst_rect):
        self.__lst_rect = lst_rect

    def the_smallest_perimeter_rect(self):
        return min(self.__lst_rect)

    def sort_by_increase_square(self):
        return sorted(self.__lst_rect, key=lambda obj: obj.square())

    def square_diagonals_length(self):
        lst_square = list(filter(lambda obj: obj.width == obj.long, self.__lst_rect))
        for obj in lst_square:
            print(obj)
            obj.length_diagonal()
