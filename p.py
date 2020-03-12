# -*- coding: utf-8 -*-
from Tkinter import *
from tkinter.ttk import *
import Tkinter, Tkconstants, tkFileDialog
from tkinter import messagebox
import IO
import sys
import GenerateKeys
import decrypt
import encrypt

def genKeys():
   directory = GenerateKeys.main(2048)
   messagebox.showinfo(message="Las llaves fueron creadas en el directorio "+ directory, title="Título")

def funEnc():
   directory = encrypt.main()
   messagebox.showinfo(message="El mensaje fue cifrado en: "+ directory, title="Título")

def funDec():
   directory = decrypt.main()
   messagebox.showinfo(message="El mensaje fue descifrado en: "+ directory, title="Título")

def start():
    root = Tk()

    style = Style() 
    style.configure('TButton', font = ('calibri', 12, 'bold'), 
                        borderwidth = '3', background="white") 

    botonKeys = Button(root, text="Generate keys", command=genKeys)
    boton = Button(root, text="Select your file to encrypt", command=funEnc)
    botonDec = Button(root, text="Select your file to decrypt", command=funDec)

    root.geometry('380x300')
    root.title("Ventana")

    botonKeys.grid(row = 0, column = 3, padx = 65)
    boton.grid(row = 1, column = 3, padx = 65)
    botonDec.grid(row = 2, column = 3, padx = 65)

    root.mainloop()


start()

