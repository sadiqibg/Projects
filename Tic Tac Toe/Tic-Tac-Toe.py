"""
The Tic tac toe game is a simple game that makes use of 'x' and 'o' as player.

The win condition being the first person to connect 3 'x' and 'o'
"""


import random
import config
from tkinter import *
from tkinter import ttk
from methods import *



config.root.title("Tic-Tac Toe game")
config.root.iconbitmap("/Users/abubakaribrahim/Desktop/Final Project/gui/Tutorial/rose.icns")
config.root.geometry("450x450")


title = "THE IS A GAME OF 'X' AND 'O' "
# Title display of the 
mylabel = Label(config.root,text="-----------------------------------------------------------")
mylabel.grid(row=0,column=0,columnspan=2)
mylabel10 = Label(config.root,text=title)
mylabel10.grid(row=1,column=0,columnspan=2)
mylabe11 = Label(config.root,text="-----------------------------------------------------------")
mylabe11.grid(row=2,column=0,columnspan=2)





# Defining the location for 'x' and 'O'
config.label1 = Label(config.root,borderwidth=1,relief="solid",width=2)
config.label1.grid(row=3,column=0,columnspan=2)
config.label2 = Label(config.root,borderwidth=1,relief="solid",width=2)
config.label2.grid(row=3,column=1,columnspan=2)
config.label3 = Label(config.root,borderwidth=1,relief="solid",width=2)
config.label3.grid(row=3,column=2,columnspan=2)

config.label4 = Label(config.root,borderwidth=1,relief="solid",width=2)
config.label4.grid(row=4,column=0,columnspan=2)
config.label5 = Label(config.root,borderwidth=1,relief="solid",width=2)
config.label5.grid(row=4,column=1,columnspan=2)
config.label6 = Label(config.root,borderwidth=1,relief="solid",width=2)
config.label6.grid(row=4,column=2,columnspan=2)

config.label7 = Label(config.root,borderwidth=1,relief="solid",width=2)
config.label7.grid(row=5,column=0,columnspan=2)
config.label8 = Label(config.root,borderwidth=1,relief="solid",width=2)
config.label8.grid(row=5,column=1,columnspan=2)
config.label9 = Label(config.root,borderwidth=1,relief="solid",width=2)
config.label9.grid(row=5,column=2,columnspan=2)

mylabe12 = Label(config.root,text="-----------------------------------------------------------")
mylabe12.grid(row=6,column=0,columnspan=2)






ply1 = Label(config.root,text="Player 1")
ply1.grid(row=7,column=0,columnspan=2)
config.ply1_selection = Label(config.root,text="..")
config.ply1_selection.grid(row=7,column=1,columnspan=2)
ply2 = Label(config.root,text="Player 2")
ply2.grid(row=8,column=0,columnspan=2)
config.ply2_selection = Label(config.root,text="..")
config.ply2_selection.grid(row=8,column=1,columnspan=2)

start = Button(config.root,text="Start",width=15,command=start_game)
start.grid(row=9,column=0,columnspan=5)

loction = Label(config.root,text="Enter Location")
loction.grid(row=10,column=0,columnspan=2)
config.location_entry = Entry(config.root,width=5)
config.location_entry.grid(row=10,column=1,columnspan=2)

place = Button(config.root,text="Place",width=5,command=lambda:place_marker(config.location_entry.get()))
place.grid(row=11,column=0,columnspan=2)
end = Button(config.root,text="End Game",command=end_game)
end.grid(row=11,column=1,columnspan=2)

config.message = Label(config.root,text="Please select start to begin !!",width=35)
config.message.grid(row=12,column=0,columnspan=5)

# main loop of the program
config.root.mainloop()