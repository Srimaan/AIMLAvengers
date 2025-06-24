from abc import ABC, abstractmethod

# Abstract base class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass

# Subclass implementing abstract method
class Car(Vehicle):
    def start_engine(self) -> None:
        print("Car engine started")

# Subclass implementing abstract method
class Bike(Vehicle):
    def start_engine(self) -> None:
        print("Bike engine started")

# Instantiate and test
v1 = Car()
v2 = Bike()
v1.start_engine()  # Output: Car engine started
v2.start_engine()  # Output: Bike engine started

"""
Java Equivalent:

abstract class Vehicle {
    abstract void startEngine(); // Abstract method
}

class Car extends Vehicle {
    void startEngine() {
        System.out.println("Car engine started");
    }
}

class Bike extends Vehicle {
    void startEngine() {
        System.out.println("Bike engine started");
    }
}

public class Test {
    public static void main(String[] args) {
        Vehicle v1 = new Car();
        Vehicle v2 = new Bike();
        v1.startEngine(); // Output: Car engine started
        v2.startEngine(); // Output: Bike engine started
    }
}

// ❌ Vehicle v = new Vehicle();
// Error: Vehicle is abstract; cannot be instantiated

// Abstract classes are useful when you want to enforce method structure
// but still allow shared implementation if needed in the future.
"""
