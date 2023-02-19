#Import the required libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd
import webbrowser
#import glob
from ttkwidgets.autocomplete import AutocompleteCombobox
import tkinter as tk
from PIL import ImageTk,Image #install pillow
import csv
import time
import threading 
from subprocess import Popen
import os
import signal

class Window(Frame):
    def __init__(self, master=None):
        f=open(r"C:/Users/junai/Downloads/archive/stock_metadata.csv" ,"r")

        readcsv=csv.reader(f)

        my_list=[]

        symbol=[]

        for i in readcsv:

            my_list.append(i[0])

            symbol.append(i[2])

        my_list=my_list[1:]

        symbol=symbol[1:]
        self.records=dict(zip(my_list , symbol))
        
        frame = tk.Frame(root, bg='#f25252')
        frame.pack(expand=True)
        
        tk.Label(
            frame,
            bg='#f25252',
            font = ('Times',21),
            text='NIFTY~50'
            ).pack()
        
        self.entry = AutocompleteCombobox(frame, width=20, completevalues=my_list)#list goes here
        self.entry.pack()

        search_button = tk.Button(frame, text="search", command = self.function )  #command = func name
        search_button.pack()
        
    def func(self, file_name):
        # * Run the dash server as separate subprocess, pass the file_name as parameter.

        process = Popen(['c:/Users/junai/Desktop/proj/venv/Scripts/python.exe', 'C:/Users/junai/Desktop/proj/sub_process.py', file_name])
        # * Wait for 10  secs
        time.sleep(10)
        # * Terminate the subprocess created.
        # ! if we don't terminate the subprocess then the subprogram will run continuously
        os.kill(process.pid,signal.SIGTERM)
        
        # * This approach will work correctly if we are going to display only the data and not receiving any data from the webpage
        
    def function(self):
        name=self.entry.get()
        print(str(self.records[name]))#call main from here
        self.func(str(self.records[name]))


root = tk.Tk()
root.title('NIFTY~50')
root.geometry('400x400')
root.config(bg='#f25252')


app = Window(root)


root.mainloop()