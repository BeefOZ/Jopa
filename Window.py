import tkinter as tk
import re, time, os

from tkinter import Label, LabelFrame, Button
from PIL import ImageTk, Image


class Wind(tk.Tk):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ############ Константы
        self.geometry("800x416+300+200")
        self.ToggSett = False
        img=self.UplImg() # Функция загрузки изображений в массив(словарь) Img
        self.BG = tk.Canvas(self, width=800, height=416, highlightthickness=0, bd=0)
        self.BG.create_image(400, 208, image=img['gis'])
        self.BG.pack()
        self.size = {'w':48, #70
                     'h':40}#100
        City = "Королев"
        Update = "1 час назад"
        self.overrideredirect(1)
        #######################
        self.Set =  LabelFrame(self, bd = 0, height=self.size["h"], width=self.size["w"], bg="#04070e")
        self.Set.place(x=800-self.size["w"],y=416-50)
        self.BG.create_image(400, 391,  image=img['bott'])
        self.quit= Button(self.Set, bd=0, highlightthickness=0, command = os.abort,
                        bg="#737375", activebackground="#40a0ca", height=30, width=30, image=img['quit'])
        self.quit.place(x=5,y=5)
        
        canvasUpdate =  tk.Canvas(self, width=160, height=48, highlightthickness=0)
        canvas =        tk.Canvas(self, width=480, height=48, highlightthickness=0)
        canvSett =      tk.Canvas(self, width=50,  height=50, highlightthickness=0, bg="#737375")
        #self.Sett = self.BG.create_image(800-self.size["w"], 416-50)
        #self.Sett = tk.Canvas(self, width=self.size['w'],  height=0, highlightbackground="#737375", highlightthickness=0, bg="#04070e")
        canvasUpdate.pack()
        canvasUpdate.place(x=0,y=0)
        canvas.pack()
        canvas.place(x=800 / 2 - 480 / 2, y=0)
        canvSett.pack()
        canvSett.place(x=750, y=368)
        canvas.bind('<1>', self.on_mouse_press)  #Чек позиции нажатия
        # Когда мышь удерживается
        canvas.bind('<B1-Motion>', self.on_drag)
        canvas.create_image(240, 25, image=img['head'])
        canvas.create_text(240, 25, font="Verdana 22", text=City, fill="grey")
        canvasUpdate.create_image(400, 208, image=img['gis'])
        canvasUpdate.create_text(46, 25, font="Verdana 10", text=Update, fill="grey")
        canvSett.create_image(25, 25, image=img['gear'])
        canvSett.bind('<1>', self.on_Sett_press)
        canvSett.bind('<Enter>', self.TurnColorON)
        canvSett.bind('<Leave>', self.TurnColorOFF)
        self.CS = canvSett

        self.mainloop()       #Визуализация всего, что написанно выше



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

    def on_Sett_press(self, event):
        if self.ToggSett:
            self.MoveSlow(self.Set, self.size['h'], 0.005)
            #self.Sett.config(height = 0)
            self.ToggSett = False
        else:
            self.MoveSlow(self.Set, -self.size['h'], 0.0014)
            #self.Sett.config(height = self.size['h'])
            self.ToggSett = True

    def MoveSlow(self, obj, to, speed):
        I=1
        if to<0: 
            I=-1
            to=-to
        Y = obj.winfo_y()
        for i in range( 0, to, 1):
            obj.place(y=Y+i*I)
            obj.update()
            time.sleep(speed)
        

    def UplImg (self):
        #Словарь с адресами изображений
        Img = { 'gis'   : 'BG.jpg',
                'head'  : 'Head.jpg',
                'upd'   : 'Upd.jpg',
                'bott'  : 'Bottom.jpg',
                'quit'  : 'Quit.png',
                'gear'  : 'Gear.png'}
        for nam in Img:
            image = Image.open(Img[nam])
            image.thumbnail((800,435), Image.ANTIALIAS)
            Img[nam] = ImageTk.PhotoImage(image)
        return Img

    def SetColor(self, canv, c1, c2):
        divider = 10                    #Делитель градации цветов(в анимации)
        c1 = [c1[1:3],c1[3:5],c1[5:]]   #color1
        c2 = [c2[1:3],c2[3:5],c2[5:]]   #color2
        for i in range(3):
            c1[i]=int(c1[i])
        for i in range(3):
            c2[i]=int(c2[i])
        cP = [-(c1[0]-c2[0])/divider,   #colorpart находит разницу и делит ее на кол-во циклов.
              -(c1[1]-c2[1])/divider,
              -(c1[2]-c2[2]) /divider]
        speed = 0.08
        for i in range(divider-1):
            calc = [c1[0]+cP[0]*(i+1),
                    c1[1]+cP[1]*(i+1),
                    c1[2]+cP[2]*(i+1)]
            for j in range(3):
                calc[j]= str(int(calc[j]))
                if len(calc[j])<2:
                    calc[j]="0"+calc[j]
            canv.config(bg="#" + calc[0]+calc[1]+calc[2])
            canv.update()
            time.sleep(speed)

    def TurnColorON(self,event):
        self.SetColor(self.CS, "#737375", "#005789")
    def TurnColorOFF(self,event):
        self.SetColor(self.CS, "#005789", "#737375")