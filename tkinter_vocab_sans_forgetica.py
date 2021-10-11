import tkinter as tk


filename = input("Enter file name to load:")
if '.txt' not in filename: filename+='.txt'

with open(filename, "r") as f:
    lst = [line.strip().split('/') for line in f]
    
lst.sort()
for i in lst:
    print(*i)

win = tk.Tk()

t = tk.Text(win, font=("Sans Forgetica", 16))
t.pack()
for i in lst:
    t.insert('end', ' '.join(i)+'\n')
        
win.mainloop()
