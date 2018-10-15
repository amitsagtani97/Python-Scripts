import requests
from PIL import Image 
from StringIO import StringIO
from random import randint 

def get_urls():
	meta = requests.get("https://api.imgflip.com/get_memes")
	data = meta.json() 
	urls = [elem['url'] for elem in  data['data']['memes']]
	return urls

def get_images():
	urls = get_urls()
	img = requests.get(urls[randint(0,len(urls))])
	str_dat = StringIO(img.content)
	img_d = Image.open(str_dat)
	img_d.show()

if __name__ == '__main__':
	get_images()
