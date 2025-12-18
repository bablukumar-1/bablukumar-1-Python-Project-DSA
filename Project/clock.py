import tkinter as tk
from time import strftime

# note: tkinter method and gui in python with strftime means time module

root= tk.Tk()
root.title("Digital Clock by Bablu Sarkar")

def time():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000,time)
    
label=tk.Label(root, font=('calibri', 40, 'bold'),background='yellow', foreground='black' )
label.pack(anchor='center')

time()

root.mainloop()







