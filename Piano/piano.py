import pygame
import sys
from tkinter import *

pygame.init()

def value_Cs():
    num1.set("C#")
    sound = pygame.mixer.Sound("E:\\D's Folder\\Piano\\Music_Notes\\C_s.wav")
    sound.play()
    return

def value_Ds():
    num1.set("D#")
    sound = pygame.mixer.Sound("E:\\D's Folder\\Piano\\Music_Notes\\D_s.wav")
    sound.play()
    return

def value_Fs():
    num1.set("F#")
    sound = pygame.mixer.Sound("E:\\D's Folder\\Piano\\Music_Notes\\F_s.wav")
    sound.play()
    return

def value_Gs():
    num1.set("C#")
    sound = pygame.mixer.Sound("E:\\D's Folder\\Piano\\Music_Notes\\G_s.wav")
    sound.play()
    return

def value_Bb():
    num1.set("C#")
    sound = pygame.mixer.Sound("E:\\D's Folder\\Piano\\Music_Notes\\Bb.wav")
    sound.play()
    return

def value_Cs1():
    num1.set("C#1")
    sound = pygame.mixer.Sound("E:\\D's Folder\\Piano\\Music_Notes\\C_s1.wav")
    sound.play()
    return

def value_Ds1():
    num1.set("D#1")
    sound = pygame.mixer.Sound("E:\\D's Folder\\Piano\\Music_Notes\\D_s1.wav")
    sound.play()
    return

def value_C():
    num1.set("C")
    sound = pygame.mixer.Sound("E:\\D's Folder\\Piano\\Music_Notes\\C.wav")
    sound.play()
    return

def value_D():
    num1.set("D")
    sound = pygame.mixer.Sound("E:\\D's Folder\\Piano\\Music_Notes\\D.wav")
    sound.play()
    return

def value_E():
    num1.set("E")
    sound = pygame.mixer.Sound("E:\\D's Folder\\Piano\\Music_Notes\\E.wav")
    sound.play()
    return

def value_F():
    num1.set("F")
    sound = pygame.mixer.Sound("E:\\D's Folder\\Piano\\Music_Notes\\F.wav")
    sound.play()
    return

def value_G():
    num1.set("G")
    sound = pygame.mixer.Sound("E:\\D's Folder\\Piano\\Music_Notes\\G.wav")
    sound.play()
    return

def value_A():
    num1.set("A")
    sound = pygame.mixer.Sound("E:\\D's Folder\\Piano\\Music_Notes\\A.wav")
    sound.play()
    return

def value_B():
    num1.set("B")
    sound = pygame.mixer.Sound("E:\\D's Folder\\Piano\\Music_Notes\\B.wav")
    sound.play()
    return

def value_C1():
    num1.set("C1")
    sound = pygame.mixer.Sound("E:\\D's Folder\\Piano\\Music_Notes\\C1.wav")
    sound.play()
    return

def value_D1():
    num1.set("D1")
    sound = pygame.mixer.Sound("E:\\D's Folder\\Piano\\Music_Notes\\D1.wav")
    sound.play()
    return

def value_E1():
    num1.set("E1")
    sound = pygame.mixer.Sound("E:\\D's Folder\\Piano\\Music_Notes\\E1.wav")
    sound.play()
    return

def value_F1():
    num1.set("F1")
    sound = pygame.mixer.Sound("E:\\D's Folder\\Piano\\Music_Notes\\F1.wav")
    sound.play()
    return

root = Tk()
frame = Frame(root)
frame.pack()

root.title('PIANO')

num1 = StringVar()

topframe = Frame(root)
topframe.pack(side = TOP)
txtDisplay = Entry(frame, textvariable = num1, bd = 20, insertwidth = 1, font = 30, justify = 'center', width = 4)
txtDisplay.pack(side = TOP)

button1 = Button(topframe, padx = 8, height = 6, pady = 8, bd = 8, text = "C# ", bg = "light pink", fg = "black", command = value_Cs)
button1.pack(side = LEFT)
button22 = Button(topframe, state = DISABLED, height = 7, width = 1, padx = 0, pady = 0, relief = RIDGE)
button22.pack(side = LEFT)
button2 = Button(topframe, padx = 8, height = 6, pady = 8, bd = 8, text = "D# ", bg = "light pink", fg = "black", command = value_Ds)
button2.pack(side = LEFT)
button22 = Button(topframe, state = DISABLED, height = 7, width = 1, padx = 0, pady = 0, relief = RIDGE)
button22.pack(side = LEFT)
button3 = Button(topframe, padx = 8, height = 6, pady = 8, bd = 8, text = "F# ", bg = "light pink", fg = "black", command = value_Fs)
button3.pack(side = LEFT)
button22 = Button(topframe, state = DISABLED, height = 7, width = 1, padx = 0, pady = 0, relief = RIDGE)
button22.pack(side = LEFT)

button4 = Button(topframe, padx = 8, height = 6, pady = 8, bd = 8, text = "G# ", bg = "light pink", fg = "black", command = value_Gs)
button4.pack(side = LEFT)
button22 = Button(topframe, state = DISABLED, height = 7, width = 1, padx = 0, pady = 0, relief = RIDGE)
button22.pack(side = LEFT)
button2 = Button(topframe, padx = 8, height = 6, pady = 8, bd = 8, text = "Bb ", bg = "light pink", fg = "black", command = value_Bb)
button2.pack(side = LEFT)
button22 = Button(topframe, state = DISABLED, height = 7, width = 1, padx = 0, pady = 0, relief = RIDGE)
button22.pack(side = LEFT)
button3 = Button(topframe, padx = 8, height = 6, pady = 8, bd = 8, text = "C#1 ", bg = "light pink", fg = "black", command = value_Cs1)
button3.pack(side = LEFT)
button22 = Button(topframe, state = DISABLED, height = 7, width = 1, padx = 0, pady = 0, relief = RIDGE)
button22.pack(side = LEFT)
button4 = Button(topframe, padx = 8, height = 6, pady = 8, bd = 8, text = "D#1 ", bg = "light pink", fg = "black", command = value_Ds1)
button4.pack(side = LEFT)

frame1 = Frame(root)
frame1.pack(side = TOP)

button1 = Button(frame1, padx = 16, pady = 16, bd = 8, height = 8, text = "C",bg = "light pink", fg = "black", command = value_C)
button1.pack(side = LEFT)
button2 = Button(frame1, padx = 16, pady = 16, bd = 8, height = 8, text = "D",bg = "light pink", fg = "black", command = value_D)
button2.pack(side = LEFT)
button3 = Button(frame1, padx = 16, pady = 16, bd = 8, height = 8, text = "E",bg = "light pink", fg = "black", command = value_E)
button3.pack(side = LEFT)
button4 = Button(frame1, padx = 16, pady = 16, bd = 8, height = 8, text = "F",bg = "light pink", fg = "black", command = value_F)
button4.pack(side = LEFT)
button5 = Button(frame1, padx = 16, pady = 16, bd = 8, height = 8, text = "G",bg = "light pink", fg = "black", command = value_G)
button5.pack(side = LEFT)

button6 = Button(frame1, padx = 16, pady = 16, bd = 8, height = 8, text = "A",bg = "light pink", fg = "black", command = value_A)
button6.pack(side = LEFT)
button7 = Button(frame1, padx = 16, pady = 16, bd = 8, height = 8, text = "B",bg = "light pink", fg = "black", command = value_B)
button7.pack(side = LEFT)
button8 = Button(frame1, padx = 16, pady = 16, bd = 8, height = 8, text = "C1",bg = "light pink", fg = "black", command = value_C1)
button8.pack(side = LEFT)
button9 = Button(frame1, padx = 16, pady = 16, bd = 8, height = 8, text = "D1",bg = "light pink", fg = "black", command = value_D1)
button9.pack(side = LEFT)
button10 = Button(frame1, padx = 16, pady = 16, bd = 8, height = 8, text = "E1",bg = "light pink", fg = "black", command = value_E1)
button10.pack(side = LEFT)
button11 = Button(frame1, padx = 16, pady = 16, bd = 8, height = 8, text = "F1",bg = "light pink", fg = "black", command = value_F1)
button11.pack(side = LEFT)

root.mainloop()