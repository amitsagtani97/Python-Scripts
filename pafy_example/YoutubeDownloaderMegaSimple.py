# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 19:16:31 2018

Links:
https://github.com/amitsagtani97/Python-Scripts/blob/6d5964d0134e4b6994f7f67459d4c6c81c73770e/Youtube-Downloader/down.py    

https://pythonhosted.org/pafy/#stream-lists

https://github.com/mps-youtube/pafy
https://www.geeksforgeeks.org/youtube-mediaaudio-download-using-python-pafy/

"""

#%%
import pafy
#%%
plurl='https://www.youtube.com/playlist?list=PL21F4788EBF186DC0' # Pumuckl
plurl='https://www.youtube.com/playlist?list=PLQrsocOZ_VCmc6WE4QHNpG-PTN4TgS6-7' # Eisbär Affe & Co (todo)
playlist = pafy.get_playlist(plurl)
#%%
for i in range(22,len(playlist['items'])):
    #%%
    pstream=playlist['items'][i]['pafy'].getbest()
    pstream.download(filepath="C:/tmp")
    
#%%
print("ready")

#%% Musik Download
plurl='https://www.youtube.com/playlist?list=PLw-VjHDlEOgvtnnnqWlTqByAtC7tXBg6D'
folder='YoutubeMusic'
plurl='https://www.youtube.com/watch?v=9xjI5Zf6bl8&list=PLC01DA09095BEED88'
folder='Parkour'
# todo create folder automatically
playlist = pafy.get_playlist(plurl)
#%
for i in range(0,len(playlist['items'])):
    #%
    p1=playlist['items'][i]['pafy']
    #%
    p1.getbestaudio().download(filepath="C:/tmp/"+folder)
    
#%
print("ready")