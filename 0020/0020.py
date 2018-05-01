import xlrd
import datetime
import re

workbook = xlrd.open_workbook('phone.xls')
sheet = workbook.sheet_by_name('Sheet1')

phone_time = []

for row in range(sheet.nrows):
    rows = sheet.row_values(row)

    match = re.match(r'(\d+):(\d+):(\d+)',rows[3])
    if match:
        hour = int(match.group(1))
        minute = int(match.group(2))
        second = int(match.group(3))

        phone_time.append(hour*3600+minute*60+second)

print('total communicate time: {}s'.format(sum(phone_time)))

