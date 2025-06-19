
from typing import Final

number: int = 10
decimal: float = 10.5
text: str = 'hello'
active: bool = True

names: list = ['Bob', 'Anna', 'Luigi'] #List
coordinates: tuple = (1.5,2.5) #Array
unique: set = {1,4,2,9} #Set
map: dict = {'name': 'Bob', 'age': 20}; #Map


VERSION: Final[str] = "1.0";  #final

#Method / funciton
def show_data() -> None:
  print(f'Greetings, {names}!');

#Method with Paramaters
def add(a:int , b:int ) -> int:
  return a + b;

