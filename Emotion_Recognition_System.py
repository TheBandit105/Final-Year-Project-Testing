import cv2
import datetime
import numpy as np
from tkinter import *
from deepface import DeepFace

win = Tk()
win.geometry('500x500')
win.title("ERS Visual V1.0")
Label(win, text = "ERS VISUAL V1.0\n", font = 'arial 20 bold').pack()
Label(win, text = "Emotion Recognition System", font = 'arial 20 bold').place(x = 50, y = 45)
Label(win, text = 'MENU', font = 'arial 15 bold').place(x = 210, y = 90)

def emotRegSys():

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cam = cv2.VideoCapture(0)

    f = 0

    if not cam.isOpened():
        cam = cv2.VideoCapture(1)
    if not cam.isOpened():
        raise IOError("Error! Camera not detected or cannot access Camera! Please fix the issue and try again!")
        print("Error! Inbuilt camera not detected or cannot access inbuilt camera! Please fix the issue and try again!")
    
    while True:
        ret, frame = cam.read()
        emotRes = DeepFace.analyze(frame, actions = ['emotion'], enforce_detection = False)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.1, 5)

        for(x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        font = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(frame, 'Angry: ' + str('%.1f' % (emotRes['emotion'].get('angry'))) + '%', (10, 20), font, 0.5, (23, 212, 212), 2, cv2.LINE_4)
        cv2.putText(frame, 'Fear: ' + str('%.1f' % (emotRes['emotion'].get('fear'))) + '%', (10, 40), font, 0.5, (23, 212, 212), 2, cv2.LINE_4)
        cv2.putText(frame, 'Neutral: ' + str('%.1f' % (emotRes['emotion'].get('neutral'))) + '%', (10, 60), font, 0.5, (23, 212, 212), 2, cv2.LINE_4)
        cv2.putText(frame, 'Sad: ' + str('%.1f' % (emotRes['emotion'].get('sad'))) + '%', (10, 80), font, 0.5, (23, 212, 212), 2, cv2.LINE_4)
        cv2.putText(frame, 'Disgust: ' + str('%.1f' % (emotRes['emotion'].get('disgust'))) + '%', (10, 100), font, 0.5, (23, 212, 212), 2, cv2.LINE_4)
        cv2.putText(frame, 'Happy: ' + str('%.1f' % (emotRes['emotion'].get('happy'))) + '%', (10, 120), font, 0.5, (23, 212, 212), 2, cv2.LINE_4)
        cv2.putText(frame, 'Surprise: ' + str('%.1f' % (emotRes['emotion'].get('surprise'))) + '%', (10, 140), font, 0.5, (23, 212, 212), 2, cv2.LINE_4)

        cv2.putText(frame, "FPS: {}".format(cam.get(cv2.CAP_PROP_FPS)), (475,30), font, 1, (23, 212, 212), 2, cv2.LINE_4)

        ct = datetime.datetime.now()

        print("Frame no.: " + str(f))
        print("Time: ", ct)
        print("Angry: " + str('%.8f' % (emotRes['emotion'].get('angry'))))
        print("Fear: " + str('%.8f' % (emotRes['emotion'].get('fear'))))
        print("Neutral: " + str('%.8f' % (emotRes['emotion'].get('neutral'))))
        print("Sad: " + str('%.8f' % (emotRes['emotion'].get('sad'))))
        print("Disgust: " + str('%.8f' % (emotRes['emotion'].get('disgust'))))
        print("Happy: " + str('%.8f' % (emotRes['emotion'].get('happy'))))
        print("Surprise: " + str('%.8f' % (emotRes['emotion'].get('surprise'))))
        print("\n")

        if(emotRes['emotion'].get('angry') > 80):
            cv2.putText(frame, 'You are getting a bit too angry, please try to enjoy the game!', (75, 400), font, 0.5, (23, 212, 212), 2, cv2.LINE_4)
            print("WARNING! Anger levels detected above set threshold of 80%!\n")

        f = f + 1
        
        cv2.putText(frame, 'Press c to close', (200,450), font, 1, (23, 212, 212), 2, cv2.LINE_4)
        cv2.imshow("ERS Visual V1.0 - Emotion Recognition System", frame)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            break

    cam.release()
    cv2.destroyAllWindows()
    
def credit():
    winCredit = Tk()
    winCredit.geometry('500x500')
    winCredit.title('ERS Visual V1.0 - Credits')

    Label(winCredit, text = "CREDITS", font = 'arial 20 bold').pack()
    Label(winCredit, text = "Created and Tested by Shavin Croos", font = 'arial 15').pack()

    Label(winCredit, text = "Libraries Used: ", font = 'arial 15').pack()
    Label(winCredit, text = "OpenCV", font = 'arial 15').pack()
    Label(winCredit, text = "Deepface", font = 'arial 15').pack()
    Label(winCredit, text = "Tkinter", font = 'arial 15').pack()
    Label(winCredit, text = "DateTime", font = 'arial 15').pack()
    Label(winCredit, text = "NumPy", font = 'arial 15').pack()

def about():
    winAbout = Tk()
    winAbout.geometry('750x500')
    winAbout.title('ERS Visual V1.0 - About')

    Label(winAbout, text = "ABOUT", font = 'arial 20 bold').pack()
    Label(winAbout, text = "Click on START to start detecting the emotions\n in real-time, using your webcam of choice.", font = 'arial 15').pack()
    Label(winAbout, text = "The emotions are displayed on the top left hand corner of\n the window and shows the extent of the emotion being detected.", font = 'arial 15').pack()
    Label(winAbout, text = "100 means that this is the emotion strongly being detected\n and 0 means that the emotion isn't being detected at all.", font = 'arial 15')
    Label(winAbout, text = "To make sure this software works at its best,\n please make sure you are in a well lit area\n and that the area is free of clutter, \nespecially in the background where the camera will be pointing.", font = 'arial 15').pack()
    Label(winAbout, text = "You may adjust your sitting position\n and posture to make sure the detector is picking up on your face nicely.", font = 'arial 15').pack()
    Label(winAbout, text = "Please note that the emotions picked up \nby the detector may not always be accurate. ", font = 'arial 15').pack()
    
Button(win, text = 'START', font = 'arial 15', command = emotRegSys, bg = '#4dff00').place(x = 200, y = 140)
Button(win, text = 'ABOUT', font = 'arial 15', command = about, bg = 'yellow').place(x = 198, y = 200)
Button(win, text = 'CREDITS', font = 'arial 15', command = credit, bg = 'cyan').place(x = 188, y = 260)
