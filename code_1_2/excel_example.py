
# -*- coding: utf-8 -*-
import xlrd

# 開啟既有的Excel檔，
bk = xlrd.open_workbook('excel_example.xls')
print(bk)
print('encoding:', bk.encoding)
print('There are ' + str(bk.nsheets) + ' sheets.')
print('-' * 20);

for sheet in bk.sheets():
    print(sheet.name, sheet.nrows, 'rows', sheet.ncols, 'cols')
    print()
    
    # 印cell
    if sheet.nrows:
        for r in range(sheet.nrows):
            row = sheet.row(r)
            for cell in row:
                print(cell, ' ', end='')
            print()
    print()
    
    # 印cell.value
    if sheet.nrows:
        for r in range(sheet.nrows):
            for c in range(sheet.ncols):
                cell = sheet.cell(r, c)  # 
                print(cell.value, ' ', end='')
            print()
        
    print('-' * 20)
            

