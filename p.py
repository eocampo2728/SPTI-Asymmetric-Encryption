# -*- coding: utf-8 -*-
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import IO
import sys
import encrypt



def funcion():
   encrypt.main()

def start():
    root = Tk()
    boton = Button(root, text="Select your file", command=funcion)
    root.geometry('380x300')
    root.title("Ventana")
    boton.pack()
    root.mainloop()


start()

