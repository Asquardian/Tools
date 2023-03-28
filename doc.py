import pandas as pd
import numpy
from docx import Document


filename = 'ovz.docx'
document = Document(filename)# Name of file
df_tables = []
for table in document.tables:
    df = [['' for i in range(len(table.columns))] for j in range(len(table.rows))]
    for i, row in enumerate(table.rows):
        for j, cell in enumerate(row.cells):
            if cell.text:
                df[i][j] = cell.text
    df_tables.append(pd.DataFrame(df))

wb = pd.DataFrame(df)
html = wb.to_html()
f = open('xyz.html','w', encoding='utf-8')
print('to html')
i = 0
while '<tr>' in html:
    html = html.replace('<th>' + str(i) + '</th>', u'')
    i = i + 1
    html = html.replace('<tr>', u'<tr itemprop="purposeLibr">', 1) #item props
    html = html.replace('<td>', u'<td itemprop="objName">', 1)
    html = html.replace('<td>', u'<td itemprop="objAddress">', 1)
    html = html.replace('<td>', u'<td itemprop="objSq">', 1)
    html = html.replace('<td>', u'<td itemprop="objCnt">', 1)
    html = html.replace('<td>', u'<td itemprop="objOvz">', 1)
    print(i)

f.write(html)