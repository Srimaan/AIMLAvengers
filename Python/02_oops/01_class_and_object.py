class Dog:

    name: str

    def bark(self) -> None:
        print("Woof!")

# Object creation
my_dog: Dog = Dog()
my_dog.name = "Buddy"
print(f"My dog's name is {my_dog.name}")  # Output: My dog's name is Buddy
my_dog.bark()  # Output: Woof!


#################################### JAVA Equivalent ##############################################

"""
public class Dog {
    String name;

    void bark() {
        System.out.println("Woof!");
    }

    public static void main(String[] args) {
        Dog myDog = new Dog();
        myDog.name = "Buddy";
        System.out.println("My dog's name is " + myDog.name);
        myDog.bark();
    }
}
"""