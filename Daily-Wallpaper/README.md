# [Daily-Wallpaper](https://github.com/udit-001/daily-wallpaper)

A python script to update desktop wallpaper on a Windows machine from a tumblr blog. For more info, [click here.](https://github.com/udit-001/daily-wallpaper)

## Inspiration
I was tired of seeing the same boring wallpaper on my desktop everyday. After learning a little bit of Python, I decided to design a script that would update my wallpaper on it's own by fetching an image from a [Tumblr Blog](http://fuckinghomepage.com/).

## Installation
Install the required dependencies/libraries by running  :

```bash
$ pip install -r requirements.txt
```

## Usage
This script can be scheduled to run daily by using the Task Scheduler utility present on Windows. You will require a BAT script to run the script from the task.

```bat
@echo off 
cd <path to wall.pyw>
pythonw wall.pyw
```

Now copy the above code and paste it into notepad, then modify the `<path to wall.pyw>` according to where you download the files from this repo, and save it as "dailywall.bat"

If you want your script to work silently in the background without having a command prompt window opening up, then you'll also need to create a .VBS script.

```vbs
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "<path to dailywall.bat>" & Chr(34), 0
Set WshShell = Nothing
```
Copy the above code and paste it into notepad, then modify the `<path to dailywall.bat>` and save it as "dailywall.vbs".  
Now add the above script in the Windows Task that you'll schedule to run daily.

## Features 
It also displays a notification on your computer when the wallpaper gets updated.

![Notifications Screenshot](https://raw.githubusercontent.com/udit-001/daily-wallpaper/master/img/notification.jpg)

## License

> You can check out the full license [here](https://github.com/udit-001/daily-wallpaper/blob/master/LICENSE)

This project is licensed under the terms of the MIT license.



