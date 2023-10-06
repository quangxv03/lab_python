
import tkinter as tk
from tkinter import ttk
  
#tao cua so tkinter
window = tk.Tk()
window.title('Combobox')
window.geometry('500x250')
  
#tieu de
ttk.Label(window, text = "GFG Combobox Widget", 
          background = 'green', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 1)
  
# label
ttk.Label(window, text = "Select the Month :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)
  
#tao combobox
n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)
  
#them danh sach combobox 
monthchoosen['values'] = (' January', 
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')
  
monthchoosen.grid(column = 1, row = 5)
monthchoosen.current()
window.mainloop()