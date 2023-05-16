import os

arr = os.listdir('rpp/')

print(arr)
html = ''
f = open('index2.html','w', encoding='utf-8')
for i in arr:
    html += '<a href="' + i + '" target="_blank">'+ i + '</a>\n' 
f.write(html)