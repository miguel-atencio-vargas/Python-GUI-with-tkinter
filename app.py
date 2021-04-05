import tkinter as tk
from tkinter import filedialog, Text
import pandas as pd
import os

from scrolling_area import Scrolling_Area
from tkinter_table import Table


filepath = ''
#funciones
def f_openCSV():
    global filepath
    filepath = filedialog.askopenfilename( title='Seleccione un archivo CSV', filetypes=(('Comma Separated Values', '.csv'), ('All files', '*.*')))
    label = tk.Label(frame_title, bg='gray', text=filepath)
    label.pack()

def f_head():
    #mostrar el scrolling
    scrolling_area = Scrolling_Area(frame_data, height=630, width=850)
    scrolling_area.pack()
    # procesamiento de datos
    dataframe = pd.read_csv(filepath)
    data = []
    for i in range(20):
        data.append(dataframe.iloc[i].tolist())
    none_v = [None]*len(list(dataframe))
    table = Table(scrolling_area.innerframe, list(dataframe.head()), column_minwidths=none_v)
    table.pack(expand=True, padx=10, pady=10)
    table.on_change_data(scrolling_area.update_viewport)
    table.set_data(data)
def f_clear():
    list = frame_data.pack_slaves()
    print(list)
    for l in list:
        l.destroy()


root = tk.Tk()
# canvas es la ventana
canvas = tk.Canvas(root, height = 800, width=1350, bg='#00a798')
canvas.pack(side='top')

# los frames son cada seccion de la ventana
frame_title = tk.Frame(root, bg="#de7a4d")
frame_title.place( relheight=0.07, relwidth=0.91, relx=0.04, rely=0.02)

frame_btns = tk.Frame(root, bg="#939598")
frame_btns.place( relheight=0.85, relwidth=0.2, relx=0.75, rely=0.1)

frame_data = tk.Frame(root, bg='#00145a')
frame_data.place(relheight = 0.85, relwidth=0.7, relx=0.04, rely=0.1)

# Buttons
openCSV = tk.Button(frame_btns, text='Cargar CSV', fg="white", command=f_openCSV)
openCSV.pack()

head = tk.Button(frame_btns, text='Show head', fg="white", command=f_head)
head.pack()

clear = tk.Button(frame_btns, text='Limpiar', fg="white", command=f_clear)
clear.pack()



root.mainloop()