import tkinter as tk
from pathlib import Path
from tkinter import filedialog
import shutil
import random
from mutagen.id3 import ID3, TIT2, ID3NoHeaderError
import os

selected_path = None

def open_file_logic(label):
    global selected_path
    selected_path = filedialog.askopenfilename()
    if selected_path:
        filename = os.path.basename(selected_path)
        try:
            tags = ID3(selected_path)
            title = tags["TIT2"].text[0]
        except (ID3NoHeaderError, KeyError):
            title = "No title"
        
        label.config(text=f"{filename} — {title}")

def on_combo_select(event, combo, label, combo2=None):
    song_id = combo.get()
    path = Path.home() / "AppData" / "Local" / "GeometryDash" / (song_id + ".mp3")
    try:
        tags = ID3(path)
        title = tags["TIT2"].text[0]
    except (ID3NoHeaderError, KeyError):
        title = "No title"
    label.config(text=f"{song_id} — {title}")
    if combo2 is not None:
        combo2['values'] = get_old_song_ids(combo.get())

def get_song_ids():
    gd_songs = Path.home() / "AppData" / "Local" / "GeometryDash"
    files = [file.replace('.mp3', '') for file in os.listdir(gd_songs) if file.endswith('mp3') and '_old_' not in file]
    files.sort()
    return files

def get_old_song_ids(song_id):
    gd_songs = Path.home() / "AppData" / "Local" / "GeometryDash"
    files = [file.replace('.mp3', '') for file in os.listdir(gd_songs) if file.endswith('mp3') and '_old_' in file and str(song_id) in file]
    files.sort()
    return files

def create_old_song_path(old_song_id_vers):
    file_path = Path.home() / "AppData" / "Local" / "GeometryDash" / (old_song_id_vers + ".mp3")
    return file_path

def replace_file_name(old_song_id, new_file, descriptor=None):
    old_file = Path.home() / "AppData" / "Local" / "GeometryDash" / (str(old_song_id) + '.mp3')
    song_name_o = get_song_name(old_file)
    song_name_n = None
    if '_old_' in str(new_file):
        song_name_n = get_song_name(Path.home() / "AppData" / "Local" / "GeometryDash" / new_file)
    base = str(old_file).replace('.mp3', '')
    i = 1
    while os.path.exists(f"{base}_old_{i}.mp3"):
        i += 1
    os.rename(old_file, f"{base}_old_{i}.mp3")
    os.rename(new_file, f"{base}.mp3")
    set_song_name(Path.home() / "AppData" / "Local" / "GeometryDash" / f"{base}_old_{i}.mp3", song_name_o)
    if descriptor is not None and descriptor != '':
        set_song_name(old_file, descriptor)
    elif song_name_n is not None:
        set_song_name(old_file, song_name_n)

def copy_file_over(old_song_id, new_file, descriptor=None):
    old_file = Path.home() / "AppData" / "Local" / "GeometryDash" / (str(old_song_id) + '.mp3')
    song_name_o = get_song_name(old_file)
    song_name_n = None
    if '_old_' in str(new_file):
        song_name_n = get_song_name(Path.home() / "AppData" / "Local" / "GeometryDash" / new_file)
    base = str(old_file).replace('.mp3', '')
    i = 1
    while os.path.exists(f"{base}_old_{i}.mp3"):
        i += 1
    os.rename(old_file, f"{base}_old_{i}.mp3")
    shutil.copy2(new_file, f"{base}.mp3")
    set_song_name(Path.home() / "AppData" / "Local" / "GeometryDash" / f"{base}_old_{i}.mp3", song_name_o)
    if descriptor is not None and descriptor != '':
        set_song_name(old_file, descriptor)
    elif song_name_n is not None:
        set_song_name(old_file, song_name_n)

def set_song_name(path, name):
    try:
        tags = ID3(path)
    except ID3NoHeaderError:
        tags = ID3()
        tags.save(path)
        tags = ID3(path)
    tags["TIT2"] = TIT2(encoding=3, text=name)
    tags.save()

def get_song_name(path):
    try:
        tags = ID3(path)
        return tags["TIT2"].text[0]
    except:
        return 'No Description'

if __name__ == '__main__':
    get_song_ids()