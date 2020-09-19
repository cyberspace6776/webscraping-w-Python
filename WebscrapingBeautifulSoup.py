import requests
from bs4 import BeautifulSoup as bsoup
import lxml
# import webbrowser

myUrl = "https://www.meetup.com/pl-PL/find/events/?allMeetups=true&radius=50&userFreeform=Wroclaw%2C+Polska&mcId=z1032109&mcName=Wroclaw%2C+PL&eventFilter=all"

# webbrowser.open(myUrl)
page_content = requests.get(myUrl)
soup = bsoup(page_content.text, 'lxml')
# print(type(soup))

filename = "meetup_links.txt"
f = open(filename, "w")
# for link in html_soup.find_all('a'):
for link in soup.find_all('a', href=True):
    if (link['href'][0] != '#'):
        f.write(str(link.get('href')) + "\n")
f.close()

filename = "meetup_list.csv"
f = open(filename, "w")

headers = "Temat Spotkania,Grupa\n"
f.write(headers)

# var0 = soup.select('.date-indicator')
var1 = soup.select('.wrapNice')
var2 = soup.select('.text--labelSecondary')

for i in range (0,10):
    # print(var2[i].text.strip() + "," + var1[i].text.strip())
    f.write(var1[i].text.strip() + "," + var2[i].text.strip() + "\n")
f.close()
