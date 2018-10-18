import requests
import numpy as np 

max_no_of_fonts = 10
text_to_show = "Enter the text here that you would like to see"
fonts = requests.get("http://artii.herokuapp.com/fonts_list")
font_list = np.array(fonts.content.split("\n"))
chose = np.arange(0,400,1)
np.random.shuffle(chose)
selected = font_list[chose[:max_no_of_fonts]]
for font in selected:
	ascif = requests.get("http://artii.herokuapp.com/make?text="+text_to_show+"&font="+font)
	print(ascif.content)
