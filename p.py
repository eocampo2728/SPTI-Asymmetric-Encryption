# coding=utf-8
import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb

def funcion(q):
    print('Exelente')
    ans=""
    nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
    if nombrearch!='':
        """Aquí tenemos la variable del archivo"""
        archi1=open(nombrearch, "r", encoding="utf-8")
        q=archi1
        contenido=archi1.read()
        print(nombrearch)
        archi1.close()

    

def start():
    root = tk.Tk()
    q=""
    botonSelectFile = tk.Button(root, text="Select file to encrypt", command=funcion(q))
    print(q)
    root.geometry('380x300')
    root.title("Ventana")
    botonSelectFile.pack()
    root.mainloop()


start()

