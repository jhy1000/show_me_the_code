import xlwt
import json

workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('student')

with open('student.txt','r') as fd:
    json_stu = json.loads(fd.read())

row = 0
col = 0
for i in json_stu:
    worksheet.write(row,col,label = i)
    for j in json_stu[i]:
        col += 1
        worksheet.write(row,col,label = j)
    row += 1
    col = 0

workbook.save('student.xls')

