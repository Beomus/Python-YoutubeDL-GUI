import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()

var1 = tk.StringVar()
var1.set(os.getcwd())
var2 = tk.StringVar()
var2.set('Link')

loc = [os.getcwd()]

def chooseloc():
	des_loc = filedialog.askdirectory()
	loc.clear()
	loc.append(des_loc)
	print(des_loc)
	var1.set(des_loc)

def download():
	link = link_entry.get()
	os.system('youtube-dl ' + link)


frame = tk.Frame(root, bg ="blue", height = 150, width = 200)
frame.pack()

label = tk.Label(frame, text = "Youtube-dl", fg = "red", bg = 'blue', font = "Times 20 bold")
label.pack()

link_entry = tk.Entry(frame, textvariable = var2)
link_entry.pack()

run_ytdl = tk.Button(frame, text = "Download", command = download)
run_ytdl.pack()

choose_dir = tk.Button(frame, text = 'Choose location', command = chooseloc)
choose_dir.pack()

dl_dir = tk.Label(frame, textvariable = var1, bg = 'gray')
dl_dir.pack()

root.mainloop()
