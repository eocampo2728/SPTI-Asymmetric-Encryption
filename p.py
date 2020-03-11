# -*- coding: utf-8 -*-
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import IO
import sys
import GenerateKeys
import decrypt
import encrypt

def genKeys():
   GenerateKeys.main(2048)

def funEnc():
   encrypt.main()

def funDec():
   decrypt.main()

def start():
    root = Tk()
    botonKeys = Button(root, text="Generate keys", command=genKeys)
    boton = Button(root, text="Select your file to encrypt", command=funEnc)
    botonDec = Button(root, text="Select your file to decrypt", command=funDec)
    root.geometry('380x300')
    root.title("Ventana")
    botonKeys.pack()
    boton.pack()
    botonDec.pack()
    root.mainloop()


start()

