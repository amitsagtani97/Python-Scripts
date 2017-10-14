import requests
from bs4 import BeautifulSoup
import sys
from PIL import Image
import io

def func():
	arg1=int(sys.argv[1])
	arg2=sys.argv[2]
	head='https://xkcd.com/'
	next=''
	for i in range(arg1):
		code=requests.get(head+next).text
		obj=BeautifulSoup(code,"html.parser")
		comic=obj.find(id='comic').find('img')['src']
		res=requests.get("https:"+comic)
		img = Image.open(io.BytesIO(res.content))
		ans1=str(img)
		imagename=comic.split("/")
		img.save(arg2+imagename[4])
		next=obj.find('a',{'accesskey':'p'})['href'];
	
if( __name__=="__main__"):
	func();	
