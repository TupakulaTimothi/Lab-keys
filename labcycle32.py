''' Write a program that opens a file dialog that allows you to select a text file. The 
program then displays the contents of the file in a textbox '''

from tkinter import filedialog
from tkinter import Tk
from tkinter import *
root=Tk()
root.fileName=filedialog.askopenfilename(filetypes=(("Text Files",".txt"),("All Files","*.*")))
t1=open(root.filename).read()
T=Text(root,height=25,width=80)
T.pack()
T.insert(END,t1)
root.mainloop()


