import cv2
import matplotlib.pyplot as plt
import numpy as np
import time
from tkinter import *
from deepface import DeepFace

cam = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

win = Tk()
win.geometry('500x500')
win.title("ERS Visual V1.0")
Label(win, text = "ERS VISUAL V1.0\n", font = 'arial 20 bold').pack()
Label(win, text = "Emotion Recognition System", font = 'arial 20 bold').place(x = 50, y = 45)
Label(win, text = 'MENU', font = 'arial 15 bold').place(x = 210, y = 90)

def emotRegSys():
    while True:
        ret, frame = cam.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.1, 4)

        for(x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        font = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(frame, "FPS: {}".format(cam.get(cv2.CAP_PROP_FPS)), (10,30), font, 1, (0, 255, 255), 2, cv2.LINE_4) 
        cv2.putText(frame, 'Press q to quit', (200,450), font, 1, (0, 255, 255), 2, cv2.LINE_4)
        cv2.imshow("ERS Visual V1.0 - Emotion Recognition System", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    quit()

def credit():
    winCredit = Tk()
    winCredit.geometry('500x500')
    winCredit.title('ERS Visual V1.0 - Credits')

    Label(winCredit, text = "CREDITS", font = 'arial 20 bold').pack()
    Label(winCredit, text = "Created and Tested by Shavin Croos", font = 'arial 10').pack()
    

Button(win, text = 'START', font = 'arial 15', command = emotRegSys, bg = '#4dff00').place(x = 200, y = 140)
Button(win, text = 'CREDITS', font = 'arial 15', command = credit, bg = 'cyan').place(x = 188, y = 210)
Button(win, text = 'QUIT', font = 'arial 15', command = quit, bg = '#ff2626').place(x = 210, y = 280)
