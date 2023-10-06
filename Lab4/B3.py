from tkinter import Tk, W, E, END
from tkinter.ttk import Frame, Button, Style, Entry

class Calculator(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Calculator")
        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        entry = Entry(self)
        entry.grid(row=0, column=0, columnspan=4, sticky=W+E)
        
        # Row 1
        clear = Button(self, text="Clear", command=lambda: self.clear_entry(entry))
        clear.grid(row=1, column=0)
        back = Button(self, text="Back", command=lambda: self.backspace_entry(entry))
        back.grid(row=1, column=1)
        div = Button(self, text="", command=lambda: self.on_button_click(entry, ''))
        div.grid(row=1, column=2)
        close = Button(self, text="Close", command=self.parent.quit)
        close.grid(row=1, column=3)
        

        # Row 2
        seven = Button(self, text="7", command=lambda: self.on_button_click(entry, '7'))
        seven.grid(row=2, column=0)
        eight = Button(self, text="8", command=lambda: self.on_button_click(entry, '8'))
        eight.grid(row=2, column=1)
        nine = Button(self, text="9", command=lambda: self.on_button_click(entry, '9'))
        nine.grid(row=2, column=2)
        div = Button(self, text="/", command=lambda: self.on_button_click(entry, '/'))
        div.grid(row=2, column=3)

        # Row 3
        four = Button(self, text="4", command=lambda: self.on_button_click(entry, '4'))
        four.grid(row=3, column=0)
        five = Button(self, text="5", command=lambda: self.on_button_click(entry, '5'))
        five.grid(row=3, column=1)
        six = Button(self, text="6", command=lambda: self.on_button_click(entry, '6'))
        six.grid(row=3, column=2)
        mul = Button(self, text="*", command=lambda: self.on_button_click(entry, '*'))
        mul.grid(row=3, column=3)

        # Row 4
        one = Button(self, text="1", command=lambda: self.on_button_click(entry, '1'))
        one.grid(row=4, column=0)
        two = Button(self, text="2", command=lambda: self.on_button_click(entry, '2'))
        two.grid(row=4, column=1)
        three = Button(self, text="3", command=lambda: self.on_button_click(entry, '3'))
        three.grid(row=4, column=2)
        sub = Button(self, text="-", command=lambda: self.on_button_click(entry, '-'))
        sub.grid(row=4, column=3)

        # Row 5
        zero = Button(self, text="0", command=lambda: self.on_button_click(entry, '0'))
        zero.grid(row=5, column=0)
        dot = Button(self, text=".", command=lambda: self.on_button_click(entry, '.'))
        dot.grid(row=5, column=1)
        equal = Button(self, text="=", command=lambda: self.calculate(entry))
        equal.grid(row=5, column=2)
        add = Button(self, text="+", command=lambda: self.on_button_click(entry, '+'))
        add.grid(row=5, column=3)
        
        self.pack()

    def on_button_click(self, entry, text):
        current_text = entry.get()
        entry.delete(0, END)
        entry.insert(END, current_text + text)

    def clear_entry(self, entry):
        entry.delete(0, END)

    def backspace_entry(self, entry):
        current_text = entry.get()
        entry.delete(0, END)
        entry.insert(END, current_text[:-1])

    def calculate(self, entry):
        try:
            result = eval(entry.get())
            entry.delete(0, END)
            entry.insert(END, str(result))
        except Exception as e:
            entry.delete(0, END)
            entry.insert(END, "Error")

if __name__ == "__main__":
    root = Tk()
    app = Calculator(root)
    root.mainloop()
