import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd

class widget(Tk):
    def __init__(self):
        super().__init__()
        self.my_text = Text(width=40,height=10, font=("Helvetica", 16))
        self.my_text.pack(pady=20)
        self.button_frame = Frame()
        self.button_frame.pack()
        self.clear_button = Button(self.button_frame, text="Clear screen", command=self.clear)
        self.clear_button.grid(row=0, column=0)
        self.get_text_button = Button(self.button_frame, text="Get text", command=self.get_text)
        self.get_text_button.grid(row=0 , column=1, padx=20)
        self.save_text = Button(self.button_frame, text="Save text", command=self.savetext)
        self.save_text.grid(row=0, column=2, padx=20)
        self.save_text = Button(self.button_frame, text="load text", command=self.load_messages)
        self.save_text.grid(row=0, column=3, padx=20)
        self.my_label = Label(text="")
        self.my_label.pack(pady=20)
    def savetext(self):
        file = fd.asksaveasfilename(title="Pick a file you want to save to")
        with open(file,"w") as f:
            f.write(self.my_text.get(1.0, END))
        messagebox.showinfo("Saved",f"Your text has been saved to a txt file called {file}")
    def clear(self):
        self.my_text.delete(1.0, END)
    def get_text(self):
        self.my_label.config(text=self.my_text.get(1.0, END))
    def load_messages(self):
        filename = fd.askopenfilename(title="Select your file")
        if filename == "":
            return
        self.clear()
        with open(filename) as file:
            l = file.read()
        f = l.splitlines()
        for line in f:
            self.my_text.insert(1.0, line)
        messagebox.showinfo("Loaded",f"{len(l)} characters has been loaded from a txt file called {filename}")
if __name__ == "__main__":
    g = widget()
    g.title("Textbox")
    g.geometry("1920x1080")
    g.mainloop()