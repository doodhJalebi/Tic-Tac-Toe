from tkinter import *
from PIL import Image, ImageTk
from math import ceil

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500


class Controller(Frame):
    def __init__(self):

        self.root = Tk()
        self.root.resizable(False, False)
        self.root.title('Tic Tac Toe')
        self.path = './img/'
        self.img_dimensions = (int(CANVAS_HEIGHT / 4), int(CANVAS_HEIGHT / 4))
        self.cell_size = CANVAS_WIDTH / 3

        self.list_of_labels = []
        self.state = [
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1]
        ]
        self.current_player = 0 # We choose tick by default

        self.control_bar_frame = Frame(self.root)
        #self.control_bar_frame.pack(side=BOTTOM)

        self.tick_img_small = Image.open(self.path + 'tick.png').resize((20, 20), Image.ANTIALIAS)
        self.cross_img_small = Image.open(self.path + 'cross.png').resize((20, 20), Image.ANTIALIAS)

        self.tick_photoimg_small = ImageTk.PhotoImage(self.tick_img_small)
        self.cross_photoimg_small = ImageTk.PhotoImage(self.cross_img_small)
        
        self.button_1 = Button(self.control_bar_frame, text="Switch to", 
        image=self.cross_photoimg_small, compound="right", command=self._switchPlayer)
        #self.button_1.pack()

        self.header_frame = Frame(self.root)
        self.header_frame.pack(side=TOP)

        self.current_player_label = Label(self.header_frame, text="Current Player:", image=self.tick_photoimg_small,
        compound="right")
        self.current_player_label.config(font=("Courier", 20))
        self.current_player_label.pack()

        self.canvas = Canvas(self.root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()

        self._createGrid()

        self.tick_img = Image.open(self.path + 'tick.png').resize(self.img_dimensions, Image.ANTIALIAS)
        self.cross_img = Image.open(self.path + 'cross.png').resize(self.img_dimensions, Image.ANTIALIAS)

        self.tick_photoimg = ImageTk.PhotoImage(self.tick_img)
        self.cross_photoimg = ImageTk.PhotoImage(self.cross_img)

        self.canvas.bind("<Button-1>", self._click)
    
    def _click(self, event):

        if event.x <= CANVAS_WIDTH and event.y <= CANVAS_HEIGHT:

            self.x_cell = ceil(event.x / self.cell_size)
            self.y_cell = ceil(event.y / self.cell_size)

            if self.state[self.y_cell - 1][self.x_cell - 1] == -1:

                if self.current_player == 0:
                    self.tick(self.x_cell, self.y_cell)
                elif self.current_player == 1:
                    self.cross(self.x_cell, self.y_cell)

                self.state[self.y_cell - 1][self.x_cell - 1] = self.current_player
                self.temp_check = self._checkVictory()
                if self.temp_check == 0:
                    self.win(0)
                elif self.temp_check == 1:
                    self.win(1)
                else:
                    self._switchPlayer()
    
    def _switchPlayer(self):
        print("switching player")
        if self.current_player == 0:
            self.current_player = 1
            self.button_1.configure(image=self.tick_photoimg_small)
            self.current_player_label.configure(image=self.cross_photoimg_small)
        
        elif self.current_player == 1:
            self.current_player = 0
            self.button_1.configure(image=self.cross_photoimg_small)
            self.current_player_label.configure(image=self.tick_photoimg_small)

    def _createGrid(self):
        self.canvas.create_line(CANVAS_WIDTH / 3, 0, CANVAS_WIDTH / 3, CANVAS_HEIGHT)
        self.canvas.create_line(2 * CANVAS_WIDTH / 3, 0, 2 * CANVAS_WIDTH / 3, CANVAS_HEIGHT)

        self.canvas.create_line(0, CANVAS_HEIGHT / 3, CANVAS_WIDTH, CANVAS_HEIGHT / 3)
        self.canvas.create_line(0, 2 * CANVAS_HEIGHT / 3, CANVAS_WIDTH, 2 * CANVAS_HEIGHT / 3)

    def tick(self, x, y):
        if x > 3 or x < 1 or y > 3 or y < 1:
            raise Exception('Tick coordinates out of range! Coordinates =', x, y)
              
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

        self.canvas.create_image(self._x, self._y, image=self.tick_photoimg, anchor='nw')
        
    def cross(self, x, y):
        if x > 3 or x < 1 or y > 3 or y < 1:
            raise Exception('Cross coordinates out of range!')
              
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

        self.canvas.create_image(self._x, self._y, image=self.cross_photoimg, anchor='nw')

    def clear(self, createGrid=True):
        self.canvas.delete('all')
        if createGrid:
            self._createGrid()

    def _checkVictory(self):
        # Checking for 3 in any row
        for y in self.state:
            if y == [0, 0, 0]:
                return 0
            elif y == [1, 1, 1]:
                return 1
        
        # Checking for 3 in any column
        for i in range(len(self.state)):
            lst = [self.state[x][i] for x in range(len(self.state))] # ith column
            if lst == [0, 0, 0]:
                return 0
            elif lst == [1, 1, 1]:
                return 1
        
        # Checking for 3 in any diagonal
        lst = [self.state[x][x] for x in range(len(self.state))] # primary diagonal
        if lst == [0, 0, 0]:
            return 0
        elif lst == [1, 1, 1]:
            return 1

        lst = [self.state[x][len(self.state) - x - 1] for x in range(len(self.state))] # secondary diagonal
        if lst == [0, 0, 0]:
            return 0
        elif lst == [1, 1, 1]:
            return 1
        
        return None
    
    def win(self, winner):
        self.clear(createGrid=False)
        self.current_player_label.destroy()
        self.header_frame.destroy()
        self.control_bar_frame.destroy()
        self.canvas.destroy()
        
        self.winner_label = Label(self.root, text="Wins!", compound="left")
        self.winner_label.configure(font=("Courier", 44))
        if winner == 0:
            self.winner_label.configure(image=self.tick_photoimg)
        else:
            self.winner_label.configure(image=self.cross_photoimg)
        
        self.winner_label.place(relx=0.5, rely=0.5, anchor=CENTER)



controller = Controller()

controller.root.mainloop()