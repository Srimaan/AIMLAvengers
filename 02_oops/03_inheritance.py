# Base class
class Animal:
    def speak(self) -> None:
        print("Animal speaks")

# Derived class
class Dog(Animal):
    def speak(self) -> None:
        print("Dog barks")

# Another derived class
class Cat(Animal):
    def speak(self) -> None:
        print("Cat meows")

# Test inheritance and overriding
pet1 = Dog()
pet2 = Cat()
pet1.speak()  # Output: Dog barks
pet2.speak()  # Output: Cat meows

#################################### JAVA Equivalent ##############################################

""""
class Animal {
    void speak() {
        System.out.println("Animal speaks");
    }
}

class Dog extends Animal {
    void speak() {
        System.out.println("Dog barks");
    }
}

class Cat extends Animal {
    void speak() {
        System.out.println("Cat meows");
    }
}

public class Test {
    public static void main(String[] args) {
        Animal pet1 = new Dog();
        Animal pet2 = new Cat();
        pet1.speak();
        pet2.speak();
    }
}
"""