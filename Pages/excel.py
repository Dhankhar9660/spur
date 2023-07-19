import openpyxl

# configure workbook path
wb = openpyxl.load_workbook("C://Users//Bal//PycharmProjects//Spurauto//Test//test-excel.xlsx")
print(type(wb))
sheet = wb.sheetnames
print(sheet)
print(type(sheet))
print(wb.active.title)
sh1 = wb["User"]
print(type(sh1))
data = sh1["B1"].value
print(data)
df = type(data)
print(df)
"""#get cell address within active sheet
cl = sht.cell (row = 3, column = 2)
#read value with cell
print("Reading value from row-3, col-2: ")
print (cl.value)"""
