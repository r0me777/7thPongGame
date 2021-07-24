import tkinter
from tkinter import *  # Import everything
import math
from math import sqrt
import pygame

top = tkinter.Tk()
global xx
global hh
global r3x
global r3x1
global r3y
global r3y1
global r3x_
global r3x1_
global r3y_
global r3y1_
score1 = 0
score2 = 0
v1 = 0.2
v2 = -0.2
xx = 1100
hh = 700
L1 = 300
L2 = 200
R1 = 350
R2 = 180
B1 = 200
T1 = 250
B2 = 200
T2 = 50

pygame.mixer.init()


def sound1():
    pygame.mixer.music.load(
        "C:\\Users\ROEMEN\Desktop\\Test_Env\\Pong_Sound_Effects (mp3cut.net)(2).mp3")
    pygame.mixer.music.play(loops=1)


def sound2():
    pygame.mixer.music.load(
        "C:\\Users\ROEMEN\Desktop\\Test_Env\\Pong_Sound_Effects (mp3cut.net).mp3")
    pygame.mixer.music.play(loops=1)


def sound3():
    pygame.mixer.music.load(
        "C:\\Users\ROEMEN\\Desktop\\Test_Env\\Pong_Sound_Effects (mp3cut.net) (1).mp3")
    pygame.mixer.music.play(loops=1)


canvas = Canvas(top, width=xx, height=hh, bg="black")
canvas.pack()
rectangle3 = canvas.create_rectangle(L1, B1, R1, T1, fill="white")
rectangle = canvas.create_rectangle(L2, B2, R2, T2, fill="white")
rectangle2 = canvas.create_rectangle(900, 200, 880, 450, fill="white")
middleline = canvas.create_line(550, 0, 550, 1000, dash=(4, 1), fill="white")


#photo = PhotoImage(file="C:\\Users\\ROEMEN\\Desktop\\Test_Env\\1-Number-PNG.png")
#image = canvas.create_image(700, 1, image=photo)

r3x = canvas.coords(rectangle3)[0]
r3x1 = canvas.coords(rectangle3)[2]
r3y = canvas.coords(rectangle3)[1]
r3y1 = canvas.coords(rectangle3)[3]
r3x_ = canvas.coords(rectangle)[0]
r3x1_ = canvas.coords(rectangle)[2]
r3y_ = canvas.coords(rectangle)[1]
r3y1_ = canvas.coords(rectangle)[3]


def pressing(event):
    x = 0
    y = 0
    if event.char == "w":
        y = -50
    if canvas.coords(rectangle)[1] <= 0:
        y = 50
    if event.char == "s":
        y = 50
    if canvas.coords(rectangle)[3] >= hh:
        y = -50
    canvas.move(rectangle, x, y)
    x = 0
    y = 0
    if event.char == "o":
        y = -50
    if canvas.coords(rectangle2)[1] <= 0:
        y = 50
    if event.char == "k":
        y = 50
    if canvas.coords(rectangle2)[3] >= hh:
        y = -50
    canvas.move(rectangle2, x, y)


top.bind("<Key>", pressing)


# def pressing2(event):
#    x = 0
#    y = 0
#    if event.char == "o":
#        y = -50
#    if canvas.coords(rectangle2)[1] <= 0:
#        y = 50
#    if event.char == "k":
#        y = 50
#    if canvas.coords(rectangle2)[3] >= hh:
#        y = -50
#    canvas.move(rectangle2, x, y)


#top.bind("<Key>", pressing2)


def ballmoving(event):
    x = 0
    y = 0
    if event.char == "up":
        y = -15
    # if canvas.coords(rectangle3)[0] >= 550:
    #    x = -15
    if event.char == "down":
        y = 15
    if canvas.coords(rectangle3)[3] <= canvas.coords(rectangle3)[3] - 50:
        y = 15
    if canvas.coords(rectangle3)[1] >= canvas.coords(rectangle3)[1] + 50:
        y = -15
    canvas.move(rectangle3, x, y)

# Binding for "Key" this way only works with letters.


def movement():
    canvas.move(rectangle3, v1, 0)
    canvas.move(rectangle3, 0, v2)


def infinity():
    while True:
        yield


canvas.coords(rectangle)
for i in infinity():
    movement()
    top.update()
    if canvas.coords(rectangle3)[0] <= 0 or canvas.coords(rectangle3)[2] >= xx:
        v1 *= -1
        sound1()
    if canvas.coords(rectangle3)[1] >= hh or canvas.coords(rectangle3)[3] <= 0:
        v2 *= -1
        sound1()
    if canvas.coords(rectangle)[0] < canvas.coords(rectangle3)[2] and canvas.coords(rectangle3)[0] < canvas.coords(rectangle)[2] and canvas.coords(rectangle)[1] < canvas.coords(rectangle3)[3] and canvas.coords(rectangle3)[1] < canvas.coords(rectangle)[3]:
        v1 *= -1
        #top.bind("<Key>", pressing2)
        sound2()
    if canvas.coords(rectangle2)[0] < canvas.coords(rectangle3)[2] and canvas.coords(rectangle3)[0] < canvas.coords(rectangle2)[2] and canvas.coords(rectangle2)[1] < canvas.coords(rectangle3)[3] and canvas.coords(rectangle3)[1] < canvas.coords(rectangle2)[3]:
        v1 *= -1
        #top.bind("<Key>", pressing)
        #top.bind("<Key>", ballmoving)
        sound2()
    if canvas.coords(rectangle3)[0] <= 100:
        canvas.move(rectangle3, 400, 0)
        score2 += 1
        v1 *= -1
        #top.bind("<Key>", pressing2)
        sound3()
    if canvas.coords(rectangle3)[0] >= 1000:
        canvas.move(rectangle3, -400, 0)
        score1 += 1
        v1 *= -1
        #top.bind("<Key>", pressing)
        sound3()
print(canvas.coords(rectangle))
print(score2)
print(score1)
top.mainloop()
