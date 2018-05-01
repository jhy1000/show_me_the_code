import xlrd
import json
from lxml import etree


workbook = xlrd.open_workbook('city.xls')
sheet = workbook.sheet_by_name('city')

cityDict = {}
for row in range(sheet.nrows):
    rows = sheet.row_values(row)
    cityDict[rows[0]] = rows[1:]

root = etree.Element('root')
tree = etree.ElementTree(root)

child1 = etree.SubElement(root,'cities')
comment = etree.Comment(u"城市信息")

child1.append(comment)
child1.text = json.dumps(cityDict)
if '\\u' in child1.text:
    child1.text = child1.text.encode('utf-8').decode('unicode_escape')


tree.write("city.xml",pretty_print=True, xml_declaration=True, encoding='utf-8')


