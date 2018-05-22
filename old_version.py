"""
ph recognition, load image from file and predict pH
basic - gui version
"""
import pickle
import cv2
import numpy as np
import tkinter as tk
import tkinter.filedialog as fd
from PIL import Image
from PIL import ImageTk


def filename():
    file = fd.askopenfile(title='open')
    return file.name


def load_img():
    global panel, img, cv_img
    file = filename()
    if len(file) > 0:
        img = cv2.imread(file)
        cv_img = img
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        if panel is None:
            panel = tk.Label(image=img)
            panel.image = img
            panel.pack(padx=10, pady=10)
            panel.bind("<Button-1>", on_mouse)
        else:
            panel.configure(image=img)
            panel.image = img


def on_mouse(event):
    red = cv_img[event.y][event.x][2]
    green = cv_img[event.y][event.x][1]
    blue = cv_img[event.y][event.x][0]
    test = np.vstack([blue, green, red]).T
    ph_predict = clf.predict(test)
    text.set("pH: " + str(ph_predict).strip('[]'))


# pickle_in = open(
#     "C:\\Users\\asus\\Desktop\\data_science_python\\ph_project\\saved_models\\gradient_regression_85.pkl", 'rb')
# clf = pickle.load(pickle_in)

# I kave to save model to .pickle file
with open("C:\\Users\\asus\\Desktop\\data_science_python\\ph_project\\saved_models\\model-0.99-v2.pickle", 'rb') as f:
    clf = pickle.load(f)

panel = None
root = tk.Tk()
btn = tk.Button(root, text="Select an image", command=load_img)
btn.pack(side="bottom", fill="both", expand="yes", padx=10, pady=10)
text = tk.StringVar()
text.set('pH meter')
label = tk.Label(root, textvariable=text, font='size, 20')
label.pack(side="top", fill="both", padx=10, pady=10)
root.withdraw()
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))
root.deiconify()
root.mainloop()
