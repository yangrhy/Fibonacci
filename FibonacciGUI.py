from tkinter import *

def Fibbonaci(n):
    if n <= 1:
        return n
    else:
        return Fibbonaci(n-1) + Fibbonaci(n-2)
        
def DisplayString(factString):
    n = int(factString)
    newString = str(Fibbonaci(n))
    entry2 = Entry(master)
    entry2.grid(row = 1, column = 1)
    entry2.insert(0,newString)

    
master = Tk()
master.title("Fibbonaci Numbers")
master.geometry("300x100+0+0")

Label(master, text = "N:").grid(row = 0)
Label(master, text = "Fibonacci:").grid(row = 1)

entry1 = Entry(master)
entry1.grid(row = 0, column = 1)

factButton = Button(master, text = "Calculate", width = 10, command = lambda: DisplayString(entry1.get())).grid(row = 2, column = 1)

mainloop()