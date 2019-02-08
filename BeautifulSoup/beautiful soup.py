import requests
from bs4 import BeautifulSoup
import csv


ans = []
ans2 =[]
page = requests.get('https://www.goodreads.com/genres/thriller')

soup = BeautifulSoup(page.text, 'html.parser')

title_list = soup.find(class_="coverBigBox clearFloats bigBox")

title_name_list_items = title_list.find_all('img')


f = csv.writer(open('thriller-author-names.csv', 'w'))
f.writerow(['Name', 'Link'])                                

s =''
for i in title_name_list_items:
    print(i['alt'])
    s = i['alt']
    ans.append(s)

last_links = soup.find(class_="h2Container gradientHeaderContainer")
last_links.decompose()


last_links = soup.find(class_="moreLink")
last_links.decompose()

book_list = soup.find(class_="coverBigBox clearFloats bigBox")
book_list_name = book_list.find_all('a')

for j in book_list_name:
    links = 'https://www.goodreads.com' + j.get('href')
    print(links)
    #z = ''
    #z = links
    ans2.append(links)
    f.writerow([links])
    
for k in range(len(ans)):
    
    f.writerow([ans[k],ans2[k]])


#Reference - https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3