# datatypes.py

# -------------------------------
# Basic Data Types
# -------------------------------

age: int = 25
# Output: <class 'int'>
"""
Java:
int age = 25;
"""

height: float = 5.9
# Output: <class 'float'>
"""
Java:
float height = 5.9f;
"""

name: str = "Alice"
# Output: <class 'str'>
"""
Java:
String name = "Alice";
"""

is_student: bool = True
# Output: <class 'bool'>
"""
Java:
boolean isStudent = true;
"""

# -------------------------------
# Collections
# -------------------------------

fruits: list[str] = ["apple", "banana", "cherry"]
# Output: ['apple', 'banana', 'cherry']
"""
Java:
ArrayList<String> fruits = new ArrayList<>(
    Arrays.asList("apple", "banana", "cherry"));
"""

coordinates: tuple[float, float] = (10.5, 20.3)
# Output: (10.5, 20.3)
"""
Java:
No built-in Tuple.
Use custom class or javafx.util.Pair.
"""

unique_numbers: set[int] = {1, 2, 3, 2}
# Output: {1, 2, 3}
"""
Java:
Set<Integer> uniqueNumbers = new HashSet<>(
    Arrays.asList(1, 2, 3, 2));
"""

person: dict[str, object] = {
    "name": "Bob",
    "age": 30,
    "is_employee": True
}
# Output: {'name': 'Bob', 'age': 30, 'is_employee': True}
"""
Java:
Map<String, Object> person = new HashMap<>();
person.put("name", "Bob");
person.put("age", 30);
person.put("is_employee", true);
"""
