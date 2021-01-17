import tkinter as tk
import time 
from functools import partial

array = [0, 1, 2, 3, 4]
def printer(i):
    print(array[i])

    
app = tk.Tk() 
app.geometry('150x100')

chkValue = tk.BooleanVar() 
chkValue.set(True)
 
chkExample = tk.Checkbutton(app, text='Check Box', var=chkValue, command = partial(printer, 2))
chkExample.grid(column=0, row=0)


b1 = tk.Button(app, text="Main", command=printer(2))
b1.grid(column=0, row = 1)
app.mainloop()
