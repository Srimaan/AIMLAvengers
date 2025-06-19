class Loops:

    def __init__(self):
        print("Start Learning Loops")

#Learning For Loop
    def forLoops(self):
        for i in range(10):
            print(i)

#Learning While Loop
    def whileLoops(self):
        i = 0
        while i < 5:
            print(i)
            i += 1

#Learning For Each Loop
    names = ["Alice", "Bob", "Charlie"]
    for name in names:
        print(name)

# Loop with Index (Java:traditional, Python: enumerate)
#  enumerate() in Python gives you both index and value — super handy!
names = ["Alice", "Bob", "Charlie"]
for i, name in enumerate(names):
    print(f"{i}: {name}")



