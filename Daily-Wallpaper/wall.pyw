#!python2
"""This script can be set to run daily on your computer using utilities like Windows Task Scheduler
on Windows, and it would download a wallpaper
from a blog and set it up as your wallpaper on it's own"""
import urllib
import os
import ctypes
import imghdr
from datetime import datetime
from bs4 import BeautifulSoup
import requests
from win10toast import ToastNotifier

url = 'http://fuckinghomepage.com/rss'
sourceCode = requests.get(url)
plainText = sourceCode.text
soup = BeautifulSoup(plainText, 'lxml')

data = soup.item.description.text
href = data.split('PICTURE OF THE DAY:')[1].split('href=')[1].split('target=')[0]
href = href.replace('\"', ' ').strip()

today = datetime.now()
files = os.listdir(os.getcwd())

dateString = str(today.day)+'-'+str(today.month)+'-'+str(today.year)
prev = str(today.day-1)+'-'+str(today.month)+'-'+str(today.year)

check = 0
for item in files:
    if dateString in item:
        fileName = item
        check = 1
    else:
        continue

for item in files:
    if prev in item:
        os.remove(item)
    else:
        continue

if check == 0:
    urllib.urlretrieve(href, dateString)
    ext = imghdr.what(dateString)
    path = dateString+'.'+ext
    os.rename(dateString, path)
    abspath = os.path.abspath(path)
    ctypes.windll.user32.SystemParametersInfoA(20, 0, abspath, 3)

elif check == 1:
    abspath = os.path.abspath(fileName)
    ctypes.windll.user32.SystemParametersInfoA(20, 0, abspath, 3)

print "Wallpaper set successfully."
toaster = ToastNotifier()
toaster.show_toast('Wallpaper Set!', 'Wallpaper was successfully downloaded.', \
	duration=5, icon_path='wall.ico')
