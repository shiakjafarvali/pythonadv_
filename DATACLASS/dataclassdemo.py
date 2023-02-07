from dataclasses1 import dataclass
@dataclass
class people():
    name:str
    no: int
    age: int
p=people('steve',1,28)
print(p)