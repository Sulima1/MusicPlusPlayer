import os
import customtkinter
import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk

# Initialize the application window
root = customtkinter.CTk()
root.geometry('960x540')
root.title("File Browser with Icons")

# Create a Treeview widget
tree = ttk.Treeview(root)
tree.pack(fill=tk.BOTH, expand=True)

# Load file and folder icons
folder_icon = Image.open("folder_icon.png").resize((20, 20))
file_icon = Image.open("file_icon.png").resize((20, 20))

folder_icon = ImageTk.PhotoImage(folder_icon)
file_icon = ImageTk.PhotoImage(file_icon)

# Dictionary to store images to prevent garbage collection
icon_cache = {"folder": folder_icon, "file": file_icon}

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        tree.delete(*tree.get_children())  # Clear the Treeview
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            is_folder = os.path.isdir(item_path)
            icon = folder_icon if is_folder else file_icon
            tree.insert("", tk.END, text=item, image=icon, values=(item_path,))

# Create a button to browse for folders
browse_button = customtkinter.CTkButton(root, text="Browse Folder", command=browse_folder)
browse_button.pack()

root.mainloop()