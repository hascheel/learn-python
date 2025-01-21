import tkinter as tk

# Funktion zum Verarbeiten von Klicks
def button_click(char):
    global entry_var
    if char == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except Exception:
            entry_var.set("Fehler")
    elif char == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + char)

# Hauptfenster
root = tk.Tk()
root.title("Taschenrechner")

# Eingabefeld
entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons einzeln erstellen
button_7 = tk.Button(root, text="7", font=("Arial", 18), command=lambda: button_click("7"))
button_7.grid(row=1, column=0, padx=5, pady=5)

button_8 = tk.Button(root, text="8", font=("Arial", 18), command=lambda: button_click("8"))
button_8.grid(row=1, column=1, padx=5, pady=5)

button_9 = tk.Button(root, text="9", font=("Arial", 18), command=lambda: button_click("9"))
button_9.grid(row=1, column=2, padx=5, pady=5)

button_div = tk.Button(root, text="/", font=("Arial", 18), command=lambda: button_click("/"))
button_div.grid(row=1, column=3, padx=5, pady=5)

button_4 = tk.Button(root, text="4", font=("Arial", 18), command=lambda: button_click("4"))
button_4.grid(row=2, column=0, padx=5, pady=5)

button_5 = tk.Button(root, text="5", font=("Arial", 18), command=lambda: button_click("5"))
button_5.grid(row=2, column=1, padx=5, pady=5)

button_6 = tk.Button(root, text="6", font=("Arial", 18), command=lambda: button_click("6"))
button_6.grid(row=2, column=2, padx=5, pady=5)

button_mul = tk.Button(root, text="*", font=("Arial", 18), command=lambda: button_click("*"))
button_mul.grid(row=2, column=3, padx=5, pady=5)

button_1 = tk.Button(root, text="1", font=("Arial", 18), command=lambda: button_click("1"))
button_1.grid(row=3, column=0, padx=5, pady=5)

button_2 = tk.Button(root, text="2", font=("Arial", 18), command=lambda: button_click("2"))
button_2.grid(row=3, column=1, padx=5, pady=5)

button_3 = tk.Button(root, text="3", font=("Arial", 18), command=lambda: button_click("3"))
button_3.grid(row=3, column=2, padx=5, pady=5)

button_sub = tk.Button(root, text="-", font=("Arial", 18), command=lambda: button_click("-"))
button_sub.grid(row=3, column=3, padx=5, pady=5)

button_clear = tk.Button(root, text="C", font=("Arial", 18), command=lambda: button_click("C"))
button_clear.grid(row=4, column=0, padx=5, pady=5)

button_0 = tk.Button(root, text="0", font=("Arial", 18), command=lambda: button_click("0"))
button_0.grid(row=4, column=1, padx=5, pady=5)

button_equals = tk.Button(root, text="=", font=("Arial", 18), command=lambda: button_click("="))
button_equals.grid(row=4, column=2, padx=5, pady=5)

button_add = tk.Button(root, text="+", font=("Arial", 18), command=lambda: button_click("+"))
button_add.grid(row=4, column=3, padx=5, pady=5)

# Haupt-Loop starten
root.mainloop()
