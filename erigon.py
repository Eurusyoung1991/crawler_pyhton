import requests
from bs4 import BeautifulSoup

link = "https://github.com/ledgerwatch/erigon/blob/devel/cmd/rpcdaemon/README.md"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} 
r = requests.get(link, headers= headers)

soup = BeautifulSoup(r.text,"lxml")
# first_title = soup.find("h1", class_="post-title").a.text.strip()
# print ("第1篇文章的标题是：", first_title)

# title_list = soup.find_all("h1", class_="post-title")
# for i in range(len(title_list)):
#     title = title_list[i].a.text.strip()
#     print ('第 %s 篇文章的标题是：%s' %(i+1, title))
table = soup.find("table")
commands = table.tbody.find_all("tr")
for command in commands:
    text = command.find("td").text
    print(text)