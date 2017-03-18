#!/usr/bin/env python3
# For Python2 use Tkinter instead of tkinter

from tkinter import *
from math import *
import random

# Layout Variables
canvasWidth = 768
canvasHeight = 512
padx = 2
pady = 2

# Color Variables
lightest_gray = "#%02x%02x%02x" % (230, 230, 230)
light_gray = "#%02x%02x%02x" % (200, 200, 200)
medium_gray = "#%02x%02x%02x" % (150, 150, 150)
dark_gray = "#%02x%02x%02x" % (100, 100, 100)
darkest_gray = "#%02x%02x%02x" % (50, 50, 50)
color_red = "#%02x%02x%02x" % (250, 50, 50)
color_orange = "#%02x%02x%02x" % (250, 100, 50)
color_yellow = "#%02x%02x%02x" % (255, 200, 50)
color_green = "#%02x%02x%02x" % (150, 250, 230)
color_blue = "#%02x%02x%02x" % (230, 230, 230)
color_purple = "#%02x%02x%02x" % (30, 30, 250)
color_random = "#%02x%02x%02x" % (random.randint(1, 255),
                                  random.randint(1, 255),
                                  random.randint(1, 255))

# Default Settings
brushStartColor = color_red
widgetsBgColor  = light_gray

# Wip
center = (canvasWidth / 2), (canvasHeight / 2)


class Application(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.radiobuttonValue = IntVar()
        self.radiobuttonValue.set(1)
        self.brush_size = 25
        self.rgb = brushStartColor

        self.pack()
        self.createWidgets()
        self.createWorkspace()



        # master.bind('d', self.thicknessPlus)
        # master.bind('a', self.thicknessMinus)
        master.bind('d', self.decrease_brush_size)
        master.bind('a', self.decrease_brush_size)
        master.bind('r', self.rainbow_brush)
        master.bind('c', self.clear_workspace)

    def createWidgets(self):

        self.leftFrame = Frame(self)
        self.leftFrame.pack(side=LEFT, fill=Y)

        self.labelTools = Label(self.leftFrame,
                                pady = 8,
                                text = "Choose a brush:     ")

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
                    text = "Bamboo +",
                    # bg = lightGray,
                    variable = self.radiobuttonValue,
                    value = 2).grid(padx = padx, pady = pady,
                                    row = 2, column = 0,
                                    sticky = NW,)

        Radiobutton(self.leftFrame,
                    text = "Magic",
                    # bg = lightGray,
                    variable = self.radiobuttonValue,
                    value = 3).grid(padx = padx, pady = pady,
                                    row = 3, column = 0,
                                    sticky = NW)

        Radiobutton(self.leftFrame,
                    text = "Box",
                    # bg = lightGray,
                    variable = self.radiobuttonValue,
                    value = 4).grid(padx = padx, pady = pady,
                                    row = 4, column = 0,
                                    sticky = NW)

        Radiobutton(self.leftFrame,
                    text = "Rainbow Box",
                    # bg = lightGray,
                    variable = self.radiobuttonValue,
                    value = 5).grid(padx = padx, pady = pady,
                                    row = 5, column = 0,
                                    sticky = NW)

    def createWorkspace(self):
        self.myCanvas = Canvas(self, width = 768,
                                     height = 512, 
                                     relief=FLAT, 
                                     borderwidth=0, 
                                     bg=light_gray
                                     )
        self.myCanvas.pack(side = RIGHT)
        self.myCanvas.bind("<B1-Motion>", self.draw)
        self.myCanvas.bind("<Button-1>", self.setPreviousXY)

    def setThickness(self, event):
        print(self.myScale.get())
        self.brush_size = self.myScale.get()

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

                                         ((event.x + 5) +  0),       # X2
                                         ((event.y + 5) +  0),       # Y2

                                         ((event.x +  0) -  25),      # X3
                                         ((event.y +  0) +  20),      # Y3

                                         ((event.x - 5) -  25),      # X4
                                         ((event.y - 5) +  20),      # Y4

                                         ((event.x +  0) +  0),       # X1
                                         ((event.y +  0) +  0),       # Y1

                                         fill = color_random,
                                         outline = "blue",
                                         )
        # Bamboo +
        if self.radiobuttonValue.get() == 2:
            self.myCanvas.create_polygon(
                                         ((event.x +  0) +  0),       # X1
                                         ((event.y +  0) +  0),       # Y1

                                         ((event.x + 5) +  0),       # X2
                                         ((event.y + 5) +  0),       # Y2

                                         ((event.x +  0) -  25),      # X3
                                         ((event.y +  0) +  70),      # Y3

                                         ((event.x - 5) -  25),      # X4
                                         ((event.y - 5) +  70),      # Y4

                                         ((event.x +  0) +  0),       # X1
                                         ((event.y +  0) +  0),       # Y1

                                         fill = "black",
                                         outline = "black",
                                         )

        # Magic
        if self.radiobuttonValue.get() == 3:
            self.myCanvas.create_rectangle(event.x - self.brush_size,
                                          (event.y / 2) - self.brush_size,
                                          (event.x / 2) + self.brush_size,
                                          event.y + self.brush_size,
                                          fill = darkGray
                                          )

        # box
        if self.radiobuttonValue.get() == 4:
            self.myCanvas.create_rectangle(event.x - self.brush_size,
                                           event.y - self.brush_size,
                                           event.x + self.brush_size,
                                           event.y + self.brush_size,
                                           fill = self.rgb 
                                           )

        # box
        if self.radiobuttonValue.get() == 5:
            self.myCanvas.create_rectangle(event.x - self.brush_size,
                                           event.y - self.brush_size,
                                           event.x + self.brush_size,
                                           event.y + self.brush_size,
                                           fill = color_random)

    def clear_workspace(self, event):
        self.myCanvas.delete("all")

    def increase_brush_size(self, event):
        if self.brush_size < 25:
            self.brush_size += 1
            self.myScale.set(self.brush_size)

    def decrease_brush_size(self, event):
        if 1 < self.brush_size:
            self.brush_size -= 1
            self.myScale.set(self.brush_size)

    def rainbow_brush(self, event):
        self.color_random  = "#%02x%02x%02x" % (random.randint(1, 255),
                                               random.randint(1, 255),
                                               random.randint(1, 255)) 

root = Tk()
root.title("Tk Calligraphy")
app = Application(root)
root.mainloop() 