import pandas as pd


wb = pd.read_excel('1.xlsx') # Name of file

html = wb.to_html()
f = open('xyz.html','w', encoding='utf-8')
print('to html')
i = 0
while '<tr>' in html:
    html = html.replace('<th>' + str(i) + '</th>', u'')
    i = i + 1
    html = html.replace('<tr>', u'<tr itemprop="eduNir">', 1) #item props
    html = html.replace('<td>', u'<td itemprop="eduCode">', 1)
    html = html.replace('<td>', u'<td itemprop="eduName">', 1)
    html = html.replace('<td>', u'<td itemprop="perechenNir">', 1)
    html = html.replace('<td>', u'<td itemprop="eduProf">', 1)
    html = html.replace('<td>', u'<td itemprop="eduLevel">', 1)
    html = html.replace('<td>', u'<td itemprop="napravNir">', 1)
    html = html.replace('<td>', u'<td itemprop="resultNir">', 1)
    html = html.replace('<td>', u'<td itemprop="baseNir">', 1)
    print(i)

f.write(html)