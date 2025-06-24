# Multiple Inheritance Example
class Flyer:
    def action(self) -> None:
        print("Flying")

class Swimmer:
    def action(self) -> None:
        print("Swimming")

class Duck(Flyer, Swimmer):
    def action(self) -> None:
        print("Duck can do both:")
        Flyer.action(self)
        Swimmer.action(self)

# Test multiple inheritance
animal = Duck()
animal.action()
# Output:
# Duck can do both:
# Flying
# Swimming

"""
Java Equivalent:

// Java does NOT support multiple class inheritance due to the Diamond Problem.
// Instead, Java uses interfaces to achieve multiple inheritance of type.

interface Flyer {
    void action();
}

interface Swimmer {
    void action();
}

class Duck implements Flyer, Swimmer {
    public void action() {
        System.out.println("Duck can do both:");
        System.out.println("Flying");
        System.out.println("Swimming");
    }
}

public class Test {
    public static void main(String[] args) {
        Duck duck = new Duck();
        duck.action();
    }
}
"""