#!/usr/bin/env python
from tkinter import *
import os


class Application():
    def __init__(self):
        self.frame = Frame(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="green", highlightthickness=0)
        self.canvas = Canvas(self.frame, bg='blue', width=root.winfo_screenwidth(), height=root.winfo_screenheight(), highlightthickness=0)
        self.label = Label(self.canvas, text="Europawahl 2019 in Berlin nach Wahlbezirken", font='Helvetica 30 bold', highlightthickness=0)
        self.label.place(relx = 0.5,y=50, anchor='center')
        self.canvas.create_image(20, 100, anchor=NW, image=map)
        #self.canvas.bind("<Button-1>", self.open_map)
        self.canvas.place(x=0, y=0)
        self.frame.place(x=0,y=0)
        self.party_button = Button(self.canvas, text="Parteien", command=self.list_party)
        self.district_button = Button(self.canvas, text="Bezirke", command=self.open_map)
        self.quit_button = Button(self.canvas, text="Exit", command=self.quit)
        self.party_button.place(relx=0.75, rely=0.25)
        self.district_button.place(relx=0.75, rely=0.5)
        self.quit_button.place(relx=0.75, rely=0.75)
        self.district_window=None
        self.party_window=None
    def open_map(self):
        self.district_window=districts()
    #def select_distric(self):

    def list_party(self):
        self.party_window=party()

    def quit(self):
        root.destroy()
class districts():
    def __init__(self):
        self.window = Toplevel()
        self.window.title("About this application...")
        self.canvas = Canvas(self.window, highlightthickness=0, bg="red", width=root.winfo_screenwidth(),
                        height=root.winfo_screenheight())
        self.quit = Button(self.canvas, text="Quit", command=self.window.destroy)
        self.quit.place(relx=0.75, rely=0.8)
        self.scrollbar = Scrollbar(self.quit)
        self.scrollbar.place(relx=0.9, rely=0.1)
        self.listbox = Listbox(self.window, yscrollcommand=self.scrollbar.set, width=100)
        self.listbox.place(relx=0.6, rely=0.1)
        self.scrollbar.config(command=self.listbox.yview)
        self.canvas.create_image(20, 100, anchor=NW, image=map)
        self.canvas.pack()
        self.window.wm_geometry("%dx%d+%d+%d" % (1920, 1080, -10, 0))
        self.button_containter=[]
        self.district_button()
    def district_button(self):
        print(root.winfo_pointerx(), ' ', root.winfo_pointery())
        if len(self.button_containter) != 0:
            self.button_containter.clear()
        for i in range(12):
            button=Button(self.window)
            self.button_containter.append(button)
        self.update_button()
    def get_coord(self):
        newFile = open('openbutton_coord.txt', 'a')
        string=str(root.winfo_pointerx()) + ',' + str(root.winfo_pointery()) + ';'
        newFile.write(string)
        print(string)

    def update_button(self):
        index=0
        file=open('openbutton_coord.txt', "r")
        coord_list=[]
        for i in file:
            xy=i.split(";")
            for j in xy:
                x_y=j.split(",")
                coord_list.append(x_y)
        for i in self.button_containter:
            i.config(text=coord_list[index][2])
            i.place(x=coord_list[index][0], y=coord_list[index][1])
            index+=1

class party():
    def __init__(self):
        self.window = Toplevel()
        self.window.title("About this application...")
        self.frame=Frame(self.window, width=root.winfo_screenwidth()/2, height=root.winfo_screenheight(), bg='green')
        self.frame.place(x=0, y=0)
        self.canvas = Canvas(self.frame, highlightthickness=0, bg="red", width=root.winfo_screenwidth()/2,
                             height=root.winfo_screenheight())
        self.canvas_title=Label(self.canvas, text='Parteienliste')
        self.canvas_title.grid(columnspan=5)
        self.canvas.place(x=0,y=0)
        self.window.wm_geometry("%dx%d+%d+%d" % (1920, 1080, -10, 0))
        self.button_container = []
        self.create_buttons()
    def create_buttons(self):
        index=0
        row=1
        column=0
        for i in range(40):
            button=Button(self.canvas)
            self.button_container.append(button)
        file = open('parties.txt', "r")
        name=None
        for i in file:
            name=i.split(",")
        name.sort()
        for i in self.button_container:
            i.config(text=name[index])
            index+=1
        for i in self.button_container:
            i.grid(row=row, column=column)
            row+=1
            if row == 9:
                column+=1
                row=1
    def show_party(self):
        print('party opened')



#class party():
    #def __init__(self):


root = Tk()
root.wm_geometry("%dx%d+%d+%d" % (1920, 1080, -10, 0))
map=PhotoImage(file="map1.png")

app = Application()
root.mainloop()