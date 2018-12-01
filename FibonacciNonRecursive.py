from tkinter import *

def Fibbonaci(n):
    num1 = 0
    num2 = 1
    
    if n <= 1:
        return n
    else:
        for i in range(n-1):
            num2 = num1 + num2
            num1 = num2 - num1
        return num2
        
def DisplayString(factString):
    n = int(factString)
    newString = str(Fibbonaci(n))
    entry2 = Entry(master)
    entry2.grid(row = 1, column = 1)
    entry2.insert(0,newString)

    
master = Tk()
master.title("Fibbonaci (NonRecursive) Numbers")
master.geometry("300x100+0+0")

Label(master, text = "N:").grid(row = 0)
Label(master, text = "Fibonacci:").grid(row = 1)

entry1 = Entry(master)
entry1.grid(row = 0, column = 1)

factButton = Button(master, text = "Calculate", width = 10, command = lambda: DisplayString(entry1.get())).grid(row = 2, column = 1)

mainloop()