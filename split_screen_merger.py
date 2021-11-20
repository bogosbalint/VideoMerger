from moviepy.editor import *
import tkinter as tk
import tkinter.filedialog

class GUI(tk.Frame):

    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.gui = self.configure_gui()
        self.widgets = self.create_widgets()

    def configure_gui(self):
        self.master.geometry('600x600')

    def create_widgets(self):
        print('widget')

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Big Python Project")

    main_app =GUI(root)
    root.mainloop()