
# -*- coding: utf-8 -*-

import xlrd, xlwt

# 開啟既有的Excel檔，
bk = xlrd.open_workbook('excel_example.xls')
# 只拿出第0個sheet
sheet = bk.sheet_by_index(0)

print(sheet.name, sheet.nrows, 'rows', sheet.ncols, 'cols')
print()

if sheet.nrows:
    for r in range(sheet.nrows):
        for c in range(sheet.ncols):
            cell = sheet.cell(r, c)
            print(cell.value, ' ', end='')
        print()
####

# 新增workboot，將要寫入cell
bk_out = xlwt.Workbook()
# 加入一個sheet
sheet_out = bk_out.add_sheet('Sheet1')

if sheet.nrows:
    # 處理第0列
    for col_i, cell in enumerate(sheet.row(0)):
        sheet_out.write(0, col_i, cell.value)
    sheet_out.write(0, sheet.ncols, '平均')
    
    # 處理其餘的列
    for row_i in range(1, sheet.nrows):
        total = 0 # 總分
        count = 0 # 幾個分數
        for col_i, cell in enumerate(sheet.row(row_i)):
            sheet_out.write(row_i, col_i, cell.value)
            if cell.ctype == xlrd.XL_CELL_NUMBER:
                total += cell.value
                count += 1
        avg = total / count # 平均
        
        sheet_out.write(row_i, sheet.ncols, avg)
        
# 存檔，指定檔名
bk_out.save('excel_example_out.xls')


