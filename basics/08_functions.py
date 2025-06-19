# AIMLAvengers/basics/08_functions.py

def greet(name: str) -> None: #return type as void and input as String
    print(f"Hello, {name}!")

    # Java: void greet(String name) {
    # System.out.println("Hello, " + name);
    # }

greet("Alice")
# Output: Hello, Alice!

# Return type function
def add(a: int, b: int) -> int: #return type as int and parameters as a, b of int
    return a + b    # Java: int add(int a, int b) { return a + b; }

print(add(3, 4))
# Output: 7
