# Shape Printing Library

The Shape Printing Library is a Python library that provides functionality to print different shapes, including squares, circles, and triangles, using customizable sizes and symbols.

## Classes

### Shape

The `Shape` class is the base class for all shapes. It provides the common functionality for setting the size and symbol and includes an abstract method `print_shape()` that should be implemented by each shape subclass.

#### Methods

- `__init__(self, size: int, symbol)`: Initializes a shape with the specified size and symbol.
- `set_size(self, size: int) -> None`: Sets the size of the shape.
- `set_symbol(self, symbol) -> None`: Sets the symbol used to represent the shape.
- `print_shape(self) -> None`: Prints the shape pattern.

### Square

The `Square` class represents a square shape. It inherits from the `Shape` class and provides an implementation of the `print_shape()` method specific to squares.

#### Methods

- `__init__(self, size: int, symbol)`: Initializes a square with the specified size and symbol.
- `print_shape(self) -> None`: Prints the square pattern.

### Circle

The `Circle` class represents a circular shape. It inherits from the `Shape` class and provides an implementation of the `print_shape()` method specific to circles.

#### Methods

- `__init__(self, size: int, symbol)`: Initializes a circle with the specified size and symbol.
- `print_shape(self) -> None`: Prints the circle pattern.

### Triangle

The `Triangle` class represents a triangular shape. It inherits from the `Shape` class and provides an implementation of the `print_shape()` method specific to triangles.

#### Methods

- `__init__(self, size: int, symbol)`: Initializes a triangle with the specified size and symbol.
- `print_shape(self) -> None`: Prints the triangle pattern.

## Usage

To use the Shape Printing Library, import the necessary classes and create objects of the desired shapes. Then, use the `print_shape()` method to print the shape pattern.

Example usage:

```python
from shape_printing import Square, Circle, Triangle

# Create a square shape
square = Square(5, '#')
square.print_shape()

# Create a circle shape
circle = Circle(7, '*')
circle.print_shape()

# Create a triangle shape
triangle = Triangle(4, '+')
triangle.print_shape()

# Output 
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #

    * * * *    
  * * * * * *  
* * * * * * * *
* * * * * * * *
* * * * * * * *
  * * * * * *  
    * * * *

        +
      + + +
    + + + + +
  + + + + + + +



