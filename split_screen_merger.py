from moviepy.editor import *
import tkinter as tk
import tkinter.filedialog

class GUI(tk.Frame):

    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.gui = self.configure_gui()
        self.widgets = self.create_widgets()
        self.imported_obj = []
        self.count = 0

    def configure_gui(self):
        self.master.geometry('600x600')

    def create_widgets(self):
        import_btn = tk.Button(self.master, text="Import", font=(12), command=self.import_file)
        import_btn.grid(sticky="W", column=0, row=0, padx=10)

        convert_btn = tk.Button(self.master, text="Convert", font=(12), command=self.convert_videos)
        convert_btn.grid(sticky="W", column=0, row=1, padx=10)

        video_name_label = tk.Label(self.master, text="Merged video name:", font=12)
        video_name_label.grid(sticky="W", column=0, row=2, padx=10)

        self.output_text = tk.Entry(self.master, width=50)
        self.output_text.grid(sticky="W", column=0, row=2, padx=220)

    def import_file(self):
        if self.count != 4:
            self.master.filename = tk.filedialog.askopenfilename(defaultextension=".mp4", filetypes=[("All files", "*.*")])
            file_name = ''
            if self.master.filename.endswith('.mp4'):
                length = len(self.master.filename) - 1
                while length != 0:
                    # print(length)
                    if self.master.filename[length] == '/':
                        file_name = self.master.filename[length + 1:]
                        break
                    length = length - 1
                imported_video_label = tk.Label(self.master, justify=tk.LEFT, text=file_name, font=(10))
                imported_video_label.grid(sticky="W", column=0, row=len(self.imported_obj) + 5, padx=10)
                self.imported_obj.append(self.master.filename)
                
                self.count = self.count + 1

    def convert_videos(self):
        if self.count == 2:
            clip1 = VideoFileClip(self.imported_obj[0])
            clip2 = VideoFileClip(self.imported_obj[1])

            self.merged = clips_array([[clip1, clip2]])

        elif self.count == 4:
            clip1 = VideoFileClip(self.imported_obj[0])
            clip2 = VideoFileClip(self.imported_obj[1])
            clip3 = VideoFileClip(self.imported_obj[2])
            clip4 = VideoFileClip(self.imported_obj[3])

            self.merged = clips_array([[clip1, clip2], [clip3, clip4]])

        name = self.output_text.get()
        dir_name = tk.filedialog.askdirectory()

        self.final_name = dir_name + "/" + name + ".mp4"

        self.merged.write_videofile(self.final_name, codec='libx264')

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Big Python Project")

    main_app =GUI(root)
    root.mainloop()