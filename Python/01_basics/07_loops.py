# AIMLAvengers/01_basics.py/07_loops.py

# For loop
for i in range(3):
    print(i)
# Output: 0 1 2

# While loop
count = 0
while count < 3:
    print(count)
    count += 1
# Output: 0 1 2

# Break and continue
for i in range(5):
    if i == 3:
        break
    if i % 2 == 0:
        continue
    print("Odd:", i)
# Output: Odd: 1

"""
Java Equivalent:
for (int i = 0; i < 3; i++) {
    System.out.println(i);
}

int count = 0;
while (count < 3) {
    System.out.println(count);
    count++;
}

for (int i = 0; i < 5; i++) {
    if (i == 3) break;
    if (i % 2 == 0) continue;
    System.out.println("Odd: " + i);
}
"""
