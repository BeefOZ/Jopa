import tkinter as tk
import re

from tkinter import Label
from PIL import ImageTk, Image


class Wind(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ############ Константы
        self.geometry("800x416")
        img=self.UplImg() # Функция загрузки изображений в массив(словарь) Img
        L = Label(self, image=img['gis'])
        L.image = img['gis']
        L.pack()
        City = "Королев"
        Update = "1 час назад"

        #imag = canvas.create_image(800, 435, image=im)
        self.overrideredirect(1)
        ##############
        canvasUpdate = tk.Canvas(self, width=160, height=48, highlightthickness=0)
        canvasUpdate.create_image(400, 208, image=img['gis'])
        canvasUpdate.create_text(46, 25, font="Verdana 10", text=Update, fill="grey")
        canvas = tk.Canvas(self, width=480, height=48, highlightthickness=0 )
        canvasUpdate.pack()
        canvasUpdate.place(x=0,y=0)
        canvas.pack()
        canvas.place(x=800 / 2 - 480 / 2, y=0)
        #canvas.move(self, 0, 0 )
        canvas.bind('<1>', self.on_mouse_press)  # pressed over the widget
        # mouse is move while being held down
        canvas.bind('<B1-Motion>', self.on_drag)
        canvas.create_image(240, 25, image=img['head'])
        canvas.create_text(240, 25, font="Verdana 22", text=City, fill="grey")
        self.mainloop()



    def on_mouse_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        rect = re.fullmatch(r'\d+x\d+\+(?P<x>-?\d+)\+(?P<y>-?\d+)',
                            self.geometry()).groupdict()
        # NOTE: self.winfo_root*() is content's coordinate without window decorations
        x = int(rect['x']) + (event.x - self.start_x)
        y = int(rect['y']) + (event.y - self.start_y)
        self.wm_geometry("+%d+%d" % (x,y))

    def UplImg (self):
        #Словарь с адресами изображений
        Img = { 'gis'   : 'BG.jpg',
                'head'  : 'Head.jpg',
                'upd'   : 'Upd.jpg'}
        for nam in Img:
            image = Image.open(Img[nam])
            image.thumbnail((800,435), Image.ANTIALIAS)
            Img[nam] = ImageTk.PhotoImage(image)
        return Img
