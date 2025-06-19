from typing import Self

class Car:

    def __init__(self, brand:str, horsepower:int):
     self.brand = brand
     self.horsepower = horsepower


    def __str__(self) -> str:
      return f'{self.brand}, {self.horsepower}hp'

    def __repr__(self, other: Self) -> str:
        return f'{self.brand}, {other.brand}'


volvo: Car = Car('Volvo', 10)
bmw: Car = Car('BMW', 20)
print(volvo)
print(bmw)

