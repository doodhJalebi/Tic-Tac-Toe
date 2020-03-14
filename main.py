from tkinter import *
from PIL import Image, ImageTk
from math import ceil

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500


class Controller(Frame):
    def __init__(self):
        

        self.root = Tk()
        self.root.resizable(False, False)
        self.path = './img/'
        self.img_dimensions = (int(CANVAS_HEIGHT / 4), int(CANVAS_HEIGHT / 4))
        print("Image size =", self.img_dimensions)

        self.list_of_labels = []
        self.state = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]

        self.canvas = Canvas(self.root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()

        self.tick_img = Image.open(self.path + 'tick.png').resize(self.img_dimensions, Image.ANTIALIAS)
        self.cross_img = Image.open(self.path + 'cross.png').resize(self.img_dimensions, Image.ANTIALIAS)

        self.tick_photoimg = ImageTk.PhotoImage(self.tick_img)
        self.cross_photoimg = ImageTk.PhotoImage(self.cross_img)
        
        self.canvas.create_line(CANVAS_WIDTH / 3, 0, CANVAS_WIDTH / 3, CANVAS_HEIGHT)
        self.canvas.create_line(2 * CANVAS_WIDTH / 3, 0, 2 * CANVAS_WIDTH / 3, CANVAS_HEIGHT)

        self.canvas.create_line(0, CANVAS_HEIGHT / 3, CANVAS_WIDTH, CANVAS_HEIGHT / 3)
        self.canvas.create_line(0, 2 * CANVAS_HEIGHT / 3, CANVAS_WIDTH, 2 * CANVAS_HEIGHT / 3)

        self.root.bind("<Button-1>", self._click)
    
    def _click(self, event):
        print("Click happened at", event.x, event.y)

        self.cell_size = CANVAS_WIDTH / 3

        self.x_cell = ceil(event.x / self.cell_size)
        self.y_cell = ceil(event.y / self.cell_size)

        print("Cell =", self.x_cell, self.y_cell)

    def tick(self, x, y):
        if x > 3 or x < 1 or y > 3 or y < 1:
            raise Exception('Tick coordinates out of range!')
        
        self.tick_label = Label(self.root, image = self.tick_photoimg)
        self.list_of_labels.append(self.tick_label)
        
        if x == 1:
            self._x = 20
        elif x == 2:
            self._x = CANVAS_HEIGHT / 3 + 20
        elif x == 3:
            self._x = 2 * CANVAS_HEIGHT / 3 + 20
        if y == 1:
            self._y = 20
        elif y == 2:
            self._y = CANVAS_WIDTH / 3 + 20
        elif y == 3:
            self._y = 2 * CANVAS_WIDTH / 3 + 20

        self.tick_label.place(x=self._x, y=self._y)
        #self.cross_label.place(x=115, y=0)
        
    def cross(self, x, y):
        if x > 3 or x < 1 or y > 3 or y < 1:
            raise Exception('Cross coordinates out of range!')
        
        self.cross_label = Label(self.root, image = self.cross_photoimg)
        self.list_of_labels.append(self.cross_label)

        if x == 1:
            self._x = 20
        elif x == 2:
            self._x = CANVAS_HEIGHT / 3 + 20
        elif x == 3:
            self._x = 2 * CANVAS_HEIGHT / 3 + 20
        if y == 1:
            self._y = 20
        elif y == 2:
            self._y = CANVAS_WIDTH / 3 + 20
        elif y == 3:
            self._y = 2 * CANVAS_WIDTH / 3 + 20

        self.cross_label.place(x=self._x, y=self._y)

    def clear(self):
        for label in self.list_of_labels: 
            label.destroy()


controller = Controller()
controller.tick(1, 1)
controller.tick(1, 2)
controller.tick(1, 3)

controller.cross(2, 1)
controller.cross(2, 2)
controller.cross(2, 3)


controller.root.mainloop()