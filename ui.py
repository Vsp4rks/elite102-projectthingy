import tkinter as tk
import main

window = tk.Tk()
greeting = tk.Label(text="I ACTUALLY MADE THIS WORK!!!!!!")
greeting.pack()
label = tk.Label(text="Stream Genesis by Grimes", background="#34A2FE")
label.pack()
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack

window.mainloop()