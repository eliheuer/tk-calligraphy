# For Python2 use Tkinter instead of tkinter

# Forked from https://funpython.wordpress.com/2015/11/08/simple-drawing-program-part-1/

from tkinter import *
from random import randint

# Layout variables 
padx = 2
pady = 2

# Color variables
lightestGrey = "#%02x%02x%02x" % (230, 230, 230)
lightGray    = "#%02x%02x%02x" % (200, 200, 200)
mediumGray   = "#%02x%02x%02x" % (150, 150, 150)
darkGray     = "#%02x%02x%02x" % (100, 100, 100)
darkestGray  = "#%02x%02x%02x" % (50, 50, 50)

# Default Settings
brushStartColor = darkGray

class Application(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.radiobuttonValue = IntVar()
        self.radiobuttonValue.set(1)
        self.toolsThickness = 25
        self.rgb = brushStartColor

        self.pack()
        self.createWidgets()

        master.bind('d', self.thicknessPlus)
        master.bind('a', self.thicknessMinus)

    def createWidgets(self):
        tk_rgb = mediumGray

        self.leftFrame = Frame(self, bg = tk_rgb)
        self.leftFrame.pack(side = LEFT, fill = Y)

        self.label = Label(self.leftFrame, text = "choose a RGB color: ")
        self.label.grid(row = 0, column = 0, sticky = NW, pady = 2, padx = 3)

        #-----------------------------------------------
        self.entryFrame = Frame(self.leftFrame)
        self.entryFrame.grid(row = 1, column = 0,
                              sticky = NW, pady = pady, padx = padx)

        self.myEntry1 = Entry(self.entryFrame, width = 4, insertwidth = padx)
        self.myEntry1.pack(side = LEFT, pady = pady, padx = 4)

        self.myEntry2 = Entry(self.entryFrame, width = 4)
        self.myEntry2.pack(side = LEFT, pady = pady, padx =padx)

        self.myEntry3 = Entry(self.entryFrame, width = 4)
        self.myEntry3.pack(side = LEFT, pady = pady, padx = padx)
        #----------------------------------------------
        self.bttn1 = Button(self.leftFrame,
                            text = "Set Color", command = self.setColor)
        self.bttn1.grid(row = 2, column = 0, pady = 2, padx = 3, sticky = NW)

        self.labelThickness = Label(
                            self.leftFrame,
                            text = "drawing tools' thickness:")
        self.labelThickness.grid(row = 4,
                                 column = 0, pady = 2, padx = 3)
         
        self.myScale = Scale(
                            self.leftFrame, from_ = 1, to = 25,
                            orient = HORIZONTAL,
                            command = self.setThickness
                            )

        self.myScale.set(25)
        self.toolsThickness = 25
        self.myScale.grid(
                          row = 5, column = 0,
                          pady = 2, padx = 3, sticky = S,
                          )

        self.labelTools = Label(
                                self.leftFrame,
                                text = "chose a drawing tool:",
                                )
        self.labelTools.grid(
                             row = 6, column = 0,
                             pady = pady, padx = padx,
                             sticky = NW
                             )

        Radiobutton(self.leftFrame,
                    text = "Bamboo",
                    variable = self.radiobuttonValue,
                    value = 1).grid(padx = padx, pady = pady,
                                    row = 7, column = 0,
                                    sticky = NW
                                    )

        self.buttonDeleteAll = Button(self.leftFrame, text = "clear paper",
                                      command = self.delteAll)
        self.buttonDeleteAll.grid(padx = padx, pady = pady,
                                    row = 11, column = 0,
                                    sticky = NW)

#----------------------------------------------------------------------
        self.myCanvas = Canvas(self, width = 768,
                                height = 512, relief=FLAT, borderwidth=0, background=lightGray)
        self.myCanvas.pack(side = RIGHT)
        self.myCanvas.bind("<B1-Motion>", self.draw)
        self.myCanvas.bind("<Button-1>", self.setPreviousXY)
#----------------------------------------------------------------------

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

    def draw(self, event):
        # Bamboo
        if self.radiobuttonValue.get() == 1:
            self.myCanvas.create_rectangle(event.x - self.toolsThickness,
                                           event.y - self.toolsThickness,
                                           event.x + self.toolsThickness,
                                           event.y + self.toolsThickness,
                                           fill = self.rgb 
                                           )

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

root = Tk()
root.title("Tk Calligraphy")
app = Application(root)
root.mainloop() 