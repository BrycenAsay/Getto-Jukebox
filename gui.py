import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import file_logic as fl
from pathlib import Path

def gui_runtime():
    root = tk.Tk()
    root.title("My App")
    root.geometry("400x300")  # width x height

    label1 = tk.Label(root, text="GD Jukebox Bootleg", font=("Felix Titling", 20))
    label1.pack()

    label2 = tk.Label(root, text="Select Song ID to Replace", font=("", 14))
    label2.pack()

    combo = ttk.Combobox(root, name='jimmy', values=fl.get_song_ids())
    combo.bind("<<ComboboxSelected>>", lambda event: fl.on_combo_select(event, combo, label6))
    combo.pack()

    label6 = tk.Label(root, text="No song ID selected", font=("", 11))
    label6.pack()

    label3 = tk.Label(root, text="Select New Song File", font=("", 14))
    label3.pack()

    button = tk.Button(root, text="Select a Song File", command=lambda: fl.open_file_logic(label4))
    button.pack()

    label4 = tk.Label(root, text="No file selected", font=("", 11))
    label4.pack()

    label5 = tk.Label(root, text="Type Descriptor/Name of Song", font=("", 14))
    label5.pack()

    descriptor = tk.Entry(root)
    descriptor.pack()

    button = tk.Button(root, text="Save", command=lambda: fl.copy_file_over(combo.get(), fl.selected_path, descriptor.get()))
    button.pack()

    label8 = tk.Label(root, text="Restore Old Song Versions", font=("Felix Titling", 20))
    label8.pack()

    label9 = tk.Label(root, text="Select Song ID to Restore Old Versions", font=("", 14))
    label9.pack()

    combo3 = ttk.Combobox(root, name='jimmyb', values=fl.get_song_ids())
    combo3.bind("<<ComboboxSelected>>", lambda event: fl.on_combo_select(event, combo3, label11, combo2))
    combo3.pack()

    label11 = tk.Label(root, text="No song ID selected", font=("", 11))
    label11.pack()

    label9 = tk.Label(root, text="Select Old Song File", font=("", 14))
    label9.pack()

    combo2 = ttk.Combobox(root, name='jimmya', values=[])
    combo2.bind("<<ComboboxSelected>>", lambda event: fl.on_combo_select(event, combo2, label7))
    combo2.pack()

    label7 = tk.Label(root, text="No song ID selected", font=("", 11))
    label7.pack()

    label9 = tk.Label(root, text="Change Descriptor/Name of Song on Restoration", font=("", 14))
    label9.pack()

    descriptor2 = tk.Entry(root)
    descriptor2.pack()

    button2 = tk.Button(root, text="Restore", command=lambda: fl.replace_file_name(combo3.get(), fl.create_old_song_path(combo2.get()), descriptor2.get()))
    button2.pack()

    root.mainloop()