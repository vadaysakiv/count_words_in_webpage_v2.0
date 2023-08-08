#required modules are requests and bs4
import requests
import re
from bs4 import BeautifulSoup


PageURL = 'http://x.x.x.x:yyyy'# enter the url which you want to try on

def get_html_of(url):
    resp = requests.get(url)

    if resp.status_code != 200:
         print(f'HTTP status code of {resp.status_code} returned , but 200 is expected. exiting')
         exit(1)

    return resp.content.decode()

html=get_html_of(PageURL)
soup=BeautifulSoup(html,'html.parser')
raw_text= soup.get_text()
all_word= re.findall(r'\w+' , raw_text)

word_count = {}
for word in all_word:
    if word not in word_count:
        word_count[word]=1
    else:
        current_count =word_count.get(word)
        word_count[word]=current_count + 1
top_words = sorted(word_count.items(), key=lambda item: item[1], reverse= True)

for i in  range(10):
    print(top_words[i][0])