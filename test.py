import tkinter as tk

def convert():
    try:
        usd = float(entry.get())
        result_label.config(text=f"{usd * 0.92:.2f} EUR")
    except ValueError:
        result_label.config(text="Bitte Zahl eingeben")

root = tk.Tk()
root.title("Currency Converter")

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text="Convert USD to EUR", command=convert)
btn.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()