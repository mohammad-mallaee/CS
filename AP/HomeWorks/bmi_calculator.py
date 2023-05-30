import tkinter as tk

root = tk.Tk()
root.title('BMI Calculator')


def show_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi_label['text'] = "BMI: " + str(round(weight / (height ** 2), 3))


img = tk.PhotoImage(file="flower.png")
tk.Label(image=img).grid(columnspan=2, pady=10)

tk.Label(text="Weight: ").grid(column=0, padx=10)
weight_entry = tk.Entry()
weight_entry.grid(row=1, column=1, padx=10)

tk.Label(text="Height: ").grid(column=0, padx=10)
height_entry = tk.Entry()
height_entry.grid(row=2, column=1, padx=10)

calculate_button = tk.Button(text="Calculate", command=show_bmi)
calculate_button.grid(columnspan=2, pady=10)

bmi_label = tk.Label(text="BMI = ")
bmi_label.grid(columnspan=2, pady=10, padx=10)
tk.mainloop()
