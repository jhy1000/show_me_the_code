import xlrd
import json
from lxml import etree


workbook = xlrd.open_workbook('numbers.xls')
sheet = workbook.sheet_by_name('numbers')

numberList = []
for row in range(sheet.nrows):
    rows = sheet.row_values(row)
    numberList.append(rows)

print(numberList)
root = etree.Element('root')
tree = etree.ElementTree(root)

child1 = etree.SubElement(root,'numbers')
comment = etree.Comment(u"数字信息")

child1.append(comment)
child1.text = json.dumps(numberList)
if '\\u' in child1.text:
    child1.text = child1.text.encode('utf-8').decode('unicode_escape')


tree.write("numbers.xml",pretty_print=True, xml_declaration=True, encoding='utf-8')


