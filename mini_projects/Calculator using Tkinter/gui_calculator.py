"""trying to create our own calculator """
#import the modules
from tkinter import *

#create screen
root = Tk()

#crteate space for entry AND grid
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

#function for buttons
def get_buttons(a):
    
    #get the input of the button pressed
    current=e.get()
    e.delete(0,END)
    
    #insert the entered string at the back of the queue
    e.insert(0,str(current)+str(a))

def do_clear():
    e.delete(0,END)

#do the evalution of the operations entered    
def call_eval():
    state=e.get()
    e.delete(0,END)
    
    #try evalutiing the string expression
    try:
        ans=eval(state)
        
        #enter the answer back to the output screen
        e.insert(0,ans)
    
    #throw the zero division error if dividing by zero
    except ZeroDivisionError:
        
        #make a new window to display popup of the wrong evalution
        wn=Tk()
        wn.title("Invalid input")
        text=Label(wn,text="You cannot divide by 0 !!! ,operation terminated")
        
        #finish the button
        b=Button(wn,text="OK",command=wn.destroy)
        text.pack()
        b.pack()
    
    #for any other technical error or using invalid arethmetic operators directly from keyboard
    except Exception:
        wn=Tk()
        wn.title("Invalid input")
        text=Label(wn,text="please only use button to put values,your expression cannot be evaluated")
        b=Button(wn,text="OK",command=wn.destroy)
        text.pack()
        b.pack()
        wn.mainloop()

#create the buttons
button_1=Button(root,text="1",padx=25,pady=10,command=lambda:get_buttons(1))
button_2=Button(root,text="2",padx=25,pady=10,command=lambda:get_buttons(2))
button_3=Button(root,text="3",padx=25,pady=10,command=lambda:get_buttons(3))
button_4=Button(root,text="4",padx=25,pady=10,command=lambda:get_buttons(4))
button_5=Button(root,text="5",padx=25,pady=10,command=lambda:get_buttons(5))
button_6=Button(root,text="6",padx=25,pady=10,command=lambda:get_buttons(6))
button_7=Button(root,text="7",padx=25,pady=10,command=lambda:get_buttons(7))
button_8=Button(root,text="8",padx=25,pady=10,command=lambda:get_buttons(8))
button_9=Button(root,text="9",padx=25,pady=10,command=lambda:get_buttons(9))
button_0=Button(root,text="0",padx=25,pady=10,command=lambda:get_buttons(0))
button_add=Button(root,text="+",padx=25,pady=10,command=lambda:get_buttons("+"))
button_equal=Button(root,text='=',padx=25,pady=10,command=call_eval)
button_clear=Button(root,text='clear',padx=25,pady=10,command=do_clear)
button_subtract=Button(root,text="-",padx=25,pady=10,command=lambda:get_buttons("-"))
button_multiply=Button(root,text="x",padx=25,pady=10,command=lambda:get_buttons("*"))
button_divide=Button(root,text="/",padx=25,pady=10,command=lambda:get_buttons("/"))

#put buttons into the grid
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_0.grid(row=4,column=0)
button_add.grid(row=1,column=3)
button_subtract.grid(row=2,column=3)
button_multiply.grid(row=3,column=3)
button_divide.grid(row=4,column=3)
button_clear.grid(row=4,column=2)
button_equal.grid(row=4,column=1)

root.mainloop()
