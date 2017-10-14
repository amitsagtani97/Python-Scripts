import time
import webbrowser
i = 0
x = 3
print("The program started on " + time.ctime())
while(i < x):
  time.sleep(1800)
  print(str(i + 1) + "break is taking place on " + time.ctime())
  webbrowser.open("https://www.youtube.com/")
  time.sleep(1200)
  i = i + 1
