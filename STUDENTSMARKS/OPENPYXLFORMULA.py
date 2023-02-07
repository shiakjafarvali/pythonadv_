import openpyxl
from openpyxl.utils import FORMULAE
wb=openpyxl.load_workbook("C://Users/user786/Desktop/hcl.xlsx")
sheet=wb.active
sheet["A7"]='=SUM(A1,A6)'
#wb.save("C://Users/user786/Desktop/hcl.xlsx")
wb.save("C://Users/user786/Desktop/newsheet.xlsx")
