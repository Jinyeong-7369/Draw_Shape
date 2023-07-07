class Shape:
    def __init__(self, size: int, symbol):
        self.size = size
        self.symbol = symbol

    def set_size(self, size: int) -> None:
        self.size = size

    def set_symbol(self, symbol) -> None:
        self.symbol = symbol

    def print_shape(self) -> None:
        pass


class Square(Shape):
    def __init__(self, size: int, symbol):
        Shape.__init__(self, size, symbol)
        self.name = "Square"

    def print_shape(self) -> None:
        for i in range(self.size):
            for j in range(self.size):
                print(self.symbol, end='  ')
            print()


class Circle(Shape):
    def __init__(self, size: int, symbol):
        Shape.__init__(self, size, symbol)
        self.name = "Circle"

    def print_shape(self) -> None:
        diameter = self.size
        offset_radius = (diameter / 2)-0.5
        for i in range(diameter):
            for j in range(diameter):
                x = i - offset_radius
                y = j - offset_radius
                if x * x + y * y <= offset_radius * offset_radius + 1:
                    print(self.symbol, end='  ')
                else:
                    print(' ', end='  ')
            print()


class Triangle(Shape):
    def __init__(self, size: int, symbol):
        Shape.__init__(self, size, symbol)
        self.name = "Triangle"

    def print_shape(self):
        height = self.size
        new_str = self.symbol + ' '
        for i in range(self.size):
            print("{s: ^{n}}".format(s=new_str, n=height*4))
            new_str += self.symbol + ' '
            new_str += self.symbol + ' '
