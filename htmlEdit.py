import pandas as pd


with open('index.html', 'r', encoding='utf-8') as file:
    html = file.read().replace('\n', '')

print(html)

f = open('index2.html','w', encoding='utf-8')
print('to html')
i = 0
while '<tr class="row' in html:
    html = html.replace('<tr class="row' + str(i) + '"', u'<tr itemprop="addressPlacePrac"')
    i+=1
    print(i)

f.write(html)