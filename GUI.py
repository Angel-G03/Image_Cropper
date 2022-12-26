from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from Cropper import Cropp

# Variable will change
file_list = []

def file_select():
    """ A method for the file select button to open the select files window"""
    filenames = fd.askopenfilenames(title="Select Files", filetypes=[("JPG Files", "*.jpg"), ("PNG Files", "*.png")])
    fileset = list(filenames)
    if file_list == []: # First time selecting files
        for file in fileset:
            file_list.append(file)
    else: # After the each file selection, the list must be reset
        file_list.clear()
        for file in fileset:
            file_list.append(file)

# Window
root = Tk()
root.title("Image Cropper")
root.geometry('510x225')
root.resizable(False, False)

title_label = Label(root, text="Image Cropper").grid(row=1, column=1)

# Is there an alternative to blank labels?
blank_space = Label(root, text="").grid(row=0, column=1)

# Entries for new dimensions
top_entry = ttk.Entry(root)
top_entry.grid(row=3, column=3)
top_entry.insert(END, '0')
bottom_entry = ttk.Entry(root)
bottom_entry.grid(row=4, column=3)
bottom_entry.insert(END, '750')
right_entry = ttk.Entry(root)
right_entry.grid(row=5, column=3)
right_entry.insert(END, '1500')
left_entry = ttk.Entry(root)
left_entry.grid(row=6, column=3)
left_entry.insert(END, '0')

# Entry Labels
top_label = Label(root, text="Top:").grid(row=3, column=2)
bottom_label = Label(root, text="Bottom:").grid(row=4, column=2)
right_label = Label(root, text="Right:").grid(row=5, column=2)
left_label = Label(root, text="Left:").grid(row=6, column=2)

# Radio Buttons for Save Option
save_mode = tkinter.StringVar()
oversave_rbutton = Radiobutton(root, text="Overwrite Files", variable=save_mode, value="Overwrite").grid(row=4, column=0)
newsave_rbutton = Radiobutton(root, text="Save New files", variable=save_mode, value="New Save").grid(row=6, column=0)

blank_space2 = Label(root, text="").grid(row=7, column=1)

file_select_button = Button(root, text="Select File(s)", command=file_select).grid(row=8, column=0)

crop_button = Button(root, text="Crop",
command=lambda: Cropp.crop1(int(top_entry.get()), int(bottom_entry.get()), int(left_entry.get()), int(right_entry.get()), save_mode.get(), file_list))
crop_button.grid(row=8, column=3)

root.mainloop()
