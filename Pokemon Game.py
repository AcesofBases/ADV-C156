# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 08:27:29 2022

@author: Ace
"""


from tkinter import *
from PIL import ImageTk,Image
import random

root=Tk()
root.title("Pokemon Game")
root.geometry("600x400")
root.configure(background = "lawn green")


abra= ImageTk.PhotoImage(Image.open("abra.jpg"))
bulbasour= ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
charmender= ImageTk.PhotoImage(Image.open("charmender.jpg"))
iyvasour= ImageTk.PhotoImage(Image.open("iyvasour.jpg"))
jigglypuff= ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
kadabra= ImageTk.PhotoImage(Image.open("kadabra.jpg"))
meowth= ImageTk.PhotoImage(Image.open("meowth.jpg"))
nidoking= ImageTk.PhotoImage(Image.open("nidoking.jpg"))
paras= ImageTk.PhotoImage(Image.open("paras.jpg"))
persion= ImageTk.PhotoImage(Image.open("persion.jpg"))
pkachu= ImageTk.PhotoImage(Image.open("pikachu.jpg"))
ratata= ImageTk.PhotoImage(Image.open("ratata.jpg"))

player1 = Label(root,text="Player 1 ",bg="royal blue" ,fg="white")
player1.place(relx=0.1,rely=0.3,anchor=CENTER)
player2 = Label(root,text="Player 2 ", bg="royal blue",fg="white")
player2.place(relx=0.9,rely=0.3,anchor=CENTER)
player1_score=Label(root,bg="royal blue",fg="white")
player1_score.place(relx=0.1,rely=0.4,anchor=CENTER)
player2_score=Label(root,bg="royal blue",fg="white")
player2_score.place(relx=0.9,rely=0.4,anchor=CENTER)
random_dice=Label(root,bg="chocolate1",fg="white")
random_dice.place(relx=0.5,rely=0.5,anchor=CENTER)














root.mainloop()