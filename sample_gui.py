from tkinter import *
from PIL import ImageTk, Image

path_to_sample_photo = "C:\\Users\\asus\\Desktop\\data_science_python\\ph_project\\ph_datasets\\ph7\\ph7.jpg"


class Application(Frame):
    """
    demo app to load image
    images from https://www.shutterstock.com/search/ph+scale
    """

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.load_picture(path_to_sample_photo)

    def init_window(self):
        self.master.title("ph-project")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Open")
        menu.add_cascade(label="File", menu=file)
        self.master.geometry("500x500")

    def load_picture(self, path):
        self.img = ImageTk.PhotoImage(Image.open(path))
        self.panel = Label(self, image=self.img)
        self.panel.pack(side="bottom", fill="both", expand="yes")

    def open_file(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu.add_command(label="Open")


if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    root.mainloop()
