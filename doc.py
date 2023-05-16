import pandas as pd
import numpy
from docx import Document


filename = '123.docx'
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

f.write(html)