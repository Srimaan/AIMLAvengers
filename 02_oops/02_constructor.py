class Car:
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model

    def display(self) -> None:
        print(f"{self.brand} {self.model}")

car1 = Car("Toyota", "Corolla")
car1.display()  # Output: Toyota Corolla

#################################### JAVA Equivalent ##############################################

""""
public class Car {
    String brand;
    String model;

    public Car(String brand, String model) {
        this.brand = brand;
        this.model = model;
    }

    void display() {
        System.out.println(brand + " " + model);
    }

    public static void main(String[] args) {
        Car car1 = new Car("Toyota", "Corolla");
        car1.display();
    }
}
"""


# Constructor without parameters
class Bike:
    def __init__(self) -> None:
        self.brand = "Hero"
        self.model = "Splendor"

    def display(self) -> None:
        print(f"{self.brand} {self.model}")

bike1 = Bike()
bike1.display()  # Output: Hero Splendor

#################################### JAVA Equivalent ##############################################

"""
Java Equivalent:

public class Bike {
    String brand;
    String model;

    public Bike() {
        this.brand = "Hero";
        this.model = "Splendor";
    }

    void display() {
        System.out.println(brand + " " + model);
    }

    public static void main(String[] args) {
        Bike bike1 = new Bike();
        bike1.display();
    }
}
"""