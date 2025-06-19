# Polymorphism through method overriding and simulated overloading
class Shape:
    def draw(self) -> None:
        print("Drawing shape")

    def draw_with_name(self, shape_name: str) -> None:
        print("Drawing shape --> " + shape_name)

# Demonstrate method overriding using subclass
class Circle(Shape):
    def draw(self) -> None:
        print("Drawing circle")

class Square(Shape):
    def draw(self) -> None:
        print("Drawing square")

# Demonstrate polymorphism
shapes: list[Shape] = [Circle(), Square()]
for shape in shapes:
    shape.draw()
# Output:
# Drawing circle
# Drawing square

# Simulate overloading using a second method
s = Shape()
s.draw_with_name("circle")  # Output: Drawing shape --> circle
s.draw_with_name("square")  # Output: Drawing shape --> square

#################################### JAVA Equivalent ##############################################

"""
Java Equivalent:

class Shape {
    void draw() {
        System.out.println("Drawing shape");
    }

    void draw(String shapeName) {
        System.out.println("Drawing shape --> " + shapeName);
    }
}

class Circle extends Shape {
    void draw() {
        System.out.println("Drawing circle");
    }
}

class Square extends Shape {
    void draw() {
        System.out.println("Drawing square");
    }
}

public class Test {
    public static void main(String[] args) {
        Shape[] shapes = { new Circle(), new Square() };
        for (Shape shape : shapes) {
            shape.draw();
        }

        Shape s = new Shape();
        s.draw("circle");
        s.draw("square");
    }
}
"""