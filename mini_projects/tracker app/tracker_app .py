# -*- coding: utf-8 -*-
"""
Created on Wed May 19 19:09:03 2021

@author: kunal
"""

"""first make the gui part in the tkinter"""

from tkinter import *
import sqlite3
from database import *
import matplotlib.pyplot as plt
from IPython import get_ipython
from operator import add

get_ipython().run_line_magic('matplotlib', 'qt')

#create screen
root = Tk()
root.title("Tracker app")

entered_screen = []

def plot_graphs(l):
    final = [0,0,0,0,0]
    for i in l:
        final = list(map(add , final , i))
    
    x = ["College Study", "Coding" ,"Video Games"  , "Reading" , "Innovation"]
    plt.bar(x , final , color = 'g')

def Get_values_last_7():
    l = Get_last_7_values()
    plot_graphs(l)
    
    return 

#fucntion for the getting the data from the user
def submit():
    
    #get the value entered in the box
    v1 = e1.get()
    v2 = e2.get()
    v3 = e3.get()
    v4 = e4.get()
    v5 = e5.get()
    
    #delete the value entered in box
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    
    v1 = int(v1)
    v2 = int(v2)
    v3 = int(v3)
    v4 = int(v4)
    v5 = int(v5)
    
    l = [v1,v2,v3,v4 , v5]
    Update_values(l)
    

#crteate space for entry AND grid
e1=Entry(root,width=10,borderwidth=5)
e2=Entry(root,width=10,borderwidth=5)
e3=Entry(root,width=10,borderwidth=5)
e4=Entry(root,width=10,borderwidth=5)
e5=Entry(root,width=10,borderwidth=5)

#create the labels for the entry 
l1 = Label(root , text = "College Study" , font = ('calibre' , 10 , 'bold'))
l2 = Label(root , text = "Coding" , font = ('calibre' , 10 , 'bold'))
l3 = Label(root , text = "Video Games" , font = ('calibre' , 10 , 'bold'))
l4 = Label(root , text = "Reading" , font = ('calibre' , 10 , 'bold'))
l5 = Label(root , text = "Innovation" , font = ('calibre' , 10 , 'bold'))

#make the buttons for the app
b1 = Button(root , text = "Submit"  ,font = ('calibre' , 10 , 'bold') , command = submit )
b2 = Button(root , text = "Show last 7 days data"  ,font = ('calibre' , 10 , 'bold'),command = Get_values_last_7 )

#place the labels on the grid
l1.grid(row=0 , column =0 , padx = 10)
e1.grid(row=0,column=1,columnspan=4,padx=10,pady=10)

l2.grid(row=1 , column =0 , padx = 10)
e2.grid(row=1,column=1,columnspan=4,padx=10,pady=10)

l3.grid(row=2 , column =0 , padx = 10)
e3.grid(row=2,column=1,columnspan=4,padx=10,pady=10)

l4.grid(row=3 , column =0 , padx = 10)
e4.grid(row=3,column=1,columnspan=4,padx=10,pady=10)

l5.grid(row=4 , column =0 , padx = 10)
e5.grid(row=4,column=1,columnspan=4,padx=10,pady=10)

b1.grid(row=5 , column =1, padx = 10 )
b2.grid(row=7 , column =0, padx = 10)

#function for the submit button




root.mainloop()