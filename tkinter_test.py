import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
greeting = tk.Label(text='Morrowind Alchemy Project',
                    foreground='red',
                    background='black',
                    width=30,
                    height=10)
greeting.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

button.pack()

window.mainloop()