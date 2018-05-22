from tkinter import *
import tkinter.filedialog as fd
from PIL import ImageTk, Image
import pickle
import cv2
import numpy as np

path_to_sample_photo = "C:\\Users\\asus\\Desktop\\data_science_python\\ph_project\\ph_datasets\\ph7\\ph7.jpg"


def load_model(filename="gradient_regression_85.pkl"):
    return pickle.load(open(filename, 'rb'))


# tą funkcję open widzi a tą w klasie juz nie trzeba bedzie jakos to przerobic

def load_img(master):
    file = fd.askopenfile(title='Open')
    filename = file.name
    if len(filename) > 0:
        img = cv2.imread(filename)
        cv_img = img
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        panel = Label(master, image=img)
        panel.pack(side="bottom", fill="both", expand="yes")


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

    def load_img(self):
        file = fd.askopenfile(title='Open')
        filename = file.name
        if len(filename) > 0:
            img = cv2.imread(filename)
            cv_img = img
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img = ImageTk.PhotoImage(img)
            panel = Label(self.master, image=img)
            panel.pack(side="bottom", fill="both", expand="yes")

    def init_window(self):
        self.master.title("ph-project")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Open", command=load_img)
        menu.add_cascade(label="File", menu=file)
        self.master.geometry("500x500")

    # for testing
    def load_picture(self, path):
        cv_img = cv.imread(path)
        self.img = ImageTk.PhotoImage(Image.open(path))
        self.panel = Label(self, image=self.img)
        self.panel.pack(side="bottom", fill="both", expand="yes")


if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    root.mainloop()
