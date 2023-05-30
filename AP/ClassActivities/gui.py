import tkinter as tk
main_window = tk.Tk()
main_window.title("hi")
main_window.geometry("400x600")

lbl = tk.Label(text="ok then")
inp = tk.Entry()
inp.pack()
lbl.pack()

main_window.mainloop()