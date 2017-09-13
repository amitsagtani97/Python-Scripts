# Importing important modules required in making of News Machine
import os
import bs4
from bs4 import BeautifulSoup
import time
import requests
import notify2
print("Hello")
#Infinite loop for unlimited news :p
notify2.init("News")
while True:
	page = requests.get("http://timesofindia.indiatimes.com/")
	soup = BeautifulSoup(page.content, "html.parser")
	headlines = soup.find(id="lateststories")
	topstories = headlines.find_all(class_="list9")
	for x in range(len(topstories[0].find_all("a"))):
		news = (topstories[0].find_all("a")[x]).get_text().strip()
		display = notify2.Notification(news)
		display.show()
		time.sleep(12)


