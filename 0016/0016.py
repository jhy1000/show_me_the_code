import xlwt
import json

workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('numbers')

with open('numbers.txt','r') as fd:
    json_num = json.loads(fd.read())


row = 0
col = 0
for i in json_num:
    for j in i:
        worksheet.write(row,col,label = j)
        col += 1
    row += 1
    col = 0

workbook.save('numbers.xls')

