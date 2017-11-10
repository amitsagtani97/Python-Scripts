import speech_recognition as sr
import pymysql
import xlwt
import ctypes

def stot():
    r = sr.Recognizer()


    with sr.Microphone() as source:
        try:
            print("Say it!!")
            audio = r.listen(source)

            print(r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))


stot()
