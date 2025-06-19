# loops.py
# Python vs Java — Loops and Control Flow with Output

# -------------------------------
# For Loop using range()
# -------------------------------

for i in range(5):
    print(f"Counting: {i}")
# Output:
# Counting: 0
# Counting: 1
# Counting: 2
# Counting: 3
# Counting: 4

"""
Java:
for (int i = 0; i < 5; i++) {
    System.out.println("Counting: " + i);
}
"""

# -------------------------------
# While Loop
# -------------------------------

count: int = 0
while count < 3:
    print("While loop:", count)
    count += 1
# Output:
# While loop: 0
# While loop: 1
# While loop: 2

"""
Java:
int count = 0;
while (count < 3) {
    System.out.println("While loop: " + count);
    count++;
}
"""

# -------------------------------
# Loop through a List
# -------------------------------

colors: list[str] = ["red", "green", "blue"]
for color in colors:
    print("Color:", color)
# Output:
# Color: red
# Color: green
# Color: blue

"""
Java:
String[] colors = {"red", "green", "blue"};
for (String color : colors) {
    System.out.println("Color: " + color);
}
"""

# -------------------------------
# Break and Continue
# -------------------------------

for num in range(10):
    if num == 5:
        break
    if num % 2 == 0:
        continue
    print("Odd number:", num)
# Output:
# Odd number: 1
# Odd number: 3

"""
Java:
for (int num = 0; num < 10; num++) {
    if (num == 5) break;
    if (num % 2 == 0) continue;
    System.out.println("Odd number: " + num);
}
"""

# -------------------------------
# Match-Case (Python 3.10+)
# -------------------------------

day: str = "Wednesday"

match day:
    case "Monday":
        print("Start of the week.")
    case "Friday":
        print("Almost weekend!")
    case "Sunday":
        print("Rest day.")
    case _:
        print("Midweek day.")
# Output:
# Midweek day.

"""
Java (Traditional Switch):
switch (day) {
    case "Monday":
        System.out.println("Start of the week.");
        break;
    case "Friday":
        System.out.println("Almost weekend!");
        break;
    case "Sunday":
        System.out.println("Rest day.");
        break;
    default:
        System.out.println("Midweek day.");
        break;
}
"""
