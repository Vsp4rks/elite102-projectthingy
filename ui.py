import tkinter as tk
import main

window = tk.Tk()
greeting = tk.Label(text="I ACTUALLY MADE THIS WORK!!!!!!")
greeting.pack()
label = tk.Label(text="Stream Genesis by Grimes", background="#34A2FE")
label.pack()
label = tk.Label(text="Name")
entry = tk.Entry()
label.pack()
entry.pack()

window.mainloop()