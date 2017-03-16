#!/usr/bin/env python3
# For Python2 use Tkinter instead of tkinter

# Module Imports
from tkinter import *
from math import *
import random

# Layout Variables
canvasWidth  = 768
canvasHeight = 512 
padx = 2
pady = 2

# Color Variables
lightestGray = "#%02x%02x%02x" % (230, 230, 230)
lightGray    = "#%02x%02x%02x" % (200, 200, 200)
mediumGray   = "#%02x%02x%02x" % (150, 150, 150)
darkGray     = "#%02x%02x%02x" % (100, 100, 100)
darkestGray  = "#%02x%02x%02x" % ( 50,  50,  50)
colorRed     = "#%02x%02x%02x" % (250,  50,  50)
colorOrange  = "#%02x%02x%02x" % (250, 100,  50)
colorYellow  = "#%02x%02x%02x" % (255, 200,  50)
colorGreen   = "#%02x%02x%02x" % (150, 250, 230)
colorBlue    = "#%02x%02x%02x" % (230, 230, 230)
colorPurple  = "#%02x%02x%02x" % ( 30,  30, 250)
colorRandom  = "#%02x%02x%02x" % (random.randint(1, 255),
                                  random.randint(1, 255),
                                  random.randint(1, 255))

# Default Settings
brushStartColor = colorRed
widgetsBgColor  = lightGray 

# Wip
center = (canvasWidth / 2), (canvasHeight / 2)


class Application(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.radiobuttonValue = IntVar()
        self.radiobuttonValue.set(1)
        self.toolsThickness = 25
        self.rgb = brushStartColor

        self.pack()
        self.createWidgets()
        self.createWorkspace()

        master.bind('d', self.thicknessPlus)
        master.bind('a', self.thicknessMinus)
        master.bind('s', self.rotateBrush)
        master.bind('w', self.rotateBrush)
        master.bind('r', self.rainbowBrush)

    def createWidgets(self):

        self.leftFrame = Frame(self)
        self.leftFrame.pack(side=LEFT, fill=Y)

        self.labelTools = Label(self.leftFrame,
                                text = "Choose a drawing tool :")

        self.labelTools.grid(
                             row = 0, column = 0,
                             pady = pady, padx = padx,
                             sticky = NW)

        Radiobutton(self.leftFrame,
                    text = "Bamboo",
                    # bg = lightGray,
                    variable = self.radiobuttonValue,
                    value = 1).grid(padx = padx, pady = pady,
                                    row = 1, column = 0,
                                    sticky = NW,)

        Radiobutton(self.leftFrame,
                    text = "Magic #1",
                    # bg = lightGray,
                    variable = self.radiobuttonValue,
                    value = 2).grid(padx = padx, pady = pady,
                                    row = 2, column = 0,
                                    sticky = NW)

        Radiobutton(self.leftFrame,
                    text = "Box",
                    # bg = lightGray,
                    variable = self.radiobuttonValue,
                    value = 3).grid(padx = padx, pady = pady,
                                    row = 3, column = 0,
                                    sticky = NW)

        Radiobutton(self.leftFrame,
                    text = "Rainbow",
                    # bg = lightGray,
                    variable = self.radiobuttonValue,
                    value = 4).grid(padx = padx, pady = pady,
                                    row = 4, column = 0,
                                    sticky = NW)


        self.buttonDeleteAll = Button(self.leftFrame, text = "clear paper",
                                      command = self.delteAll)
        self.buttonDeleteAll.grid(padx = padx, pady = pady,
                                    row = 11, column = 0,
                                    sticky = NW)

    def createWorkspace(self):
        self.myCanvas = Canvas(self, width = 768,
                                     height = 512, 
                                     relief=FLAT, 
                                     borderwidth=0, 
                                     bg=lightGray
                                     )
        self.myCanvas.pack(side = RIGHT)
        self.myCanvas.bind("<B1-Motion>", self.draw)
        self.myCanvas.bind("<Button-1>", self.setPreviousXY)

    def setThickness(self, event):
        print(self.myScale.get())
        self.toolsThickness = self.myScale.get()

    def setColor(self):
        try:
            val1 = int(self.myEntry1.get())
            val2 = int(self.myEntry2.get())
            val3 = int(self.myEntry3.get())
            if 0 <=(val1 and val2 and val3) <= 255:              
                self.rgb = "#%02x%02x%02x" % (val1, val2, val3)
            self.myEntry1.delete(0, END)
            self.myEntry2.delete(0, END)
            self.myEntry3.delete(0, END)

        except ValueError:
            print("That's not an int!")
        # set focus to something else, not to mess with pressing keys: a,s
        self.focus()

    def setPreviousXY(self, event):
            print("now")
            self.previousX = event.x
            self.previousY = event.y

    # Drawing Tools
    def draw(self, event):

        # Bamboo
        if self.radiobuttonValue.get() == 1:
            self.myCanvas.create_polygon(
                                         ((event.x +  0) +  0),       # X1
                                         ((event.y +  0) +  0),       # Y1
                                         ((event.x + 20) +  0),       # X2
                                         ((event.y +  0) +  0),       # Y2
                                         ((event.x +  0) + 30),       # X1
                                         ((event.y +  0) + 30),       # Y1
                                         ((event.x + 20) + 60),       # X2
                                         ((event.y +  0) + 60),       # Y2
                                         ((event.x +  0) +  0),       # X1
                                         ((event.y +  0) +  0),       # Y1
                                         fill = self.rgb,
                                         outline = "black",
                                         )

        # Magic
        if self.radiobuttonValue.get() == 2:
            self.myCanvas.create_rectangle(event.x - self.toolsThickness,
                                          (event.y / 2) - self.toolsThickness,
                                          (event.x / 2) + self.toolsThickness,
                                          event.y + self.toolsThickness,
                                          fill = self.rgb 
                                          )

        # box
        if self.radiobuttonValue.get() == 3:
            self.myCanvas.create_rectangle(event.x - self.toolsThickness,
                                           event.y - self.toolsThickness,
                                           event.x + self.toolsThickness,
                                           event.y + self.toolsThickness,
                                           fill = self.rgb 
                                           )

        # box
        if self.radiobuttonValue.get() == 4:
            self.myCanvas.create_rectangle(event.x - self.toolsThickness,
                                           event.y - self.toolsThickness,
                                           event.x + self.toolsThickness,
                                           event.y + self.toolsThickness,
                                           fill = colorRandom)

    def delteAll(self):
        self.myCanvas.delete("all")

    def thicknessPlus(self, event):
        if self.toolsThickness < 25:
            self.toolsThickness += 1
            self.myScale.set(self.toolsThickness)

    def thicknessMinus(self, event):
        if 1 < self.toolsThickness:
            self.toolsThickness -= 1
            self.myScale.set(self.toolsThickness)

    def rainbowBrush(self, event):
        self.colorRandom  = "#%02x%02x%02x" % (random.randint(1, 255),
                                          random.randint(1, 255),
                                          random.randint(1, 255)) 

    def rotateBrush(self, event):
        # rotate the brush 
        print ("rotate!")

root = Tk()
root.title("Tk Calligraphy")
app = Application(root)
root.mainloop() 