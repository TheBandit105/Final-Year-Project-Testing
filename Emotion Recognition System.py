import cv2
import numpy as np
import time
from tkinter import *

win = Tk()
win.geometry('500x500')
win.title("ERS Visual V1.0")
Label(win, text = "ERS VISUAL V1.0\n", font = 'arial 20 bold').pack()
Label(win, text = "Emotion Recognition System", font = 'arial 20 bold').place(x = 50, y = 45)
Label(win, text = 'MENU', font = 'arial 15 bold').place(x = 210, y = 90)

def emotRegSys():
    winERS = Tk()
    winERS.geometry('500x500')
    winERS.title('ERS Visual V1.0 - ERS')
    Button(winERS, text = 'QUIT', font = 'arial 15', command = quit, bg = 'grey').place(x = 200, y = 140)

def credit():
    winCredit = Tk()
    winCredit.geometry('500x500')
    winCredit.title('ERS Visual V1.0 - Credits')

    Label(winCredit, text = "CREDITS", font = 'arial 20 bold').pack()

Button(win, text = 'START', font = 'arial 15', command = emotRegSys, bg = '#4dff00').place(x = 200, y = 140)
Button(win, text = 'CREDITS', font = 'arial 15', command = credit, bg = 'cyan').place(x = 188, y = 210)
Button(win, text = 'QUIT', font = 'arial 15', command = quit, bg = '#ff2626').place(x = 210, y = 280)
