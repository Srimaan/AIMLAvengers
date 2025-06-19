# datatypes.py
# Python vs Java — Data Types with Type Hints and Output

# -------------------------------
# Integer
# -------------------------------
age: int = 25
print(type(age))
# Output: <class 'int'>

"""
Java:
int age = 25;
"""

# -------------------------------
# Float
# -------------------------------
height: float = 5.9
print(type(height))
# Output: <class 'float'>

"""
Java:
float height = 5.9f;
"""

# -------------------------------
# String
# -------------------------------
name: str = "Alice"
print(type(name))
# Output: <class 'str'>

"""
Java:
String name = "Alice";
"""

# -------------------------------
# Boolean
# -------------------------------
is_student: bool = True
print(type(is_student))
# Output: <class 'bool'>

"""
Java:
boolean isStudent = true;
"""

# -------------------------------
# List (ArrayList in Java)
# -------------------------------
fruits: list[str] = ["apple", "banana", "cherry"]
print(fruits)
# Output: ['apple', 'banana', 'cherry']

"""
Java:
ArrayList<String> fruits = new ArrayList<>(
    Arrays.asList("apple", "banana", "cherry"));
"""

# -------------------------------
# Tuple (No direct Java equivalent)
# -------------------------------
coordinates: tuple[float, float] = (10.5, 20.3)
print(coordinates)
# Output: (10.5, 20.3)

"""
Java:
No built-in Tuple.
Use a custom class or Pair (from JavaFX).
"""

# -------------------------------
# Set (HashSet in Java)
# -------------------------------
unique_numbers: set[int] = {1, 2, 3, 2}
print(unique_numbers)
# Output: {1, 2, 3} — no duplicates

"""
Java:
Set<Integer> uniqueNumbers = new HashSet<>(
    Arrays.asList(1, 2, 3, 2));
"""

# -------------------------------
# Dictionary (HashMap in Java)
# -------------------------------
person: dict[str, object] = {
    "name": "Bob",
    "age": 30,
    "is_employee": True
}
print(person)
# Output: {'name': 'Bob', 'age': 30, 'is_employee': True}

"""
Java:
Map<String, Object> person = new HashMap<>();
person.put("name", "Bob");
person.put("age", 30);
person.put("is_employee", true);
"""
