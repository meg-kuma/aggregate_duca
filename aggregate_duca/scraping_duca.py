from urllib import request
from bs4 import BeautifulSoup

html = request.urlopen("http://atamakayui.blog.fc2.com/blog-entry-36.html")

soup = BeautifulSoup(html,"html.parser")

body = soup.find('body')

with open('./music_name_dev.txt', 'w', encoding='utf-8') as f:
    for tbody in body.findAll('tbody')[1:]:
        for tr in tbody.findAll('tr'):
            tbs = tr.find('td')
            if tbs.string is None:
                f.write('"' + "追記" + '", ')
            else:
                f.write('"' + tbs.string + '", ')