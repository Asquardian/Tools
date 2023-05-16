import pandas as pd


wb = pd.read_excel('123.xlsx') # Name of file

html = wb.to_html()
f = open('123.html','w', encoding='utf-8')
print('to html')
i = 0
while '<tr>' in html:
    html = html.replace('<th>' + str(i) + '</th>', u'')
    i = i + 1
    html = html.replace('<tr>', u'<tr itemprop="graduateJob">', 1) #item props
    html = html.replace('<td>', u'<td itemprop="eduCode">', 1)
    html = html.replace('<td>', u'<td itemprop="eduName">', 1)
    html = html.replace('<td>', u'<td itemprop="eduProf">', 1)
    html = html.replace('<td>', u'<td itemprop="v1">', 1)
    html = html.replace('<td>', u'<td itemprop="t1">', 1)
    print(i)

f.write(html)