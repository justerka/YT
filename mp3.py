from logging import root
import os
import tkinter as tk
from tracemalloc import stop
import pygame
from tkinter import Listbox, filedialog

# процедура музыка қосады
def play_music():
    selected_song = listbox.get(tk.ACTIVE)
    pygame.mixer.music.load(selected_song)
    pygame.mixer.music.play()

# музыка өшіреді
def stop_music():
    pygame.mixer.music.stop()

# папкадан музыка алады
def load_music():
    folder = filedialog.askdirectory()
    os.chdir(folder)
    songs = [file for file in os.listdir(folder) if file.endswith(".mp3")]
    for song in songs:
        listbox.insert(tk.END, song)

# окно ашады сосын аты
root = tk.Tk()
root.title("mp3 player")

pygame.init()
pygame.mixer.init()

listbox = tk.Listbox(root,width=50)
listbox.pack(pady=10)
# музыка қосатын кнопка
play_button =tk.Button(root,text="play", command=play_music)
play_button.pack(pady=5)
# музыка өшіретін кнопка
stop_button = tk.Button(root,text="stop", command=stop_music)
stop_button.pack(pady=5)
# музыка папкадан алатын кнопка
load_button =tk.Button(root,text="load music", command=load_music)
load_button.pack(pady=10)

root.mainloop()