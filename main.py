import tkinter as tk

class mycalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry ("300x300")
        self.root.title("mycalculator")

        self.label = tk.Label(self.root, text="hello kitty!", font=('Arial', 18)) 
        self.label.pack()
        self.button = tk.Button(self.root, text="Click Here!", height=4)
        self.button.place(x=10, y=70)

        self.root.mainloop()

mycalculator ()