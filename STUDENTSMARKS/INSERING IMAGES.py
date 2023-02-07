from openpyxl import load_workbook
from openpyxl.drawing.image import Image

#lets use the hello_world spreadsheet
workbook=load_workbook(filename='C://Users/user786/Desktop/hcl.xlsx')
sheet=workbook.active

logo=Image("C://Users/user786/Desktop/1.PNG")

logo.height=150
logo.width=150

sheet.add_image(logo,"D10")
workbook.save(filename="C://Users/user786/Desktop/newsheet.xlsx")