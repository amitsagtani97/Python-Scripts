# Importing important modules required in making of News Machine
import os
import bs4
from bs4 import BeautifulSoup
import time
import requests
import notify2


#Infinite loop for unlimited news :p
notify2.init("News")


#This function looks for a user answer of ny or india and then returns the headlines for that news service. 
def newsreader(source):
	if source == 'india':
		india_page = requests.get("http://timesofindia.indiatimes.com/")
		india_soup = BeautifulSoup(india_page.content, "html.parser")
		india_headlines = india_soup.find(id="lateststories")
		india_topstories = india_headlines.find_all(class_="list9")
		for x in range(len(india_topstories[0].find_all("a"))):
				news = (india_topstories[0].find_all("a")[x]).get_text().strip()
				display = notify2.Notification(news)
				display.show()
				time.sleep(12)
	elif source == 'ny':
		ny_page = requests.get("https://www.nytimes.com/section/world")
		ny_soup = BeautifulSoup(ny_page.content, "html.parser")
		ny_headlines = ny_soup.find(id="latest-panel")
		for x in ny_headlines.find_all("h2"):
				news = x.text.strip()
				display = notify2.Notification(news)
				display.show()
				time.sleep(12)
                

#Takes a users answer and grabs the headlines from the respective news service
answer = input("Please type NY for New York Times or India for India Times: ").lower()
while answer !='india' and answer != 'ny':
        answer = input("Please type NY for New York Times or India for India Times: ").lower()
        
newsreader(answer)
	
