import xlwt
import json

workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('city')

with open('city.txt','r') as fd:
    json_city = json.loads(fd.read())

row = 0
for index in json_city:
    worksheet.write(row,0,label = index)
    worksheet.write(row,1,label = json_city[index])
    row += 1

workbook.save('city.xls')

