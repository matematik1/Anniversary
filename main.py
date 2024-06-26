from tkinter import *
from tkinter import messagebox
import tkinter as tk
import pygame
from pygame import mixer
import webbrowser
from PIL import Image, ImageTk
from itertools import count, cycle
import random

#musik

mixer.init()
mixer.music.load('musick/musick.mp3')
nam = 0.6
mixer.music.set_volume(nam)
mixer.music.play(99)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#клас

class RandomImage:
    def __init__(self, app):
        self.app = app

        self.images = [ImageTk.PhotoImage(Image.open(f"image/img ({i}).png")) for i in range(1, 26)]

        self.image_label = tk.Label(app)
        self.image_label.pack()
        self.image_label.place(x=492, y=108.5)

        self.change_image()

    def change_image(self):
        random_image = random.choice(self.images)
        self.image_label.config(image=random_image)
        self.app.after(1333, self.change_image)


class ImageLabel(Label):
    def load(self, im):
        im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        self.frames = cycle(frames)
        self.deley = im.info['duration']

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.deley, self.next_frame)

#клас
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#функці

def open_TG():
    webbrowser.open("https://t.me/matematikUK", new=0, autoraise=True)

def open_TT():
    webbrowser.open("https://www.tiktok.com/@matematikuk", new=0, autoraise=True)

def open_GitHub():
    webbrowser.open("https://github.com/matematik1", new=0, autoraise=True)

def on_closing():
    if messagebox.askokcancel("Люблю тебе😘", "Зоходь ще як небудь!"):
        app.destroy()

#функції
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#основна приложуха

app = tk.Tk()
app.protocol("WM_DELETE_WINDOW", on_closing)
app.title ('Вітаю з Ювілеєм!')
app.geometry('963x766')
app.resizable(width=False, height=False)
app.wm_attributes("-topmost", 1)

cWidth = 963
cHeight = 766

canvas = Canvas(app, width = cWidth, height  = cHeight, bd= 0, highlightthickness=0,)
canvas.pack()

app.iconbitmap(r'image/app.ico')

image_tg = PhotoImage(file="image/tg.png")
TgButton = Button(app, text="TG", image=image_tg, command=open_TG)
TgButton_canvas = canvas.create_window(20, 720, window= TgButton, anchor= "nw")
TgButton["border"] = "0"

image_tt = PhotoImage(file="image/tt.png")
TtButton = Button(app, text="TT", image=image_tt, command=open_TT)
TtButton_canvas = canvas.create_window(60, 720, window= TtButton, anchor= "nw")
TtButton["border"] = "0"

image_github = PhotoImage(file="image/git.png")
GitHubButton = Button(app, text="GitHub", image=image_github, command=open_GitHub)
GitHubButton_canvas = canvas.create_window(100, 720, window= GitHubButton, anchor= "nw")
GitHubButton["border"] = "0"

#ocновна приложуха
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#фото

bg_fon = PhotoImage(file="image/font1.png")
canvas.create_image(0, 0, image=bg_fon, anchor="nw")

used_foto = PhotoImage(file="image/used.png")
canvas.create_image(0, 0, image=used_foto, anchor="nw")

random_photo = RandomImage(app)

anniversary_foto = PhotoImage(file="image/anniversary.png")
canvas.create_image(0, 0, image=anniversary_foto, anchor="nw")


# розмір картинок = 441x351
#фото
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Кнопка музики

#Кнопка музики
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#текст

canvas.create_text(717.5, 489.5, text="Матусю рідненьку ми раді вітати", font="Lolapeluza 18")
canvas.create_text(717.5, 519.5, text="У день ювілейний, що врешті прийшов.", font="Lolapeluza 18")
canvas.create_text(717.5, 549.5, text="Для нас ти, матусю, найкращая мати,", font="Lolapeluza 18")
canvas.create_text(717.5, 579.5, text="Твоя материнська нас гріє любов.", font="Lolapeluza 18")
canvas.create_text(717.5, 609.5, text="І ми із тобою завжди нерозлучні,", font="Lolapeluza 18")
canvas.create_text(717.5, 639.5, text="Матуся до серця всіх нас пригорне,", font="Lolapeluza 18")
canvas.create_text(717.5, 669.5, text="І буде хай в тебе все благополучно,", font="Lolapeluza 18")
canvas.create_text(717.5, 699.5, text="Для нас ти усіх, мов те сонце ясне!", font="Lolapeluza 18")

#текст
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#якась хуйня

app.mainloop()

