from dataclasses import dataclass
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
@dataclass
class People():
    name:str
    num:int
    age:int=0
p=[People('steve',1,23),People('jafar',2,22),People('raju',3,25)]
data=[[p.name,p.num,p.age]for p in p]
data=[['Name','Num','Age']]+data

for d in data:
    sheet.append(d)
wb.save("C://Users/user786/Desktop/dataclass.xlsx")