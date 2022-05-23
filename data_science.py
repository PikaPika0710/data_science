from bs4 import BeautifulSoup
import urllib.request
import pathlib
def savetotxt(title,href,i):
  p = pathlib.Path('/content/sample_data/acticle/news'+str(i)+".txt")
  p.touch()
  page = urllib.request.urlopen(href)
  soup = BeautifulSoup(page,'html.parser')
  new_feeds = soup.findAll(class_='Normal')
  content = "\n"
  for j in new_feeds:
    content = content + j.text + "\n"
  f= open('/content/sample_data/acticle/news'+str(i)+".txt","w+")
  f.write("title:"+title+",href:"+link+",content:"+content)
  f.close()
url = 'https://vnexpress.net' #get url
page = urllib.request.urlopen(url) #open url
soup = BeautifulSoup(page, 'html.parser')
#print(soup)
new_feeds = soup.findAll(class_='title-news')
print(len(new_feeds))
i=1
for nfeed in new_feeds:
  feed = nfeed.find("a")
  title = feed.get('title')
  link = feed.get('href')
  if title==None or title=="" or link==None:
    continue
  savetotxt(title,link,i)
  i=i+1
  print('Title: {} - Link: {}'.format(title, link))
