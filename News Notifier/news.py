import requests
import os
import sys
import urllib
from bs4 import BeautifulSoup
import notify2
import time

notify2.init("News")
url = "https://khabar.ndtv.com/topic/news/news"
r = requests.get(url)
soup = BeautifulSoup(r.content,"lxml")
news_data = soup.find_all("p",{"class":"intro"})

for item in news_data:
	news = item.get_text().strip()
	display = notify2.Notification(news)
	display.show()
	time.sleep(12)
