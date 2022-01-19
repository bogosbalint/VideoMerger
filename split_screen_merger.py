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
        self.video_length = ['','','','']
        self.count = 0
        self.master.image = ''

    def configure_gui(self):
        self.master.geometry('600x600')

    def create_widgets(self):
        # Import gomb
        import_btn = tk.Button(self.master, text="Import Video", font=(12), command=self.import_file)
        import_btn.grid(sticky="W", column=0, row=0, padx=10)

        # Mentés gomb
        convert_btn = tk.Button(self.master, text="Convert", font=(12), command=self.convert_videos)
        convert_btn.grid(sticky="W", column=0, row=5, padx=10)

        # Videó neve label
        video_name_label = tk.Label(self.master,  text="Merged video name:", font=12)
        video_name_label.grid(sticky="W",  column=0, row=4, padx=10)

        # Videó neve szövegmező
        self.output_text = tk.Entry(self.master,  width=50)
        self.output_text.grid(sticky="W", column=0, row=4, padx=220)

        # Vízjel beillesztése gomb
        watermark_btn = tk.Button(self.master, text="Import Watermark", font=(12), command=self.import_watermark)
        watermark_btn.grid(sticky="W", column=0, row=1, padx=10)

        # Kép áttetszősége label
        watermark_opacity_label = tk.Label(self.master, text="Watermark opacity:", font=12)
        watermark_opacity_label.grid(sticky="W", column=0, row=2, padx=10)

        # Kép áttetszősége szövegmező
        self.watermark_opacity = tk.Entry(self.master, width=15)
        self.watermark_opacity.grid(sticky="W", column=0, row=2, padx=220)
        self.watermark_opacity.insert(0, '50')

    # Videó importálása
    def import_file(self):
        if self.count != 4:
            self.master.filename = tk.filedialog.askopenfilename(defaultextension=".mp4", filetypes=[("All files", "*.*")])
            file_name = ''
            if self.master.filename.endswith('.mp4'): # fájl típusának leellenőrzése
                length = len(self.master.filename) - 1
                while length != 0:
                    #print(length)
                    if self.master.filename[length] == '/':
                        file_name = self.master.filename[length+1:]
                        break
                    length = length - 1

                print(len(file_name))
                imported_video_label = tk.Label(self.master, justify=tk.LEFT, text=file_name, font=(10))
                imported_video_label.grid(sticky="W", column=0, row=len(self.imported_obj) + 7, padx=10)
                self.imported_obj.append(self.master.filename)

                self.audio1 = tk.BooleanVar()
                self.audio2 = tk.BooleanVar()
                self.audio3 = tk.BooleanVar()
                self.audio4 = tk.BooleanVar()

                # trim mezők & checkboxok
                if self.count == 0:
                    self.clip1_start = tk.Entry(self.master, width=10)
                    self.clip1_start.insert(0, '0,0')
                    self.clip1_start.grid(sticky="W", column=0, row=len(self.imported_obj) + 6, padx=len(file_name) * 12 + 10)

                    self.clip1_end = tk.Entry(self.master, width=10)
                    self.clip1_end.insert(0, '0,0')
                    self.clip1_end.grid(sticky="W", column=0, row=len(self.imported_obj) + 6, padx=len(file_name) * 12 + 90)

                    self.checkbox1 = tk.Checkbutton(self.master, text='Inactive', variable=self.audio1, onvalue=False, offvalue=True)
                    self.checkbox1.grid(sticky="W", column=0, row=len(self.imported_obj) + 6, padx=len(file_name) * 12 + 150)

                if self.count == 1:
                    self.clip2_start = tk.Entry(self.master, width=10)
                    self.clip2_start.insert(0, '0,0')
                    self.clip2_start.grid(sticky="W", column=0, row=len(self.imported_obj) + 6, padx=len(file_name) * 12 + 10)

                    self.clip2_end = tk.Entry(self.master, width=10)
                    self.clip2_end.insert(0, '0,0')
                    self.clip2_end.grid(sticky="W", column=0, row=len(self.imported_obj) + 6, padx=len(file_name) * 12 + 90)

                    self.checkbox2 = tk.Checkbutton(self.master, text='Inactive', variable=self.audio2, onvalue=False, offvalue=True)
                    self.checkbox2.grid(sticky="W", column=0, row=len(self.imported_obj) + 6, padx=len(file_name) * 12 + 150)

                if self.count == 2:
                    self.clip3_start = tk.Entry(self.master, width=10)
                    self.clip3_start.insert(0, '0,0')
                    self.clip3_start.grid(sticky="W", column=0, row=len(self.imported_obj) + 6, padx=len(file_name) * 12 + 10)

                    self.clip3_end = tk.Entry(self.master, width=10)
                    self.clip3_end.insert(0, '0,0')
                    self.clip3_end.grid(sticky="W", column=0, row=len(self.imported_obj) + 6, padx=len(file_name) * 12 + 90)

                    self.checkbox3 = tk.Checkbutton(self.master, text='Inactive', variable=self.audio3, onvalue=False, offvalue=True)
                    self.checkbox3.grid(sticky="W", column=0, row=len(self.imported_obj) + 6, padx=len(file_name) * 12 + 150)

                if self.count == 3:
                    self.clip4_start = tk.Entry(self.master, width=10)
                    self.clip4_start.insert(0, '0,0')
                    self.clip4_start.grid(sticky="W", column=0, row=len(self.imported_obj) + 6, padx=len(file_name) * 12 + 10)

                    self.clip4_end = tk.Entry(self.master, width=10)
                    self.clip4_end.insert(0, '0,0')
                    self.clip4_end.grid(sticky="W", column=0, row=len(self.imported_obj) + 6, padx=len(file_name) * 12 + 90)

                    self.checkbox4 = tk.Checkbutton(self.master, text='Inactive', variable=self.audio4, onvalue=False, offvalue=True)
                    self.checkbox4.grid(sticky="W", column=0, row=len(self.imported_obj) + 6, padx=len(file_name) * 12 + 150)

                self.count = self.count + 1

    #Vízjel
    def import_watermark(self):
        self.master.image = tk.filedialog.askopenfilename(defaultextension=".png", filetypes=[("All files", "*.*")])
        image = self.master.image
        self.watermark = ImageClip(image).set_position("right", "bottom")

        image_length = len(self.master.image) - 1
        while image_length != 0:
            if self.master.image[image_length] == '/':
                image_name = self.master.image[image_length + 1:]
                break
            image_length = image_length - 1

        print(len(image_name))
        imported_video_label = tk.Label(self.master, justify=tk.LEFT, text=image_name, font=(10))
        imported_video_label.grid(sticky="W", column=0, row=6, padx=10)

    def trim(self, file, start, end):
        start, end = tuple(float(i) for i in start.split(',')), tuple(float(i) for i in end.split(','))
        return file.subclip(start, end)

    def get_time(self, time):
        array = time.split(',')
        return int(array[0]) * 60 + int(array[1])

    def convert_videos(self):
        opacity = int(self.watermark_opacity.get()) / 100
        print(opacity)

        if self.count == 2:
            clip1 = VideoFileClip(self.imported_obj[0], audio=self.audio1.get())
            clip2 = VideoFileClip(self.imported_obj[1], audio=self.audio2.get())

            clip1_s, clip1_e = self.clip1_start.get(), self.clip1_end.get()
            clip2_s, clip2_e = self.clip2_start.get(), self.clip2_end.get()

            self.video_length[0] = self.get_time(clip1_e) - self.get_time(clip1_s)
            self.video_length[1] = self.get_time(clip2_e) - self.get_time(clip2_s)

            self.max_length = self.video_length[0]

            if self.video_length[1] > self.max_length:
                self.max_length = self.video_length[1]

            self.merged = clips_array([[self.trim(clip1, clip1_s, clip1_e), self.trim(clip2, clip2_s, clip2_e)]])

        elif self.count == 4:
            clip1 = VideoFileClip(self.imported_obj[0], audio=self.audio1.get())
            clip2 = VideoFileClip(self.imported_obj[1], audio=self.audio2.get())
            clip3 = VideoFileClip(self.imported_obj[2], audio=self.audio3.get())
            clip4 = VideoFileClip(self.imported_obj[3], audio=self.audio4.get())

            clip1_s, clip1_e = self.clip1_start.get(), self.clip1_end.get()
            clip2_s, clip2_e = self.clip2_start.get(), self.clip2_end.get()
            clip3_s, clip3_e = self.clip3_start.get(), self.clip3_end.get()
            clip4_s, clip4_e = self.clip4_start.get(), self.clip4_end.get()

            self.video_length[0] = self.get_time(clip1_e) - self.get_time(clip1_s)
            self.video_length[1] = self.get_time(clip2_e) - self.get_time(clip2_s)
            self.video_length[2] = self.get_time(clip3_e) - self.get_time(clip3_s)
            self.video_length[3] = self.get_time(clip4_e) - self.get_time(clip4_s)

            self.max_length = self.video_length[0]
            for i in len(self.video_length):
                if self.video_length[i] > self.max_length:
                    self.max_length = self.video_length[i]

            self.merged = clips_array([[self.trim(clip1, clip1_s, clip1_e), self.trim(clip2, clip2_s, clip2_e)], [self.trim(clip3, clip3_s, clip3_e), self.trim(clip4, clip4_s, clip4_e)]])

        name = self.output_text.get()
        dir_name = tk.filedialog.askdirectory()

        if self.master.image != '':
            final = CompositeVideoClip([self.merged, self.watermark.set_opacity(opacity).set_duration(self.max_length)])
        else:
            final = CompositeVideoClip([self.merged])

        self.final_name = dir_name + "/" + name + ".mp4"

        final.write_videofile(self.final_name)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Big Python Project")

    main_app =GUI(root)
    root.mainloop()