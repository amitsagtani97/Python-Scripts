import xlwt
import speech_recognition as sr

wb = xlwt.Workbook()

ws = wb.add_sheet("Test_sheet", True)

    #Speech Part

r = sr.Recognizer()
with sr.Microphone() as source:
    #     print("Speech recognition start")
    #     audio = r.listen(source)
    #
    # try:
    #     print("You said: " + r.recognize_google(audio))
    # except sr.UnknownValueError:
    #     print("Could not understand audio")
    # except sr.RequestError as e:
    #     print("Could not request results; {0}".format(e))

    #Speechends


    print("Enter row")
    audio = r.listen(source)
    row = r.recognize_google(audio)
    print("You said: " + r.recognize_google(audio))

    print("Enter Column")
    audio = r.listen(source)
    column = r.recognize_google(audio)
    print("You said: " + r.recognize_google(audio))

    print("Enter data")
    audio = r.listen(source)
    string = r.recognize_google(audio)

    ws.write(int(row), int(column), str(string))

    wb.save("ex1.xls")
