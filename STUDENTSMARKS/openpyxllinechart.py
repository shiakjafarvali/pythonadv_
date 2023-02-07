from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference
wb=Workbook()
sheet=wb.active

sales_data=[["Years", "Sales"],
               [2010,10000],[2011,90000],[2012,20000],[2013,25000],[2014,44000]]

for row in sales_data:
    sheet.append(row)
chart=LineChart()
data=Reference(worksheet=sheet,min_row=1, max_row=6,min_col=1,max_col=2)#chartobject
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"E10")

wb.save("C://Users/user786/Desktop/Linechart.xlsx")